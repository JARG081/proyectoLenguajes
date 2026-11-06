"""Análisis semántico: revisa el programa antes de ejecutarlo.

Recorre el árbol de derivación con una tabla de símbolos por ámbitos y
detecta, sin ejecutar nada:

  * usos de nombres que no han sido declarados,
  * declaraciones repetidas en el mismo ámbito y parámetros repetidos,
  * asignaciones a funciones,
  * 'retornar' fuera de una función,
  * llamadas con una cantidad incorrecta de argumentos (cuando la
    función se conoce en el análisis).

Las funciones se declaran al inicio de su bloque y sus cuerpos se revisan
al final, así una función puede usarse antes de la línea donde está escrita
y puede llamar a otra declarada después.
"""

import difflib

from .errores import PALABRAS_RESERVADAS, ErrorLlano, ErroresLlano
from .generado.LlanoParser import LlanoParser
from .generado.LlanoVisitor import LlanoVisitor
from .valores import NATIVAS


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
        self.pendientes = []

    # -- utilidades ---------------------------------------------------

    def error(self, token_o_ctx, mensaje):
        if hasattr(token_o_ctx, "getSymbol"):      # nodo terminal
            tok = token_o_ctx.getSymbol()
        else:                                      # nodo de regla
            tok = token_o_ctx.start
        self.errores.append(ErrorLlano("semantico", mensaje, tok.line, tok.column))

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
        self.revisar_bloque(ctx.bloque().sentencia())
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

    def visitPara(self, ctx):
        for e in ctx.expresion():
            self.visit(e)
        # Si la variable del ciclo no existe, se crea solo para el ciclo.
        nombre = ctx.ID().getText()
        anterior = self.actual
        self.actual = Ambito(anterior, "para")
        simbolo = anterior.buscar(nombre)
        if simbolo is None:
            self.declarar(ctx.ID(), "variable")
        elif simbolo.clase in ("funcion", "nativa"):
            self.error(ctx.ID(), f"'{nombre}' es una función; no puede ser la variable del ciclo")
        self.visit(ctx.bloque())
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


def analizar_semantica(arbol, nombres_previos=None):
    """Lanza ErroresLlano si encuentra errores; si no, devuelve los símbolos globales."""
    analizador = AnalizadorSemantico(nombres_previos)
    analizador.visit(arbol)
    if analizador.errores:
        errores = sorted(analizador.errores, key=lambda e: (e.linea, e.columna))
        raise ErroresLlano(errores)
    return analizador.global_.simbolos
