"""Valores de Llano, conversión a texto y funciones predefinidas.

Tipos del lenguaje y su representación en Python:

    número  -> int o float        texto  -> str
    lógico  -> bool               nulo   -> None
    lista   -> list               función -> Funcion o Nativa
"""

import math
import random
from decimal import ROUND_HALF_UP, Decimal


class Funcion:
    """Función definida por el usuario (guarda el entorno donde se creó)."""

    def __init__(self, nombre, parametros, cuerpo, cierre):
        self.nombre = nombre
        self.parametros = parametros
        self.cuerpo = cuerpo
        self.cierre = cierre

    @property
    def aridad(self):
        return len(self.parametros)

    def __repr__(self):
        return f"<función {self.nombre}>"


class Nativa:
    """Función predefinida del lenguaje, implementada en Python."""

    def __init__(self, nombre, implementacion, minimo, maximo, descripcion):
        self.nombre = nombre
        self.implementacion = implementacion
        self.minimo = minimo
        self.maximo = maximo          # None = sin límite
        self.descripcion = descripcion

    def __repr__(self):
        return f"<función {self.nombre}>"


class FalloNativo(Exception):
    """Lo lanza una función predefinida; el intérprete le agrega la posición."""


# ---------------------------------------------------------------------
#  Tipos
# ---------------------------------------------------------------------

def es_numero(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool)


def es_entero(v):
    return (isinstance(v, int) and not isinstance(v, bool)) or (
        isinstance(v, float) and v.is_integer())


def nombre_tipo(v):
    if v is None:
        return "nulo"
    if isinstance(v, bool):
        return "lógico"
    if es_numero(v):
        return "número"
    if isinstance(v, str):
        return "texto"
    if isinstance(v, list):
        return "lista"
    if isinstance(v, (Funcion, Nativa)):
        return "función"
    return type(v).__name__


def normalizar(n):
    """Deja los números enteros como int (2.0 -> 2) para mostrarlos limpios."""
    if isinstance(n, float) and n.is_integer() and abs(n) < 2 ** 53:
        return int(n)
    return n


# ---------------------------------------------------------------------
#  Conversión a texto
# ---------------------------------------------------------------------

def a_texto(v):
    """Texto que muestra imprimir()."""
    if isinstance(v, str):
        return v
    return representar(v)


def representar(v):
    """Representación de un valor dentro de una lista o en el modo interactivo."""
    if v is None:
        return "nulo"
    if isinstance(v, bool):
        return "verdadero" if v else "falso"
    if isinstance(v, int):
        return str(v)
    if isinstance(v, float):
        if math.isinf(v):
            return "infinito" if v > 0 else "-infinito"
        n = normalizar(v)
        return str(n) if isinstance(n, int) else format(n, ".12g")
    if isinstance(v, str):
        escapado = v.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n").replace("\t", "\\t")
        return f'"{escapado}"'
    if isinstance(v, list):
        return "[" + ", ".join(representar(x) for x in v) + "]"
    return repr(v)


def iguales(a, b):
    """Igualdad del lenguaje: valores de tipos distintos nunca son iguales."""
    if es_numero(a) and es_numero(b):
        return a == b
    if nombre_tipo(a) != nombre_tipo(b):
        return False
    if isinstance(a, list):
        return len(a) == len(b) and all(iguales(x, y) for x, y in zip(a, b))
    if isinstance(a, (Funcion, Nativa)):
        return a is b
    return a == b


# ---------------------------------------------------------------------
#  Funciones predefinidas
# ---------------------------------------------------------------------

def _requiere(cond, mensaje):
    if not cond:
        raise FalloNativo(mensaje)


def _numero(texto):
    _requiere(isinstance(texto, str) or es_numero(texto),
              f"numero() necesita un texto, pero recibió {nombre_tipo(texto)}")
    if es_numero(texto):
        return texto
    limpio = texto.strip()
    try:
        return int(limpio)
    except ValueError:
        pass
    try:
        valor = float(limpio)
    except ValueError:
        raise FalloNativo(f"el texto {representar(texto)} no es un número válido")
    _requiere(math.isfinite(valor), f"el texto {representar(texto)} no es un número válido")
    return normalizar(valor)


def _entero(x):
    _requiere(es_numero(x), f"entero() necesita un número, pero recibió {nombre_tipo(x)}")
    return int(x)


def _longitud(x):
    _requiere(isinstance(x, (str, list)),
              f"longitud() necesita un texto o una lista, pero recibió {nombre_tipo(x)}")
    return len(x)


def _agregar(lista, valor):
    _requiere(isinstance(lista, list),
              f"agregar() necesita una lista como primer argumento, pero recibió {nombre_tipo(lista)}")
    lista.append(valor)
    return None


