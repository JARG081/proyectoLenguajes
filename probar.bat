@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo === 1. Pruebas unitarias ===
python -m unittest discover -s pruebas
echo.
echo === 2. Casos de uso de punta a punta ===
python pruebas\casos_de_uso.py
echo.
echo El detalle quedo en casos_de_uso\RESULTADOS.md
pause
