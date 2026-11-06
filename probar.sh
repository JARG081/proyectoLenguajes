#!/usr/bin/env sh
# Pruebas unitarias y casos de uso (Git Bash, Linux o macOS)
cd "$(dirname "$0")"
PY=$(command -v python3 || command -v python)
"$PY" -m unittest discover -s pruebas
"$PY" pruebas/casos_de_uso.py
