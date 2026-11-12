"""Análisis semántico: revisa el programa antes de ejecutarlo.

Recorre el árbol de derivación con una tabla de símbolos por ámbitos y
detecta, sin ejecutar nada:

  * usos de nombres que no han sido declarados,
  * declaraciones repetidas en el mismo ámbito y parámetros repetidos,
  * asignaciones a funciones,
  * 'retornar' fuera de una función,
  * llamadas con una cantidad incorrecta de argumentos (cuando la
    función se conoce en el análisis),
  * 'romper' y 'continuar' fuera de un ciclo,
  * errores matemáticos en expresiones constantes (1 / 0, x % 0,
    raiz(-4), 0 ^ -1, ...): se evalúan antes de ejecutar,
  * condiciones constantes que no son lógicas (si 1 entonces ...),
  * ciclos infinitos evidentes: 'mientras verdadero' sin 'romper' ni
    'retornar', y 'para' con 'paso 0'.

También produce advertencias (no detienen el programa) para ciclos que
nunca se ejecutan y ciclos cuya condición no cambia dentro del cuerpo.
Detectar TODOS los ciclos infinitos es imposible (problema de la parada);
para el resto, el intérprete limita la cantidad de repeticiones.

Las funciones se declaran al inicio de su bloque y sus cuerpos se revisan
al final, así una función puede usarse antes de la línea donde está escrita
y puede llamar a otra declarada después.
"""

import difflib

from antlr4.tree.Tree import TerminalNode

from .errores import PALABRAS_RESERVADAS, ErrorLlano, ErroresLlano
from .generado.LlanoParser import LlanoParser
from .generado.LlanoVisitor import LlanoVisitor
from .valores import NATIVAS, representar

P = LlanoParser

# Funciones predefinidas sin efectos (no leen ni escriben, no son al azar):
# con argumentos constantes dan siempre el mismo resultado.
PURAS = {"raiz", "logaritmo", "absoluto", "entero", "redondear", "numero", "texto",
         "longitud", "invertir", "subcadena", "tipo"}

# Nodos que son expresiones (candidatos a evaluarse como constantes).
EXPRESIONES = (P.ExpresionContext, P.DisyuncionContext, P.ConjuncionContext,
               P.NegacionContext, P.ComparacionContext, P.SumaContext, P.ProductoContext,
               P.UnarioContext, P.PotenciaContext, P.PostfijoContext, P.PrimarioContext)


class Simbolo:
    def __init__(self, nombre, clase, minimo=None, maximo=None):
        self.nombre = nombre
        self.clase = clase          # 'variable', 'parametro', 'funcion' o 'nativa'
        self.minimo = minimo
        self.maximo = maximo


class Ambito:
    def __init__(self, padre=None, nombre="global"):
        self.padre = padre
        self.nombre = nombre
        self.simbolos = {}

    def buscar(self, nombre):
        ambito = self
        while ambito is not None:
            if nombre in ambito.simbolos:
                return ambito.simbolos[nombre]
            ambito = ambito.padre
        return None


def _todos_los_nombres(ambito):
    nombres = []
    while ambito is not None:
        nombres.extend(ambito.simbolos)
        ambito = ambito.padre
    return nombres


