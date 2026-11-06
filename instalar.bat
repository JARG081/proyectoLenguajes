@echo off
chcp 65001 >nul
echo === Instalacion de Llano ===
where python >nul 2>nul
if errorlevel 1 (
    echo No se encontro Python. Instala Python 3.10 o superior desde https://www.python.org
    echo y marca la opcion "Add python.exe to PATH".
    pause
    exit /b 1
)
python -c "import sys; sys.exit(0 if sys.version_info >= (3, 10) else 1)"
if errorlevel 1 (
    echo Se necesita Python 3.10 o superior.
    pause
    exit /b 1
)
python -m pip install -r requirements.txt
if errorlevel 1 (
    echo No se pudieron instalar las dependencias.
    pause
    exit /b 1
)
echo.
echo Ejecutando las pruebas...
python -m unittest discover -s pruebas
echo.
echo Listo. Prueba:  python llano.py ejemplos\01_hola.llano
pause
