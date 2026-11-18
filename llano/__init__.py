import sys
import threading

from .analisis import analizar
from .errores import ErrorLlano, ErroresLlano
from .interprete import MAX_ITERACIONES, Interprete
from .semantico import analizar_semantica

__version__ = "0.3.0"

# enteros sin límite de dígitos
if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)
__all__ = ["ejecutar", "verificar", "ErrorLlano", "ErroresLlano", "Interprete", "MAX_ITERACIONES"]


def verificar(fuente, advertencias=None):
    resultado = analizar(fuente)
    analizar_semantica(resultado.arbol, advertencias=advertencias)
    return resultado


def ejecutar(fuente, salida=print, entrada=input, interprete=None,
             max_iteraciones=MAX_ITERACIONES, advertencias=None):
    resultado = verificar(fuente, advertencias)
    interprete = interprete or Interprete(salida, entrada, max_iteraciones)
    return con_pila_grande(lambda: interprete.visit(resultado.arbol), interprete.cancelar)


def con_pila_grande(funcion, al_interrumpir=None):
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
        for megas in (512, 128, 32, 0):
            try:
                threading.stack_size(megas * 1024 * 1024)
                hilo = threading.Thread(target=correr, daemon=True)
                hilo.start()
                break
            except (ValueError, RuntimeError, MemoryError):
                hilo = None
        if hilo is None:
            try:
                return funcion()
            finally:
                sys.setrecursionlimit(limite_anterior)
    finally:
        threading.stack_size(tam_anterior)
    try:
        try:
            while hilo.is_alive():
                hilo.join(0.1)
        except KeyboardInterrupt:
            if al_interrumpir is not None:
                al_interrumpir()
                hilo.join(2)
            raise
    finally:
        sys.setrecursionlimit(limite_anterior)
    if excepcion[0] is not None:
        raise excepcion[0]
    return resultado[0]