class AnalizadorSemantico(LlanoVisitor):
    def __init__(self, nombres_previos=None):
        self.errores = []
        self.nativo = Ambito(nombre="nativo")
        for nombre, (mi, ma) in NATIVAS.items():
            self.nativo.simbolos[nombre] = Simbolo(nombre, "nativa", mi, ma)
        self.global_ = Ambito(self.nativo, "global")
        for nombre, simbolo in (nombres_previos or {}).items():
            self.global_.simbolos[nombre] = simbolo
        self.actual = self.global_
        self.en_funcion = 0
        self.en_ciclo = 0
        self.pendientes = []
        self.advertencias = []
        self._constantes = {}
        self._evaluador = None

    # -- utilidades ---------------------------------------------------

    def error(self, token_o_ctx, mensaje):
        if hasattr(token_o_ctx, "getSymbol"):      # nodo terminal
            tok = token_o_ctx.getSymbol()
        else:                                      # nodo de regla
            tok = token_o_ctx.start
        self.errores.append(ErrorLlano("semantico", mensaje, tok.line, tok.column))

    def advertir(self, ctx, mensaje):
        tok = ctx.getSymbol() if hasattr(ctx, "getSymbol") else ctx.start
        self.advertencias.append(ErrorLlano("advertencia", mensaje, tok.line, tok.column))

    # -- expresiones constantes ---------------------------------------

    def es_constante(self, ctx):
        """Una expresión es constante si solo tiene literales, operadores y
        llamadas a funciones predefinidas puras: su valor no depende de la
        ejecución, así que se puede calcular durante el análisis."""
        if isinstance(ctx, TerminalNode):
            return ctx.getSymbol().type != P.ID
        if isinstance(ctx, P.PostfijoContext) and isinstance(ctx.primario(), P.IdentificadorContext):
            nombre = ctx.primario().ID().getText()
            simbolo = self.actual.buscar(nombre)
            hijos = [ctx.getChild(i) for i in range(1, ctx.getChildCount())]
            if not (simbolo is not None and simbolo.clase == "nativa" and nombre in PURAS
                    and hijos and isinstance(hijos[0], P.LlamadaContext)):
                return False
            llamada = hijos[0]
            n = len(llamada.argumentos().expresion()) if llamada.argumentos() else 0
            if n < simbolo.minimo or (simbolo.maximo is not None and n > simbolo.maximo):
                return False
            return all(self.es_constante(h) for h in hijos)
        return all(self.es_constante(ctx.getChild(i)) for i in range(ctx.getChildCount()))

    def constante(self, ctx):
        """Devuelve (True, valor) si la expresión es constante y se puede
        evaluar sin errores; si no, (False, None). Los errores de la
        evaluación (p. ej. una división por cero) se informan una sola vez."""
        if ctx in self._constantes:
            return self._constantes[ctx]
        resultado = (False, None)
        if self.es_constante(ctx):
            if self._evaluador is None:
                from .interprete import Interprete   # import tardío: evita ciclo de imports
                self._evaluador = Interprete(salida=lambda *_: None, entrada=lambda *_: "")
            try:
                resultado = (True, self._evaluador.visit(ctx))
            except ErrorLlano as e:
                self.errores.append(ErrorLlano("semantico", e.mensaje + " (detectado antes de ejecutar)",
                                               e.linea, e.columna))
            except Exception:  # noqa: BLE001 - si no se puede evaluar, se deja para la ejecución
                pass
        self._constantes[ctx] = resultado
        return resultado

    def visit(self, ctx):
        # Una expresión constante se evalúa completa (y así se revisan sus
        # restricciones matemáticas); las demás se recorren normalmente.
        if isinstance(ctx, EXPRESIONES) and self.es_constante(ctx):
            self.constante(ctx)
            return None
        return super().visit(ctx)

    def visitChildren(self, node):
        # El recorrido por defecto de ANTLR llama a accept() y se saltaría
        # el método visit() de arriba; aquí todo pasa por visit().
        for i in range(node.getChildCount()):
            hijo = node.getChild(i)
            if not isinstance(hijo, TerminalNode):
                self.visit(hijo)
        return None

    def condicion_constante(self, cond, palabra):
        """Revisa la condición de un si/mientras. Devuelve su valor si es
        constante y lógica; si no, None."""
        ok, valor = self.constante(cond)
        if not ok:
            return None
        if not isinstance(valor, bool):
            self.error(cond, f"la condición del '{palabra}' debe ser verdadero o falso, "
                             f"pero siempre vale {representar(valor)}")
            return None
        return valor

    # -- ciclos -------------------------------------------------------

    @staticmethod
    def _buscar(ctx, tipos, sin_entrar=()):
        """¿Hay un nodo de 'tipos' dentro de ctx, sin entrar en 'sin_entrar'?"""
        for i in range(ctx.getChildCount()):
            h = ctx.getChild(i)
            if isinstance(h, TerminalNode):
                continue
            if isinstance(h, tipos):
                return True
            if isinstance(h, sin_entrar):
                continue
            if AnalizadorSemantico._buscar(h, tipos, sin_entrar):
                return True
        return False

    def tiene_salida(self, bloque):
        """¿El cuerpo de un ciclo tiene una forma de salir de él?
        'romper' (de este ciclo, no de uno interno) o 'retornar'."""
        if self._buscar(bloque, (P.RomperContext,), (P.MientrasContext, P.ParaContext, P.FuncionContext)):
            return True
        return self.en_funcion > 0 and self._buscar(bloque, (P.RetornoContext,), (P.FuncionContext,))

    @staticmethod
    def _nombres_usados(ctx, acumulado):
        if isinstance(ctx, P.IdentificadorContext):
            acumulado.add(ctx.ID().getText())
        for i in range(ctx.getChildCount()):
            h = ctx.getChild(i)
            if not isinstance(h, TerminalNode):
                AnalizadorSemantico._nombres_usados(h, acumulado)
        return acumulado

    def _modificados(self, ctx, acumulado):
        """Nombres que el cuerpo de un ciclo puede cambiar. Devuelve None si
        no se puede saber (llama a una función del usuario, que podría
        cambiar cualquier variable)."""
        if isinstance(ctx, (P.AsignacionContext, P.ParaContext)):
            acumulado.add(ctx.ID().getText())
        if isinstance(ctx, P.PostfijoContext):
            hijos = [ctx.getChild(i) for i in range(1, ctx.getChildCount())]
            if any(isinstance(h, P.LlamadaContext) for h in hijos):
                prim = ctx.primario()
                nombre = prim.ID().getText() if isinstance(prim, P.IdentificadorContext) else None
                if nombre not in NATIVAS:
                    return None
                if nombre in ("agregar", "quitar") and hijos[0].argumentos():
                    acumulado |= self._nombres_usados(hijos[0].argumentos().expresion(0), set())
        for i in range(ctx.getChildCount()):
            h = ctx.getChild(i)
            if not isinstance(h, TerminalNode) and self._modificados(h, acumulado) is None:
                return None
        return acumulado

    def revisar_cuerpo_ciclo(self, bloque):
        self.en_ciclo += 1
        self.visit(bloque)
        self.en_ciclo -= 1

    def sugerencia(self, nombre):
        parecido = difflib.get_close_matches(nombre, _todos_los_nombres(self.actual), n=1, cutoff=0.75)
        if parecido:
            return f" (¿quisiste decir '{parecido[0]}'?)"
        clave = difflib.get_close_matches(nombre.lower(), sorted(PALABRAS_RESERVADAS), n=1, cutoff=0.75)
        if clave:
            return f" (¿quisiste escribir la palabra clave '{clave[0]}'?)"
        return ""

    def declarar(self, nodo_id, clase, minimo=None, maximo=None):
        nombre = nodo_id.getText()
        if nombre in NATIVAS:
            self.error(nodo_id, f"'{nombre}' es una función predefinida del lenguaje; usa otro nombre")
            return
        previo = self.actual.simbolos.get(nombre)
        if previo is not None:
            if previo.clase == "funcion":
                self.error(nodo_id, f"ya existe una función llamada '{nombre}' en este ámbito")
            else:
                self.error(nodo_id, f"'{nombre}' ya fue declarada en este ámbito")
            return
        self.actual.simbolos[nombre] = Simbolo(nombre, clase, minimo, maximo)

    def revisar_bloque(self, sentencias):
        """Revisa una secuencia de sentencias y luego las funciones pendientes."""
        pendientes_previos = self.pendientes
        self.pendientes = []
        # Las funciones se declaran primero ("elevación"): se pueden llamar
        # desde cualquier punto de su bloque, aunque estén escritas después.
        for s in sentencias:
            if s.funcion():
                self.visit(s.funcion())
        for s in sentencias:
            if not s.funcion():
                self.visit(s)
        pendientes, self.pendientes = self.pendientes, pendientes_previos
        for ctx, ambito in pendientes:
            self.revisar_funcion(ctx, ambito)

    def revisar_funcion(self, ctx, ambito_externo):
        anterior = self.actual
        self.actual = Ambito(ambito_externo, f"función {ctx.ID().getText()}")
        if ctx.parametros():
            for p in ctx.parametros().ID():
                if p.getText() in self.actual.simbolos:
                    self.error(p, f"el parámetro '{p.getText()}' está repetido")
                else:
                    self.declarar(p, "parametro")
        self.en_funcion += 1
        ciclos, self.en_ciclo = self.en_ciclo, 0   # 'romper' no cruza una función
        self.revisar_bloque(ctx.bloque().sentencia())
        self.en_ciclo = ciclos
        self.en_funcion -= 1
        self.actual = anterior

    # -- sentencias ---------------------------------------------------

    def visitPrograma(self, ctx):
        self.revisar_bloque(ctx.sentencia())
        return self.errores

    def visitBloque(self, ctx):
        # Cada bloque de si/mientras/para crea un ámbito nuevo.
        anterior = self.actual
        self.actual = Ambito(anterior, "bloque")
        self.revisar_bloque(ctx.sentencia())
        self.actual = anterior

    def visitDeclaracion(self, ctx):
        if ctx.expresion():
            self.visit(ctx.expresion())
        self.declarar(ctx.ID(), "variable")

    def visitAsignacion(self, ctx):
        nombre = ctx.ID().getText()
        simbolo = self.actual.buscar(nombre)
        if simbolo is None:
            pista = self.sugerencia(nombre) or f" (declárala con: variable {nombre} = ...)"
            self.error(ctx.ID(), f"la variable '{nombre}' no ha sido declarada{pista}")
        elif simbolo.clase in ("funcion", "nativa") and not ctx.indice():
            self.error(ctx.ID(), f"'{nombre}' es una función; no se le puede asignar un valor")
        for i in ctx.indice():
            self.visit(i)
        self.visit(ctx.expresion())

    def visitCondicional(self, ctx):
        for cond in ctx.expresion():
            self.visit(cond)
            self.condicion_constante(cond, "si")
        for b in ctx.bloque():
            self.visit(b)

    def visitMientras(self, ctx):
        cond = ctx.expresion()
        self.visit(cond)
        valor = self.condicion_constante(cond, "mientras")
        if valor is True and not self.tiene_salida(ctx.bloque()):
            self.error(ctx, "ciclo infinito: la condición del 'mientras' siempre es verdadera "
                            "y el ciclo no tiene 'romper' ni 'retornar' para salir")
        elif valor is False:
            self.advertir(ctx, "la condición del 'mientras' siempre es falsa: el ciclo nunca se ejecuta")
        elif valor is None and not self._buscar(cond, (P.LlamadaContext,)) \
                and not self.tiene_salida(ctx.bloque()):
            usados = self._nombres_usados(cond, set())
            cambiados = self._modificados(ctx.bloque(), set())
            if usados and cambiados is not None and not (usados & cambiados):
                nombres = ", ".join(f"'{n}'" for n in sorted(usados))
                self.advertir(ctx, f"posible ciclo infinito: ninguna variable de la condición "
                                   f"({nombres}) cambia dentro del ciclo")
        self.revisar_cuerpo_ciclo(ctx.bloque())

    def visitRomper(self, ctx):
        if self.en_ciclo == 0:
            self.error(ctx, "'romper' solo puede usarse dentro de un ciclo (mientras o para)")

    def visitContinuar(self, ctx):
        if self.en_ciclo == 0:
            self.error(ctx, "'continuar' solo puede usarse dentro de un ciclo (mientras o para)")

    def visitProducto(self, ctx):
        # x / 0 y x % 0 con un divisor constante se detectan sin ejecutar,
        # aunque el dividendo dependa de variables.
        for op, factor in zip(ctx.opProd(), ctx.unario()[1:]):
            if op.getText() in "/%":
                ok, valor = self.constante(factor)
                if ok and not isinstance(valor, bool) and isinstance(valor, (int, float)) and valor == 0:
                    texto = "división por cero" if op.getText() == "/" else "módulo por cero"
                    self.error(op, f"{texto} (detectado antes de ejecutar)")
        return self.visitChildren(ctx)

    def visitPara(self, ctx):
        for parte, e in zip(("desde", "hasta", "paso"), ctx.expresion()):
            self.visit(e)
            ok, valor = self.constante(e)
            if ok and (isinstance(valor, bool) or not isinstance(valor, (int, float))):
                self.error(e, f"el valor de '{parte}' debe ser un número, pero es {representar(valor)}")
            elif ok and parte == "paso" and valor == 0:
                self.error(e, "ciclo infinito: el 'paso' no puede ser 0")
        # Si la variable del ciclo no existe, se crea solo para el ciclo.
        nombre = ctx.ID().getText()
        anterior = self.actual
        self.actual = Ambito(anterior, "para")
        simbolo = anterior.buscar(nombre)
        if simbolo is None:
            self.declarar(ctx.ID(), "variable")
        elif simbolo.clase in ("funcion", "nativa"):
            self.error(ctx.ID(), f"'{nombre}' es una función; no puede ser la variable del ciclo")
        self.revisar_cuerpo_ciclo(ctx.bloque())
        self.actual = anterior

    def visitFuncion(self, ctx):
        n = len(ctx.parametros().ID()) if ctx.parametros() else 0
        self.declarar(ctx.ID(), "funcion", n, n)
        self.pendientes.append((ctx, self.actual))

    def visitRetorno(self, ctx):
        if self.en_funcion == 0:
            self.error(ctx, "'retornar' solo puede usarse dentro de una función")
        self.visit(ctx.expresion())

    # -- expresiones --------------------------------------------------

    def visitIdentificador(self, ctx):
        nombre = ctx.ID().getText()
        if self.actual.buscar(nombre) is None:
            self.error(ctx, f"'{nombre}' no ha sido declarado{self.sugerencia(nombre)}")

    def visitPostfijo(self, ctx):
        self.visit(ctx.primario())
        hijos = [ctx.getChild(i) for i in range(1, ctx.getChildCount())]
        primario = ctx.primario()
        if hijos and isinstance(primario, LlanoParser.IdentificadorContext) \
                and isinstance(hijos[0], LlanoParser.LlamadaContext):
            simbolo = self.actual.buscar(primario.ID().getText())
            if simbolo is not None and simbolo.clase in ("funcion", "nativa"):
                self.revisar_aridad(simbolo, hijos[0])
            elif simbolo is not None and simbolo.clase == "variable":
                pass  # puede guardar una función: se revisa al ejecutar
        for h in hijos:
            self.visit(h)

    def revisar_aridad(self, simbolo, llamada):
        n = len(llamada.argumentos().expresion()) if llamada.argumentos() else 0
        mi, ma = simbolo.minimo, simbolo.maximo
        if n < mi or (ma is not None and n > ma):
            if mi == ma:
                esperado = f"{mi} argumento{'s' if mi != 1 else ''}"
            elif ma is None:
                esperado = f"al menos {mi} argumento{'s' if mi != 1 else ''}"
            else:
                esperado = f"entre {mi} y {ma} argumentos"
            self.error(llamada, f"'{simbolo.nombre}' recibe {esperado}, pero se le pasaron {n}")


def analizar_semantica(arbol, nombres_previos=None, advertencias=None):
    """Lanza ErroresLlano si encuentra errores; si no, devuelve los símbolos
    globales. Si se pasa una lista en 'advertencias', se le agregan."""
    analizador = AnalizadorSemantico(nombres_previos)
    analizador.visit(arbol)
    if advertencias is not None:
        advertencias.extend(sorted(analizador.advertencias, key=lambda e: (e.linea, e.columna)))
    if analizador.errores:
        errores = sorted(analizador.errores, key=lambda e: (e.linea, e.columna))
        raise ErroresLlano(errores)
    return analizador.global_.simbolos
