"""Fases de análisis: léxica (tokens) y sintáctica (árbol de derivación).

El analizador léxico y el sintáctico los genera ANTLR a partir de
gramatica/Llano.g4. Este módulo los conecta, cambia los mensajes de
error por mensajes en español y ofrece utilidades para mostrar los
tokens y el árbol (opciones --tokens y --arbol).
"""

from antlr4 import CommonTokenStream, InputStream, Token
from antlr4.tree.Tree import TerminalNode

import difflib

from .errores import PALABRAS_RESERVADAS, PISTAS_CARACTERES, ErrorLlano, ErroresLlano, RecolectorErrores
from .generado.LlanoLexer import LlanoLexer
from .generado.LlanoParser import LlanoParser

MAX_ERRORES = 5


class ResultadoAnalisis:
    def __init__(self, fuente, tokens, arbol, parser):
        self.fuente = fuente
        self.tokens = tokens
        self.arbol = arbol
        self.parser = parser


def analizar_lexico(fuente):
    """Devuelve la lista de tokens (sin EOF) o lanza ErroresLlano."""
    lexer = LlanoLexer(InputStream(fuente))
    recolector = RecolectorErrores("lexico")
    lexer.removeErrorListeners()
    lexer.addErrorListener(recolector)
    flujo = CommonTokenStream(lexer)
    flujo.fill()

    errores = list(recolector.errores)
    anterior = None
    for tok in flujo.tokens:
        if tok.type == LlanoLexer.DESCONOCIDO:
            repetido = (anterior is not None and anterior.text == tok.text
                        and anterior.line == tok.line)
            anterior = tok
            if repetido:            # '&&', 'hola': un solo error por carácter y línea
                continue
            if tok.text == '"':
                mensaje = "texto sin cerrar: falta la comilla \" de cierre en esta línea"
            else:
                mensaje = f"el carácter {tok.text!r} no pertenece al alfabeto del lenguaje"
                if tok.text in PISTAS_CARACTERES:
                    mensaje += f" ({PISTAS_CARACTERES[tok.text]})"
            errores.append(ErrorLlano("lexico", mensaje, tok.line, tok.column))
    if errores:
        raise ErroresLlano(errores[:MAX_ERRORES])
    return flujo


def analizar(fuente):
    """Análisis léxico + sintáctico. Devuelve un ResultadoAnalisis."""
    flujo = analizar_lexico(fuente)
    flujo.seek(0)
    parser = LlanoParser(flujo)
    recolector = RecolectorErrores("sintactico")
    parser.removeErrorListeners()
    parser.addErrorListener(recolector)
    arbol = parser.programa()
    if recolector.errores:
        # Solo el primer error de sintaxis: los siguientes suelen ser
        # consecuencia de la recuperación automática de ANTLR y confunden.
        errores = recolector.errores[:1]
        pista = pista_contextual(flujo.tokens, errores[0].token)
        if pista:
            errores[0].mensaje += f" ({pista})"
        if errores[0].al_final:
            abierto = bloque_sin_cerrar(flujo.tokens)
            if abierto is not None:
                errores[0] = ErrorLlano(
                    "sintactico",
                    f"falta el 'fin' que cierra este '{abierto.text}'",
                    abierto.line, abierto.column)
                errores[0].al_final = True
        raise ErroresLlano(errores)
    tokens = [t for t in flujo.tokens if t.type != Token.EOF]
    return ResultadoAnalisis(fuente, tokens, arbol, parser)


CLAVES = sorted(PALABRAS_RESERVADAS)


def pista_contextual(tokens, tok):
    """Pista según los tokens alrededor de un error de sintaxis."""
    if tok is None:
        return None
    visibles = [t for t in tokens if t.channel == 0]
    try:
        i = next(k for k, t in enumerate(visibles) if t.tokenIndex == tok.tokenIndex)
    except StopIteration:
        return None
    previo = visibles[i - 1] if i > 0 else None
    if previo is not None and previo.type == LlanoLexer.RETORNAR:
        return ("después de 'retornar' va el valor que devuelve la función; "
                "si no devuelve nada, escribe: retornar nulo")
    if tok.type == LlanoLexer.ASIG:
        return "para comparar dos valores se usa '=='"
    if tok.type == LlanoLexer.POR and previo is not None and previo.type == LlanoLexer.POR:
        return "para la potencia se usa '^'"
    # ¿La línea empieza con una palabra clave mal escrita? (mientra, Si, Para, retorna…)
    linea = [t for t in visibles if t.line == tok.line]
    for t in linea[:1] + ([previo] if previo is not None else []):
        if t.type != LlanoLexer.ID:
            continue
        if t.text.lower() in PALABRAS_RESERVADAS:
            return f"las palabras clave van en minúscula: escribe '{t.text.lower()}'"
        parecida = difflib.get_close_matches(t.text, CLAVES, n=1, cutoff=0.75)
        if parecida:
            return f"¿quisiste escribir '{parecida[0]}' en lugar de '{t.text}'?"
    return None


APERTURAS = {LlanoLexer.SI, LlanoLexer.MIENTRAS, LlanoLexer.PARA, LlanoLexer.FUNCION}


