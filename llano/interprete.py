"""Intérprete de Llano: ejecuta el árbol de derivación.

Es un intérprete de recorrido de árbol (tree-walking): cada método
visitX da el significado (semántica) de la regla X de la gramática.
"""

import operator

from .errores import ErrorLlano
from .generado.LlanoParser import LlanoParser
from .generado.LlanoVisitor import LlanoVisitor
from .valores import (FalloNativo, Funcion, Nativa, a_texto, crear_nativas, es_entero,
                      es_numero, iguales, nombre_tipo, normalizar, representar)

MAX_EXPONENTE = 10_000
MAX_PROFUNDIDAD = 3000
MAX_TEXTO = 10_000_000


class Retorno(Exception):
    """Se usa para salir de una función con 'retornar'."""

    def __init__(self, valor):
        super().__init__()
        self.valor = valor


class Entorno:
    """Tabla de variables en tiempo de ejecución, encadenada a su entorno padre."""

    def __init__(self, padre=None):
        self.valores = {}
        self.padre = padre

    def buscar_entorno(self, nombre):
        e = self
        while e is not None:
            if nombre in e.valores:
                return e
            e = e.padre
        return None

    def obtener(self, nombre):
        e = self.buscar_entorno(nombre)
        if e is None:
            raise KeyError(nombre)
        return e.valores[nombre]


def _describir(v):
    """Describe un valor para los mensajes: 'un número (5)', 'una lista', 'nulo'."""
    if v is None:
        return "nulo"
    if isinstance(v, list):
        return "una lista"
    if isinstance(v, (Funcion, Nativa)):
        return "una función"
    articulo = {"número": "un número", "texto": "un texto", "lógico": "un valor lógico"}
    return f"{articulo.get(nombre_tipo(v), nombre_tipo(v))} ({representar(v)})"


P = LlanoParser


def _paso_directo(ctx):
    """Si el nodo solo reenvía a un hijo (no aporta significado), devuelve ese hijo."""
    t = type(ctx)
    if t is P.ExpresionContext or t is P.SentenciaContext or t is P.AgrupacionContext:
        return ctx.getChild(0) if t is P.SentenciaContext else ctx.expresion() if t is P.AgrupacionContext else ctx.disyuncion()
    if t is P.DisyuncionContext or t is P.ConjuncionContext or t is P.ComparacionContext \
            or t is P.SumaContext or t is P.ProductoContext or t is P.PostfijoContext:
        return ctx.getChild(0) if ctx.getChildCount() == 1 else None
    if t is P.NegacionContext:
        return ctx.comparacion() if ctx.NO() is None else None
    if t is P.UnarioContext:
        return ctx.potencia() if ctx.MENOS() is None else None
    if t is P.PotenciaContext:
        return ctx.postfijo() if ctx.POT() is None else None
    return None


