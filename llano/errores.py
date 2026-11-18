import re

from antlr4.error.ErrorListener import ErrorListener

FASES = {
    "lexico": "Error léxico",
    "sintactico": "Error de sintaxis",
    "semantico": "Error semántico",
    "ejecucion": "Error de ejecución",
    "advertencia": "Advertencia",
}


class ErrorLlano(Exception):
    def __init__(self, fase, mensaje, linea=None, columna=None):
        super().__init__(mensaje)
        self.fase = fase
        self.mensaje = mensaje
        self.linea = linea
        self.columna = columna
        self.al_final = False   # error al final del texto
        self.token = None

    def formatear(self, fuente=None):
        titulo = FASES.get(self.fase, "Error")
        if self.linea is None:
            return f"{titulo}: {self.mensaje}"
        texto = f"{titulo} en la línea {self.linea}, columna {self.columna + 1}: {self.mensaje}"
        if fuente is not None:
            lineas = fuente.splitlines()
            if 1 <= self.linea <= len(lineas):
                codigo = lineas[self.linea - 1].expandtabs(4)
                prefijo = lineas[self.linea - 1][: self.columna].expandtabs(4)
                texto += f"\n    {codigo}\n    {' ' * len(prefijo)}^"
        return texto

    def __str__(self):
        return self.formatear()


class ErroresLlano(Exception):
    def __init__(self, errores):
        super().__init__(f"{len(errores)} error(es)")
        self.errores = list(errores)

    def formatear(self, fuente=None):
        return "\n\n".join(e.formatear(fuente) for e in self.errores)

    def __str__(self):
        return self.formatear()


def mensaje_de_excepcion(e):
    if isinstance(e, RecursionError):
        return "demasiadas llamadas anidadas (¿una recursión sin caso base?)"
    if isinstance(e, MemoryError):
        return ("el programa se quedó sin memoria "
                "(¿una lista o un texto que crece sin fin?)")
    if isinstance(e, ZeroDivisionError):
        return "división por cero"
    if isinstance(e, OverflowError):
        return "el número es demasiado grande para calcularse (desbordamiento)"
    if isinstance(e, ArithmeticError):
        return "operación matemática no válida"
    if isinstance(e, (IndexError, KeyError)):
        return "se intentó usar una posición o un elemento que no existe"
    if isinstance(e, TypeError):
        return "los tipos de los valores no son compatibles con esta operación"
    if isinstance(e, ValueError):
        return "valor no válido para esta operación"
    if isinstance(e, (UnicodeError, OSError)):
        return "no se pudo leer o escribir un dato (entrada/salida)"
    return "ocurrió un error interno al ejecutar esta instrucción"


PALABRAS_RESERVADAS = {
    "variable", "si", "entonces", "sino", "fin", "mientras", "hacer", "para",
    "desde", "hasta", "paso", "funcion", "función", "retornar", "verdadero",
    "falso", "nulo", "y", "o", "no", "romper", "continuar",
}

NOMBRES_TOKENS = {
    "ID": "un nombre",
    "NUMERO": "un número",
    "TEXTO": "un texto",
    "<EOF>": "el final del programa",
    "EOF": "el final del programa",
}


def _nombre_token(nombre):
    nombre = nombre.strip()
    if nombre in NOMBRES_TOKENS:
        return NOMBRES_TOKENS[nombre]
    return nombre


def _lista_esperada(texto):
    texto = texto.strip()
    if texto.startswith("{") and texto.endswith("}"):
        opciones = [_nombre_token(t) for t in texto[1:-1].split(",")]
    else:
        opciones = [_nombre_token(texto)]
    opciones = list(dict.fromkeys(opciones))
    if len(opciones) > 6:
        return None
    if len(opciones) == 1:
        return opciones[0]
    return ", ".join(opciones[:-1]) + " o " + opciones[-1]


def _encontrado(texto):
    if texto == "<EOF>":
        return "el final del programa"
    return f"'{texto}'"


def traducir_mensaje_sintactico(msg, simbolo=None):
    m = re.match(r"mismatched input '(.*)' expecting (.*)", msg, re.S)
    if m:
        encontrado, esperado = m.group(1), _lista_esperada(m.group(2))
        texto = f"no se esperaba {_encontrado(encontrado)}"
        if esperado:
            texto += f"; se esperaba {esperado}"
        return texto + _pista(encontrado, esperado)
    m = re.match(r"extraneous input '(.*)' expecting (.*)", msg, re.S)
    if m:
        encontrado, esperado = m.group(1), _lista_esperada(m.group(2))
        texto = f"sobra {_encontrado(encontrado)}"
        if esperado:
            texto += f"; se esperaba {esperado}"
        elif encontrado == "fin":
            texto += " (¿hay un 'fin' de más?)"
        return texto + _pista(encontrado, esperado)
    m = re.match(r"missing (.*) at '(.*)'", msg, re.S)
    if m:
        antes = _encontrado(m.group(2))
        antes = "del " + antes[3:] if antes.startswith("el ") else "de " + antes
        return f"falta {_nombre_token(m.group(1))} antes {antes}"
    m = re.match(r"no viable alternative at input '(.*)'", msg, re.S)
    if m:
        entrada = m.group(1)
        ultimo = simbolo.text if simbolo is not None else entrada.split()[-1:] or entrada
        return f"no se reconoce la instrucción cerca de {_encontrado(ultimo)}"
    return msg


def _pista(token, esperado=None):
    if token in PALABRAS_RESERVADAS and esperado and "un nombre" in esperado:
        return (f" (recuerda que '{token}' es una palabra reservada y no "
                f"puede usarse como nombre de variable)")
    if token == "<EOF>":
        return " (¿falta un 'fin' para cerrar un bloque?)"
    return ""


PISTAS_CARACTERES = {
    "&": "para el 'y' lógico se escribe la palabra y",
    "|": "para el 'o' lógico se escribe la palabra o",
    "!": "para negar se escribe la palabra no; para 'diferente' se usa !=",
    ";": "Llano no usa ';' para terminar las instrucciones",
    "{": "los bloques empiezan con 'entonces' o 'hacer' y terminan con 'fin'",
    "}": "los bloques empiezan con 'entonces' o 'hacer' y terminan con 'fin'",
    ":": "Llano no usa ':'; los bloques empiezan con 'entonces' o 'hacer'",
    "'": 'los textos se escriben entre comillas dobles: "hola"',
}


class RecolectorErrores(ErrorListener):
    def __init__(self, fase):
        super().__init__()
        self.fase = fase
        self.errores = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        if self.fase == "lexico":
            m = re.match(r"token recognition error at: '(.*)'", msg, re.S)
            caracter = m.group(1) if m else msg
            mensaje = f"el carácter {caracter!r} no pertenece al alfabeto del lenguaje"
        else:
            mensaje = traducir_mensaje_sintactico(msg, offendingSymbol)
        error = ErrorLlano(self.fase, mensaje, line, column)
        error.al_final = offendingSymbol is not None and offendingSymbol.type == -1  # EOF
        error.token = offendingSymbol
        self.errores.append(error)
