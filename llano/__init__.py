"""Llano: un lenguaje de programación sencillo en español.

Uso como librería:

    from llano import ejecutar
    ejecutar('imprimir("hola")')

Fases: análisis léxico -> análisis sintáctico -> análisis semántico -> ejecución.
"""

import sys
import threading

from .analisis import analizar
from .errores import ErrorLlano, ErroresLlano
from .interprete import Interprete
from .semantico import analizar_semantica

__version__ = "0.2.0"

# Python 3.11+ limita los enteros a 4300 dígitos al convertirlos en texto;
# Llano promete enteros sin límite (por ejemplo, 2000!), así que se quita.
if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)
__all__ = ["ejecutar", "verificar", "ErrorLlano", "ErroresLlano", "Interprete"]


def verificar(fuente):
    """Fases de análisis (léxica, sintáctica y semántica) sin ejecutar.
    Lanza ErroresLlano si el programa tiene errores."""
    resultado = analizar(fuente)
    analizar_semantica(resultado.arbol)
    return resultado


def ejecutar(fuente, salida=print, entrada=input, interprete=None):
    """Analiza y ejecuta un programa. Lanza ErroresLlano o ErrorLlano."""
    resultado = verificar(fuente)
    interprete = interprete or Interprete(salida, entrada)
    return con_pila_grande(lambda: interprete.visit(resultado.arbol))


def con_pila_grande(funcion):
    """Ejecuta 'funcion' en un hilo con una pila amplia, para que los
    programas recursivos no agoten la pila de Python."""
    resultado, excepcion = [None], [None]

    def correr():
        try:
            resultado[0] = funcion()
        except BaseException as e:  # se relanza en el hilo principal
            excepcion[0] = e

    limite_anterior = sys.getrecursionlimit()
    sys.setrecursionlimit(max(limite_anterior, 400_000))
    tam_anterior = threading.stack_size()
    hilo = None
    try:
        for megas in (512, 128, 32, 0):       # la pila más grande que permita el sistema
            try:
                threading.stack_size(megas * 1024 * 1024)
                hilo = threading.Thread(target=correr, daemon=True)
                hilo.start()
                break
            except (ValueError, RuntimeError, MemoryError):
                hilo = None
        if hilo is None:                      # sin hilos: se ejecuta directamente
            try:
                return funcion()
            finally:
                sys.setrecursionlimit(limite_anterior)
    finally:
        threading.stack_size(tam_anterior)
    try:
        while hilo.is_alive():
            hilo.join(0.1)
    finally:
        sys.setrecursionlimit(limite_anterior)
    if excepcion[0] is not None:
        raise excepcion[0]
    return resultado[0]