class Interprete(LlanoVisitor):
    def __init__(self, salida=print, entrada=input):
        self.nativas = Entorno()
        self.nativas.valores.update(crear_nativas(salida, entrada))
        self.globales = Entorno(self.nativas)
        self.entorno = self.globales
        self.profundidad = 0
        self._atajos = {}
        self._bloques = {}

    # -- atajos en el recorrido -----------------------------------------

    def visit(self, ctx):
        """Las reglas de precedencia forman cadenas de nodos con un solo hijo
        (expresion -> disyuncion -> ... -> primario). El significado no cambia
        al saltarlas, así que cada nodo se resuelve una vez a su destino real
        y se guarda: el programa corre varias veces más rápido."""
        try:
            metodo, destino = self._atajos[ctx]
        except KeyError:
            destino = ctx
            while True:
                siguiente = _paso_directo(destino)
                if siguiente is None:
                    break
                destino = siguiente
            metodo = getattr(self, "visit" + type(destino).__name__[:-len("Context")])
            self._atajos[ctx] = (metodo, destino)
        return metodo(destino)

    # -- utilidades ---------------------------------------------------

    @staticmethod
    def error(ctx, mensaje):
        tok = ctx.getSymbol() if hasattr(ctx, "getSymbol") else ctx.start
        return ErrorLlano("ejecucion", mensaje, tok.line, tok.column)

    def condicion(self, ctx, palabra):
        valor = self.visit(ctx)
        if not isinstance(valor, bool):
            raise self.error(ctx, f"la condición del '{palabra}' debe ser verdadero o falso, "
                                  f"pero es {_describir(valor)}")
        return valor

    def ejecutar_bloque(self, bloque, entorno=None):
        """Ejecuta un bloque. Cada bloque de si/mientras/para tiene su propio
        ámbito: lo que se declara dentro no existe afuera."""
        anterior = self.entorno
        self.entorno = entorno if entorno is not None else Entorno(anterior)
        try:
            self.ejecutar_sentencias(bloque.sentencia())
        finally:
            self.entorno = anterior

    def ejecutar_sentencias(self, sentencias):
        """Primero define las funciones del bloque (elevación) y luego ejecuta
        el resto de sentencias en orden. Devuelve el valor de la última."""
        clave = sentencias[0] if sentencias else None
        partes = self._bloques.get(clave)
        if partes is None:
            partes = ([s.funcion() for s in sentencias if s.funcion()],
                      [s for s in sentencias if not s.funcion()])
            self._bloques[clave] = partes
        funciones, resto = partes
        for f in funciones:
            self.visit(f)
        ultimo = None
        for s in resto:
            ultimo = self.visit(s)
        return ultimo

    # -- programa y sentencias ---------------------------------------

    def visitPrograma(self, ctx):
        return self.ejecutar_sentencias(ctx.sentencia())

    def visitSentencia(self, ctx):
        return self.visit(ctx.getChild(0))

    def visitDeclaracion(self, ctx):
        nombre = ctx.ID().getText()
        if nombre in self.entorno.valores:
            raise self.error(ctx.ID(), f"'{nombre}' ya fue declarada en este ámbito")
        valor = self.visit(ctx.expresion()) if ctx.expresion() else None
        self.entorno.valores[nombre] = valor
        return None

    def visitAsignacion(self, ctx):
        nombre = ctx.ID().getText()
        destino = self.entorno.buscar_entorno(nombre)
        if destino is None or destino is self.nativas:
            raise self.error(ctx.ID(), f"la variable '{nombre}' no ha sido declarada")
        valor = self.visit(ctx.expresion())
        indices = ctx.indice()
        if not indices:
            destino.valores[nombre] = valor
            return None
        contenedor = destino.valores[nombre]
        for ind in indices[:-1]:
            contenedor = self.indexar(ind, contenedor, self.visit(ind.expresion()))
        ultimo = indices[-1]
        pos = self.visit(ultimo.expresion())
        if isinstance(contenedor, str):
            raise self.error(ultimo, "los textos no se pueden modificar por posición; "
                                     "construye un texto nuevo")
        if not isinstance(contenedor, list):
            raise self.error(ultimo, f"solo se puede asignar por posición en una lista, "
                                     f"no en {nombre_tipo(contenedor)}")
        contenedor[self.posicion(ultimo, contenedor, pos)] = valor
        return None

    def visitCondicional(self, ctx):
        condiciones = ctx.expresion()
        bloques = ctx.bloque()
        for cond, bloque in zip(condiciones, bloques):
            if self.condicion(cond, "si"):
                self.ejecutar_bloque(bloque)
                return None
        if len(bloques) > len(condiciones):      # hay 'sino' final
            self.ejecutar_bloque(bloques[-1])
        return None

    def visitMientras(self, ctx):
        while self.condicion(ctx.expresion(), "mientras"):
            self.ejecutar_bloque(ctx.bloque())
        return None

    def visitPara(self, ctx):
        exprs = ctx.expresion()
        inicio, fin = self.visit(exprs[0]), self.visit(exprs[1])
        for e, v, parte in ((exprs[0], inicio, "desde"), (exprs[1], fin, "hasta")):
            if not es_numero(v):
                raise self.error(e, f"el valor de '{parte}' debe ser un número, pero es {_describir(v)}")
        if len(exprs) == 3:
            paso = self.visit(exprs[2])
            if not es_numero(paso):
                raise self.error(exprs[2], f"el 'paso' debe ser un número, pero es {_describir(paso)}")
            if paso == 0:
                raise self.error(exprs[2], "el 'paso' no puede ser 0 (el ciclo no terminaría)")
        else:
            paso = 1      # para contar hacia atrás se escribe: paso -1

        # Si la variable del ciclo no existe, se crea solo para el ciclo.
        nombre = ctx.ID().getText()
        ciclo = Entorno(self.entorno)
        destino = self.entorno.buscar_entorno(nombre)
        if destino is None or destino is self.nativas:
            destino = ciclo
        i = inicio
        while (i <= fin) if paso > 0 else (i >= fin):
            destino.valores[nombre] = normalizar(i)
            self.ejecutar_bloque(ctx.bloque(), Entorno(ciclo))
            i += paso
        return None

    def visitFuncion(self, ctx):
        nombre = ctx.ID().getText()
        parametros = [p.getText() for p in ctx.parametros().ID()] if ctx.parametros() else []
        self.entorno.valores[nombre] = Funcion(nombre, parametros, ctx.bloque(), self.entorno)
        return None

    def visitRetorno(self, ctx):
        raise Retorno(self.visit(ctx.expresion()))

    # -- expresiones: operadores lógicos -------------------------------

    def visitExpresion(self, ctx):
        return self.visit(ctx.disyuncion())

    def visitDisyuncion(self, ctx):
        partes = ctx.conjuncion()
        if len(partes) == 1:
            return self.visit(partes[0])
        for p in partes:                      # evaluación en cortocircuito
            if self.logico(p, "o"):
                return True
        return False

    def visitConjuncion(self, ctx):
        partes = ctx.negacion()
        if len(partes) == 1:
            return self.visit(partes[0])
        for p in partes:
            if not self.logico(p, "y"):
                return False
        return True

    def visitNegacion(self, ctx):
        if ctx.NO():
            return not self.logico(ctx.negacion(), "no")
        return self.visit(ctx.comparacion())

    def logico(self, ctx, operador):
        v = self.visit(ctx)
        if not isinstance(v, bool):
            raise self.error(ctx, f"el operador '{operador}' necesita valores lógicos "
                                  f"(verdadero o falso), pero recibió {_describir(v)}")
        return v

    # -- expresiones: comparación y aritmética --------------------------

    COMPARADORES = {"<": operator.lt, ">": operator.gt, "<=": operator.le, ">=": operator.ge}

    def visitComparacion(self, ctx):
        sumas = ctx.suma()
        izq = self.visit(sumas[0])
        if len(sumas) == 1:
            return izq
        der = self.visit(sumas[1])
        op = ctx.opRel().getText()
        if op == "==":
            return iguales(izq, der)
        if op == "!=":
            return not iguales(izq, der)
        if (es_numero(izq) and es_numero(der)) or (isinstance(izq, str) and isinstance(der, str)):
            return self.COMPARADORES[op](izq, der)
        raise self.error(ctx.opRel(), f"no se puede comparar {nombre_tipo(izq)} con "
                                      f"{nombre_tipo(der)} usando '{op}'")

    def visitSuma(self, ctx):
        terminos = ctx.producto()
        valor = self.visit(terminos[0])
        for op_ctx, t in zip(ctx.opSuma(), terminos[1:]):
            der = self.visit(t)
            valor = self.sumar(op_ctx, op_ctx.getText(), valor, der)
        return valor

    def sumar(self, ctx, op, a, b):
        if es_numero(a) and es_numero(b):
            return normalizar(a + b if op == "+" else a - b)
        if op == "+":
            if isinstance(a, str) or isinstance(b, str):
                return a_texto(a) + a_texto(b)          # concatenación
            if isinstance(a, list) and isinstance(b, list):
                return a + b
        raise self.error(ctx, f"no se puede aplicar '{op}' a {nombre_tipo(a)} y {nombre_tipo(b)}")

    def visitProducto(self, ctx):
        factores = ctx.unario()
        valor = self.visit(factores[0])
        for op_ctx, f in zip(ctx.opProd(), factores[1:]):
            der = self.visit(f)
            valor = self.multiplicar(op_ctx, op_ctx.getText(), valor, der)
        return valor

    def multiplicar(self, ctx, op, a, b):
        if op == "*":
            # Potencia de una cadena: "ab" * 3 = "ababab" (Unidad 1)
            if isinstance(a, str) and es_entero(b) or isinstance(b, str) and es_entero(a):
                texto, n = (a, int(b)) if isinstance(a, str) else (b, int(a))
                if n < 0:
                    raise self.error(ctx, "no se puede repetir un texto un número negativo de veces")
                if len(texto) * n > MAX_TEXTO:
                    raise self.error(ctx, f"el texto resultante es demasiado grande "
                                          f"(más de {MAX_TEXTO:,} caracteres)".replace(",", "."))
                return texto * n
        if not (es_numero(a) and es_numero(b)):
            raise self.error(ctx, f"no se puede aplicar '{op}' a {nombre_tipo(a)} y {nombre_tipo(b)}")
        if op == "*":
            return normalizar(a * b)
        if b == 0:
            raise self.error(ctx, "división por cero" if op == "/" else "módulo por cero")
        if op == "/":
            if isinstance(a, int) and isinstance(b, int) and a % b == 0:
                return a // b
            return normalizar(a / b)
        return normalizar(a % b)

    def visitUnario(self, ctx):
        if ctx.MENOS():
            v = self.visit(ctx.unario())
            if not es_numero(v):
                raise self.error(ctx, f"no se puede aplicar '-' a {_describir(v)}")
            return -v
        return self.visit(ctx.potencia())

    def visitPotencia(self, ctx):
        base = self.visit(ctx.postfijo())
        if not ctx.POT():
            return base
        exp = self.visit(ctx.unario())
        if not (es_numero(base) and es_numero(exp)):
            raise self.error(ctx.POT(), f"no se puede aplicar '^' a {nombre_tipo(base)} y {nombre_tipo(exp)}")
        if base == 0 and exp < 0:
            raise self.error(ctx.POT(), "división por cero (0 elevado a un exponente negativo)")
        if abs(exp) > MAX_EXPONENTE and abs(base) > 1:
            raise self.error(ctx.POT(), "el resultado es demasiado grande")
        if base < 0 and not es_entero(exp):
            raise self.error(ctx.POT(), "una base negativa solo admite exponentes enteros")
        if isinstance(base, int) and es_entero(exp) and exp >= 0:
            return base ** int(exp)
        return normalizar(float(base) ** exp)

    # -- llamadas e índices -------------------------------------------

    def visitPostfijo(self, ctx):
        valor = self.visit(ctx.primario())
        for i in range(1, ctx.getChildCount()):
            hijo = ctx.getChild(i)
            if isinstance(hijo, LlanoParser.LlamadaContext):
                args = [self.visit(e) for e in hijo.argumentos().expresion()] if hijo.argumentos() else []
                valor = self.llamar(hijo, valor, args)
            else:
                valor = self.indexar(hijo, valor, self.visit(hijo.expresion()))
        return valor

    def posicion(self, ctx, contenedor, pos):
        if not es_entero(pos):
            raise self.error(ctx, f"la posición debe ser un número entero, pero es {_describir(pos)}")
        pos = int(pos)
        if not 0 <= pos < len(contenedor):
            if len(contenedor) == 0:
                vacio = "la lista está vacía" if isinstance(contenedor, list) else "el texto está vacío"
                raise self.error(ctx, f"posición {pos} fuera de rango: {vacio}")
            raise self.error(ctx, f"posición {pos} fuera de rango (válidas: 0 a {len(contenedor) - 1})")
        return pos

    def indexar(self, ctx, contenedor, pos):
        if not isinstance(contenedor, (list, str)):
            raise self.error(ctx, f"solo se puede acceder por posición a listas y textos, "
                                  f"no a {nombre_tipo(contenedor)}")
        return contenedor[self.posicion(ctx, contenedor, pos)]

    def llamar(self, ctx, funcion, args):
        if isinstance(funcion, Nativa):
            n = len(args)
            if n < funcion.minimo or (funcion.maximo is not None and n > funcion.maximo):
                raise self.error(ctx, f"'{funcion.nombre}' no acepta {n} argumento(s)")
            try:
                return funcion.implementacion(*args)
            except FalloNativo as fallo:
                raise self.error(ctx, str(fallo))
        if not isinstance(funcion, Funcion):
            raise self.error(ctx, f"solo se pueden llamar funciones, y esto es {_describir(funcion)}")
        if len(args) != funcion.aridad:
            raise self.error(ctx, f"'{funcion.nombre}' recibe {funcion.aridad} argumento(s), "
                                  f"pero se le pasaron {len(args)}")
        if self.profundidad >= MAX_PROFUNDIDAD:
            raise self.error(ctx, "demasiadas llamadas anidadas (¿una recursión sin caso base?)")
        local = Entorno(funcion.cierre)
        local.valores.update(zip(funcion.parametros, args))
        self.profundidad += 1
        try:
            self.ejecutar_bloque(funcion.cuerpo, local)
            return None
        except Retorno as r:
            return r.valor
        finally:
            self.profundidad -= 1

    # -- valores primarios --------------------------------------------

    def visitNumero(self, ctx):
        texto = ctx.getText()
        return float(texto) if "." in texto else int(texto)

    def visitTexto(self, ctx):
        crudo = ctx.getText()[1:-1]
        resultado, i = [], 0
        escapes = {"n": "\n", "t": "\t", '"': '"', "\\": "\\"}
        while i < len(crudo):
            c = crudo[i]
            if c == "\\" and i + 1 < len(crudo):
                resultado.append(escapes.get(crudo[i + 1], crudo[i + 1]))
                i += 2
            else:
                resultado.append(c)
                i += 1
        return "".join(resultado)

    def visitLogico(self, ctx):
        return ctx.VERDADERO() is not None

    def visitNulo(self, ctx):
        return None

    def visitIdentificador(self, ctx):
        nombre = ctx.getText()
        try:
            return self.entorno.obtener(nombre)
        except KeyError:
            raise self.error(ctx, f"'{nombre}' no ha sido declarado")

    def visitLista(self, ctx):
        return [self.visit(e) for e in ctx.argumentos().expresion()] if ctx.argumentos() else []

    def visitAgrupacion(self, ctx):
        return self.visit(ctx.expresion())