def bloque_sin_cerrar(tokens):
    """Busca el bloque que quedó abierto usando una pila, como un autómata
    de pila que empareja cada 'si', 'mientras', 'para' o 'funcion' con su
    'fin'. En 'sino si' el 'si' no abre un bloque nuevo."""
    pila = []
    anterior = None
    for t in tokens:
        if t.type in APERTURAS and not (t.type == LlanoLexer.SI and anterior == LlanoLexer.SINO):
            pila.append(t)
        elif t.type == LlanoLexer.FIN and pila:
            pila.pop()
        anterior = t.type
    return pila[-1] if pila else None


# ---------------------------------------------------------------------
#  Presentación de tokens y árboles
# ---------------------------------------------------------------------

def nombre_tipo_token(tipo):
    nombres = LlanoLexer.symbolicNames
    return nombres[tipo] if 0 <= tipo < len(nombres) else str(tipo)


def tabla_tokens(fuente):
    """Tabla de texto con línea:columna, tipo y lexema de cada token."""
    flujo = analizar_lexico(fuente)
    filas = [("POSICIÓN", "TOKEN", "LEXEMA")]
    for t in flujo.tokens:
        if t.type == Token.EOF:
            continue
        filas.append((f"{t.line}:{t.column + 1}", nombre_tipo_token(t.type), t.text))
    ancho0 = max(len(f[0]) for f in filas)
    ancho1 = max(len(f[1]) for f in filas)
    lineas = [f"{a:<{ancho0}}  {b:<{ancho1}}  {c}" for a, b, c in filas]
    lineas.insert(1, "-" * (ancho0 + ancho1 + 12))
    lineas.append(f"\nTotal: {len(filas) - 1} tokens")
    return "\n".join(lineas)


def _etiqueta(nodo, parser, compacto):
    if isinstance(nodo, TerminalNode):
        tok = nodo.getSymbol()
        return f"{nombre_tipo_token(tok.type)} '{tok.text}'"
    regla = parser.ruleNames[nodo.getRuleIndex()]
    etiqueta = type(nodo).__name__[:-len("Context")].lower()
    return regla if etiqueta == regla else f"{regla} ({etiqueta})"   # alternativa etiquetada


def _hijos(nodo, compacto):
    """Hijos de un nodo. En modo compacto se saltan las cadenas de reglas
    con un solo hijo (por ejemplo disyuncion -> conjuncion -> ... -> primario),
    que solo existen para codificar la precedencia."""
    hijos = [nodo.getChild(i) for i in range(nodo.getChildCount())]
    if not compacto:
        return hijos
    resultado = []
    for h in hijos:
        while (not isinstance(h, TerminalNode) and h.getChildCount() == 1
               and not isinstance(h.getChild(0), TerminalNode)):
            h = h.getChild(0)
        resultado.append(h)
    return resultado


def arbol_texto(resultado, compacto=True):
    """Árbol de derivación con sangría, al estilo del comando tree."""
    parser = resultado.parser
    lineas = []

    def recorrer(nodo, prefijo, ultimo, raiz=False):
        if raiz:
            lineas.append(_etiqueta(nodo, parser, compacto))
            nuevo = ""
        else:
            lineas.append(prefijo + ("└── " if ultimo else "├── ") + _etiqueta(nodo, parser, compacto))
            nuevo = prefijo + ("    " if ultimo else "│   ")
        if isinstance(nodo, TerminalNode):
            return
        hijos = [h for h in _hijos(nodo, compacto)
                 if not (isinstance(h, TerminalNode) and h.getSymbol().type == Token.EOF)]
        for i, h in enumerate(hijos):
            recorrer(h, nuevo, i == len(hijos) - 1)

    raiz = resultado.arbol
    while compacto and raiz.getChildCount() == 1 and not isinstance(raiz.getChild(0), TerminalNode):
        raiz = raiz.getChild(0)
    recorrer(raiz, "", True, raiz=True)
    return "\n".join(lineas)


def arbol_dot(resultado, compacto=True):
    """Árbol en formato DOT de Graphviz (se puede ver en https://dreampuf.github.io/GraphvizOnline)."""
    parser = resultado.parser
    lineas = ["digraph arbol {", '  node [fontname="Helvetica", fontsize=11];']
    contador = [0]

    def recorrer(nodo):
        ident = f"n{contador[0]}"
        contador[0] += 1
        etiqueta = _etiqueta(nodo, parser, compacto).replace("\\", "\\\\").replace('"', '\\"')
        forma = "box, style=rounded" if not isinstance(nodo, TerminalNode) else "plaintext"
        lineas.append(f'  {ident} [label="{etiqueta}", shape={forma}];')
        if not isinstance(nodo, TerminalNode):
            for h in _hijos(nodo, compacto):
                if isinstance(h, TerminalNode) and h.getSymbol().type == Token.EOF:
                    continue
                lineas.append(f"  {ident} -> {recorrer(h)};")
        return ident

    recorrer(resultado.arbol)
    lineas.append("}")
    return "\n".join(lineas)
