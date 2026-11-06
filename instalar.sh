#!/usr/bin/env sh
# Instalación de Llano en Git Bash, Linux o macOS
set -e
PY=$(command -v python3 || command -v python)
"$PY" -c "import sys; sys.exit(0 if sys.version_info >= (3, 10) else 'Se necesita Python 3.10 o superior')"
"$PY" -m pip install -r requirements.txt
"$PY" -m unittest discover -s pruebas
echo "Listo. Prueba:  $PY llano.py ejemplos/01_hola.llano"