def _quitar(lista, posicion=None):
    _requiere(isinstance(lista, list),
              f"quitar() necesita una lista, pero recibió {nombre_tipo(lista)}")
    _requiere(len(lista) > 0, "no se puede quitar un elemento de una lista vacía")
    if posicion is None:
        return lista.pop()
    _requiere(es_entero(posicion), "la posición debe ser un número entero")
    posicion = int(posicion)
    _requiere(0 <= posicion < len(lista),
              f"la posición {posicion} está fuera de la lista (0 a {len(lista) - 1})")
    return lista.pop(posicion)


def _invertir(x):
    _requiere(isinstance(x, (str, list)),
              f"invertir() necesita un texto o una lista, pero recibió {nombre_tipo(x)}")
    return x[::-1]


def _subcadena(texto, inicio, fin=None):
    _requiere(isinstance(texto, str),
              f"subcadena() necesita un texto, pero recibió {nombre_tipo(texto)}")
    fin = len(texto) if fin is None else fin
    _requiere(es_entero(inicio) and es_entero(fin), "las posiciones deben ser números enteros")
    inicio, fin = int(inicio), int(fin)
    _requiere(0 <= inicio <= fin <= len(texto),
              f"posiciones inválidas ({inicio}, {fin}) para un texto de longitud {len(texto)}")
    return texto[inicio:fin]


def _raiz(x):
    _requiere(es_numero(x), f"raiz() necesita un número, pero recibió {nombre_tipo(x)}")
    _requiere(x >= 0, "no existe la raíz cuadrada real de un número negativo")
    return normalizar(math.sqrt(x))


def _absoluto(x):
    _requiere(es_numero(x), f"absoluto() necesita un número, pero recibió {nombre_tipo(x)}")
    return abs(x)


def _redondear(x, decimales=0):
    _requiere(es_numero(x), f"redondear() necesita un número, pero recibió {nombre_tipo(x)}")
    _requiere(es_entero(decimales), "la cantidad de decimales debe ser un número entero")
    # Redondeo escolar: 2.5 -> 3 y -2.5 -> -3 (round() de Python daría 2)
    paso = Decimal(1).scaleb(-int(decimales))
    redondeado = Decimal(str(x)).quantize(paso, rounding=ROUND_HALF_UP)
    return normalizar(int(redondeado) if int(decimales) <= 0 else float(redondeado))


def _aleatorio(minimo, maximo):
    _requiere(es_entero(minimo) and es_entero(maximo), "aleatorio() necesita dos números enteros")
    _requiere(minimo <= maximo, "en aleatorio(a, b), a debe ser menor o igual que b")
    return random.randint(int(minimo), int(maximo))


def crear_nativas(salida, entrada):
    """Crea las funciones predefinidas usando las funciones de E/S dadas."""

    def _imprimir(*valores):
        salida(" ".join(a_texto(v) for v in valores))
        return None

    def _leer(mensaje=None):
        try:
            return entrada("" if mensaje is None else a_texto(mensaje))
        except EOFError:
            raise FalloNativo("leer() no recibió datos: la entrada terminó")

    tabla = [
        ("imprimir", _imprimir, 0, None, "Muestra los valores separados por un espacio."),
        ("leer", _leer, 0, 1, "Lee una línea del teclado y la devuelve como texto."),
        ("numero", _numero, 1, 1, "Convierte un texto en número."),
        ("texto", lambda v: a_texto(v), 1, 1, "Convierte cualquier valor en texto."),
        ("entero", _entero, 1, 1, "Parte entera de un número."),
        ("longitud", _longitud, 1, 1, "Longitud |w| de un texto o tamaño de una lista."),
        ("agregar", _agregar, 2, 2, "Agrega un valor al final de una lista."),
        ("quitar", _quitar, 1, 2, "Quita y devuelve un elemento de una lista."),
        ("invertir", _invertir, 1, 1, "Reflexión w⁻¹ de un texto o una lista."),
        ("subcadena", _subcadena, 2, 3, "Subcadena entre dos posiciones [inicio, fin)."),
        ("tipo", lambda v: nombre_tipo(v), 1, 1, "Nombre del tipo de un valor."),
        ("raiz", _raiz, 1, 1, "Raíz cuadrada."),
        ("absoluto", _absoluto, 1, 1, "Valor absoluto."),
        ("redondear", _redondear, 1, 2, "Redondea a cierta cantidad de decimales."),
        ("aleatorio", _aleatorio, 2, 2, "Entero al azar entre a y b (incluidos)."),
    ]
    return {nombre: Nativa(nombre, f, mi, ma, d) for nombre, f, mi, ma, d in tabla}


# Nombres y aridades, para el análisis semántico (no necesita E/S).
NATIVAS = {n.nombre: (n.minimo, n.maximo)
           for n in crear_nativas(lambda _: None, lambda _: "").values()}
