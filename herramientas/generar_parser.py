"""Regenera el analizador léxico y sintáctico a partir de gramatica/Llano.g4.

Solo hace falta después de modificar la gramática. Requiere Java 11 o
superior. Uso, desde la carpeta del proyecto:

    python herramientas/generar_parser.py
"""

import os
import shutil
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JAR = os.path.join(RAIZ, "herramientas", "antlr-4.13.2-complete.jar")
GRAMATICA = os.path.join(RAIZ, "gramatica", "Llano.g4")
DESTINO = os.path.join(RAIZ, "llano", "generado")


def main():
    if not os.path.exists(JAR):
        sys.exit(f"No se encontró {JAR}.\nDescárgalo de https://www.antlr.org/download/antlr-4.13.2-complete.jar")
    if shutil.which("java") is None:
        sys.exit("No se encontró Java. Instala Java 11 o superior (por ejemplo, Eclipse Temurin).")
    comando = ["java", "-jar", JAR, "-Dlanguage=Python3", "-visitor", "-no-listener",
               "-Xexact-output-dir", "-o", DESTINO, GRAMATICA]
    print("Ejecutando:", " ".join(comando))
    resultado = subprocess.run(comando)
    if resultado.returncode != 0:
        sys.exit("ANTLR reportó errores en la gramática.")
    open(os.path.join(DESTINO, "__init__.py"), "a").close()
    print("Analizadores generados en llano/generado/")


if __name__ == "__main__":
    main()
