#!/usr/bin/env python3
"""Línea de comandos de Llano.

    python llano.py programa.llano            ejecuta un programa
    python llano.py programa.llano --tokens   muestra los tokens (análisis léxico)
    python llano.py programa.llano --arbol    muestra el árbol de derivación
    python llano.py programa.llano --dot      árbol en formato Graphviz DOT
    python llano.py programa.llano --verificar  solo analiza, no ejecuta
    python llano.py -e 'imprimir(2 + 3)'      ejecuta código escrito en la línea
    python llano.py                           modo interactivo
    python llano.py --funciones               lista las funciones predefinidas
"""

import argparse
import sys

from llano import ErrorLlano, ErroresLlano, Interprete, __version__, con_pila_grande
from llano.analisis import analizar, arbol_dot, arbol_texto, tabla_tokens
from llano.semantico import analizar_semantica
from llano.valores import crear_nativas, representar


def _configurar_consola():
    for flujo in (sys.stdout, sys.stderr):
        try:
            flujo.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass


def _leer_archivo(ruta):
    try:
        with open(ruta, encoding="utf-8-sig") as f:
            return f.read()
    except FileNotFoundError:
        sys.exit(f"No se encontró el archivo '{ruta}'.")
    except UnicodeDecodeError:
        sys.exit(f"El archivo '{ruta}' no está guardado en UTF-8.")


def _mostrar_error(error, fuente):
    print(error.formatear(fuente), file=sys.stderr)


def _ejecutar_fuente(fuente, args):
    try:
        if args.tokens:
            print(tabla_tokens(fuente))
            return 0
        resultado = analizar(fuente)
        if args.arbol or args.arbol_completo:
            print(arbol_texto(resultado, compacto=not args.arbol_completo))
            return 0
        if args.dot:
            print(arbol_dot(resultado, compacto=not args.arbol_completo))
            return 0
        analizar_semantica(resultado.arbol)
        if args.verificar:
            print("El programa no tiene errores léxicos, sintácticos ni semánticos.")
            return 0
        interprete = Interprete()
        con_pila_grande(lambda: interprete.visit(resultado.arbol))
        return 0
    except (ErrorLlano, ErroresLlano) as e:
        sys.stdout.flush()
        _mostrar_error(e, fuente)
        return 1
    except KeyboardInterrupt:
        print("\nEjecución interrumpida.", file=sys.stderr)
        return 130
    except BrokenPipeError:
        return 0
    except RecursionError:
        print("Error de ejecución: el programa anidó demasiadas llamadas.", file=sys.stderr)
        return 1
    except MemoryError:
        print("Error de ejecución: el programa se quedó sin memoria.", file=sys.stderr)
        return 1
    except Exception as e:  # nunca mostrar una traza de Python al usuario
        print(f"Error interno de Llano ({type(e).__name__}: {e}). "
              "Por favor, reporta el programa que lo produjo.", file=sys.stderr)
        return 2


def _interactivo():
    print(f"Llano {__version__} - modo interactivo. Escribe 'salir' para terminar.")
    print("Los bloques (si, mientras, para, funcion) continúan hasta su 'fin'.")
    interprete = Interprete()
    simbolos = {}
    while True:
        try:
            linea = input("llano> ")
        except (EOFError, KeyboardInterrupt):
            print()
            return 0
        if linea.strip() in ("salir", "salir()"):
            return 0
        fuente = linea
        while True:
            if not fuente.strip():
                break
            try:
                resultado = analizar(fuente)
                simbolos.update(analizar_semantica(resultado.arbol, simbolos))
                valor = con_pila_grande(lambda: interprete.visit(resultado.arbol))
                if valor is not None:
                    print(representar(valor))
                break
            except ErroresLlano as e:
                if all(getattr(x, "al_final", False) for x in e.errores):
                    try:                          # bloque incompleto: pedir más líneas
                        fuente += "\n" + input("  ... ")
                        continue
                    except (EOFError, KeyboardInterrupt):
                        print()
                        break
                _mostrar_error(e, fuente)
                break
            except ErrorLlano as e:
                _mostrar_error(e, fuente)
                break
            except KeyboardInterrupt:
                print("\nEjecución interrumpida.")
                break
            except (RecursionError, MemoryError) as e:
                print(f"Error de ejecución: {type(e).__name__}", file=sys.stderr)
                break
            except Exception as e:  # el modo interactivo nunca se cierra por un error
                print(f"Error interno de Llano ({type(e).__name__}: {e})", file=sys.stderr)
                break


def _listar_funciones():
    print("Funciones predefinidas de Llano:\n")
    for nombre, f in crear_nativas(print, input).items():
        print(f"  {nombre:<10} {f.descripcion}")
    return 0


def main(argv=None):
    _configurar_consola()
    p = argparse.ArgumentParser(
        prog="llano",
        description="Intérprete de Llano, un lenguaje de programación en español.")
    p.add_argument("archivo", nargs="?", help="programa .llano a ejecutar")
    p.add_argument("-e", "--codigo", help="ejecuta el código dado en lugar de un archivo")
    p.add_argument("--tokens", action="store_true", help="muestra los tokens (análisis léxico)")
    p.add_argument("--arbol", action="store_true", help="muestra el árbol de derivación compacto")
    p.add_argument("--arbol-completo", action="store_true",
                   help="muestra el árbol con todas las reglas de precedencia")
    p.add_argument("--dot", action="store_true", help="imprime el árbol en formato Graphviz DOT")
    p.add_argument("--verificar", action="store_true", help="solo analiza el programa, no lo ejecuta")
    p.add_argument("--funciones", action="store_true", help="lista las funciones predefinidas")
    p.add_argument("--version", action="version", version=f"Llano {__version__}")
    args = p.parse_args(argv)

    if args.funciones:
        return _listar_funciones()
    if args.codigo is not None:
        return _ejecutar_fuente(args.codigo, args)
    if args.archivo:
        return _ejecutar_fuente(_leer_archivo(args.archivo), args)
    return _interactivo()


if __name__ == "__main__":
    sys.exit(main())
