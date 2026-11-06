"""Casos de uso de Llano, probados de punta a punta.

Cada caso ejecuta la línea de comandos real (python llano.py ...) como lo
haría un usuario: con su archivo, su entrada por teclado y sus opciones.
Luego compara la salida, el código de salida y verifica que nunca
aparezca una traza interna de Python.

Uso, desde la carpeta del proyecto:

    python pruebas/casos_de_uso.py            ejecuta todo y escribe casos_de_uso/RESULTADOS.md
    python pruebas/casos_de_uso.py -v         además muestra la salida de cada caso
"""

import datetime
import os
import platform
import subprocess
import sys
import tempfile
import time

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LLANO = os.path.join(RAIZ, "llano.py")


def caso(id, nombre, args=None, codigo=None, entrada="", esperado=(), salida=0, preparar=None,
         admite_errores=False):
    """admite_errores: el caso termina bien (salida 0) aunque muestre errores,
    como el modo interactivo, que informa un error y sigue funcionando."""
    return {"id": id, "nombre": nombre, "args": args or [], "codigo": codigo, "entrada": entrada,
            "esperado": list(esperado), "salida": salida, "preparar": preparar,
            "admite_errores": admite_errores}


def cu(nombre_archivo):
    return [os.path.join("casos_de_uso", nombre_archivo)]


# ---------------------------------------------------------------------
#  1. Casos de uso: programas completos que escribiría un estudiante
# ---------------------------------------------------------------------
PROGRAMAS = [
    caso("CU01", "Saludo personalizado (leer un dato)", cu("cu01_saludo.llano"), entrada="Ana\n",
         esperado=["Hola, Ana. Bienvenido a Llano.", "Tu nombre tiene 3 letras."]),
    caso("CU02", "Promedio de notas con validación de rango", cu("cu02_promedio_notas.llano"),
         entrada="3\n4.5\n7\n3\n2.5\n",
         esperado=["La nota debe estar entre 0 y 5", "Promedio: 3.33", "Resultado: aprobó"]),
    caso("CU03", "Tabla Celsius a Fahrenheit (para con paso)", cu("cu03_temperaturas.llano"),
         esperado=["-10 -> 14", "0 -> 32", "40 -> 104"]),
    caso("CU04", "Números primos hasta escribir 0", cu("cu04_numero_primo.llano"),
         entrada="97\n91\n1\n2\n0\n",
         esperado=["97 es primo", "91 no es primo", "1 no es primo", "2 es primo", "Adiós"]),
    caso("CU05", "FizzBuzz (sino si encadenado)", cu("cu05_fizzbuzz.llano"),
         esperado=["Fizz\n4\nBuzz", "14\nFizzBuzz"]),
    caso("CU06", "Contar vocales con tilde", cu("cu06_contar_vocales.llano"),
         entrada="Murciélago aéreo\n", esperado=["La frase tiene 9 vocales"]),
    caso("CU07a", "Palíndromo: frase que sí lo es", cu("cu07_palindromo.llano"),
         entrada="anita lava la tina\n", esperado=['"anita lava la tina" es un palíndromo']),
    caso("CU07b", "Palíndromo: frase que no lo es", cu("cu07_palindromo.llano"),
         entrada="hola mundo\n", esperado=['"hola mundo" no es un palíndromo']),
    caso("CU08", "Lista de compras (agregar, quitar, total)", cu("cu08_lista_compras.llano"),
         esperado=["Total: $23400", "Se quitó: café", "Total: $10500"]),
    caso("CU09", "Búsqueda binaria", cu("cu09_busqueda_binaria.llano"),
         esperado=["encontrado en 3 pasos", "posición: 5", "no encontrado tras 3 pasos", "posición: -1"]),
    caso("CU10", "Ordenamiento por selección y mediana", cu("cu10_ordenar_mediana.llano"),
         esperado=["[18, 19, 19, 19, 20, 21, 22, 25]", "Mediana: 19.5", "Mínima: 18 - Máxima: 25"]),
    caso("CU11", "Suma y transpuesta de matrices", cu("cu11_matrices.llano"),
         esperado=["A + B = [[11, 22, 33], [44, 55, 66]]", "Aᵀ = [[1, 4], [2, 5], [3, 6]]"]),
    caso("CU12", "Torres de Hanói (recursión)", cu("cu12_hanoi.llano"),
         esperado=["Mover disco 3 de A a C", "Total de movimientos: 7"]),
    caso("CU13", "Cajero automático con menú", cu("cu13_cajero.llano"),
         entrada="1\n3\n150000\n3\n30000\n2\n5000\n9\n4\n",
         esperado=["Saldo: $100000", "Fondos insuficientes", "Nuevo saldo: $70000",
                   "Nuevo saldo: $75000", "Opción inválida", "Gracias por usar el cajero"]),
    caso("CU14", "Validar identificadores con un AFD", cu("cu14_validar_identificador.llano"),
         entrada="contador\n2x\nmientras\naño_2026\nhola mundo\n\n",
         esperado=["'contador' es un identificador válido", "'2x' NO es un identificador",
                   "'mientras' es una palabra reservada", "'año_2026' es un identificador válido",
                   "'hola mundo' NO es un identificador"]),
    caso("CU15", "Conversión decimal y binario", cu("cu15_binario.llano"),
         esperado=["255 -> 11111111", "101101 -> 45", "Ida y vuelta 2026: 2026"]),
]

# Los ejemplos del proyecto también deben seguir funcionando
EJEMPLOS = [
    caso("EJ01", "Ejemplo: hola mundo", ["ejemplos/01_hola.llano"], esperado=["¡Hola, mundo!"]),
    caso("EJ05", "Ejemplo: funciones y recursión", ["ejemplos/05_funciones.llano"],
         esperado=["25! = 15511210043330985984000000", "Cuadrados: [1, 4, 9, 16, 25]"]),
    caso("EJ07", "Ejemplo: cadenas (Unidad 1)", ["ejemplos/07_cadenas.llano"],
         esperado=["|Σ³| = 8 = 2³"]),
    caso("EJ08", "Ejemplo: AFD (Unidad 2)", ["ejemplos/08_automata_afd.llano"],
         esperado=["q0 -1-> q1 -1-> q0"]),
    caso("EJ09", "Ejemplo: Mealy y Moore", ["ejemplos/09_traductor_mealy.llano"],
         esperado=["1101 -> Mealy: baab  Moore: baab"]),
    caso("EJ10", "Ejemplo: máquina de Turing aⁿbⁿ", ["ejemplos/10_maquina_turing.llano"],
         esperado=["aaabbb -> verdadero", "abab -> falso"]),
    caso("EJ11", "Ejemplo: calculadora interactiva", ["ejemplos/11_calculadora.llano"],
         entrada="*\n6\n7\nfin\n", esperado=["Resultado: 42", "¡Hasta luego!"]),
]

# ---------------------------------------------------------------------
#  2. Errores típicos de un principiante: el mensaje debe orientar
# ---------------------------------------------------------------------
ERRORES = [
    caso("E01", "Usar = para comparar", codigo="variable x = 5\nsi x = 5 entonces imprimir(1) fin",
         esperado=["Error de sintaxis en la línea 2", "para comparar dos valores se usa '=='"], salida=1),
    caso("E02", "Olvidar el 'fin' de un ciclo",
         codigo="variable i = 0\nmientras i < 3 hacer\n  i = i + 1\n",
         esperado=["falta el 'fin' que cierra este 'mientras'"], salida=1),
    caso("E03", "Nombre de variable mal escrito", codigo="variable total = 1\ntotl = total + 1",
         esperado=["Error semántico", "¿quisiste decir 'total'?"], salida=1),
    caso("E04", "Palabra clave mal escrita", codigo="variable i = 0\nmientra i < 3 hacer i = i + 1 fin",
         esperado=["¿quisiste escribir 'mientras'"], salida=1),
    caso("E05", "Palabra clave en mayúscula", codigo="Si verdadero entonces imprimir(1) fin",
         esperado=["las palabras clave van en minúscula: escribe 'si'"], salida=1),
    caso("E06", "Texto sin cerrar", codigo='imprimir("hola)',
         esperado=["Error léxico", "texto sin cerrar"], salida=1),
    caso("E07", "Operadores de otros lenguajes (&&)", codigo="imprimir(verdadero && falso)",
         esperado=["Error léxico", "se escribe la palabra y"], salida=1),
    caso("E08", "Punto y coma al final", codigo="variable x = 1;",
         esperado=["Llano no usa ';'"], salida=1),
    caso("E09", "Usar 'y' como nombre de variable", codigo="variable y = 2",
         esperado=["'y' es una palabra reservada"], salida=1),
    caso("E10", "'retornar' sin valor", codigo="funcion f()\n  retornar\nfin",
         esperado=["retornar nulo"], salida=1),
    caso("E11", "Argumentos de más", codigo="funcion doble(n) retornar n * 2 fin\nimprimir(doble(1, 2))",
         esperado=["'doble' recibe 1 argumento, pero se le pasaron 2"], salida=1),
    caso("E12", "División por cero", codigo="variable a = 10\nimprimir(a / 0)",
         esperado=["Error de ejecución en la línea 2", "división por cero"], salida=1),
    caso("E13", "Posición fuera de la lista", codigo="variable l = [1, 2, 3]\nimprimir(l[3])",
         esperado=["posición 3 fuera de rango (válidas: 0 a 2)"], salida=1),
    caso("E14", "Condición que no es lógica", codigo="si 1 entonces imprimir(1) fin",
         esperado=["debe ser verdadero o falso"], salida=1),
    caso("E15", "Recursión sin caso base", codigo="funcion f(n) retornar f(n) fin\nf(1)",
         esperado=["¿una recursión sin caso base?"], salida=1),
    caso("E16", "Texto que no es número", codigo='imprimir(numero("doce"))',
         esperado=['el texto "doce" no es un número válido'], salida=1),
    caso("E17", "Leer cuando ya no hay datos", codigo='variable n = leer("Dato: ")',
         esperado=["leer() no recibió datos"], salida=1),
    caso("E18", "Varios errores semánticos a la vez", codigo="a = 1\nimprimir(b)\nretornar 3",
         esperado=["línea 1", "línea 2", "línea 3", "'retornar' solo puede usarse dentro de una función"],
         salida=1),
]

# ---------------------------------------------------------------------
#  3. Línea de comandos y entorno
# ---------------------------------------------------------------------


def _crear_crlf_bom(carpeta):
    ruta = os.path.join(carpeta, "windows.llano")
    with open(ruta, "wb") as f:
        f.write('﻿variable n = 2\r\nimprimir("ok", n * 21)\r\n'.encode("utf-8"))
    return ["windows.llano"]


def _crear_latin1(carpeta):
    ruta = os.path.join(carpeta, "latin1.llano")
    with open(ruta, "wb") as f:
        f.write('imprimir("canción")'.encode("latin-1"))
    return ["latin1.llano"]


def _crear_con_espacios(carpeta):
    sub = os.path.join(carpeta, "mi carpeta con espacios")
    os.makedirs(sub, exist_ok=True)
    with open(os.path.join(sub, "prueba.llano"), "w", encoding="utf-8") as f:
        f.write('imprimir("desde otra carpeta")')
    return [os.path.join(sub, "prueba.llano")]


LINEA_COMANDOS = [
    caso("L01", "--tokens muestra el análisis léxico", ["ejemplos/01_hola.llano", "--tokens"],
         esperado=["ID", "TEXTO", "Total: 8 tokens"]),
    caso("L02", "--arbol muestra la precedencia", ["-e", "variable x = 2 + 3 * 4", "--arbol"],
         esperado=["declaracion", "suma", "producto"]),
    caso("L03", "--dot genera Graphviz", ["-e", "imprimir(1)", "--dot"], esperado=["digraph arbol {"]),
    caso("L04", "--verificar no ejecuta", ["-e", 'imprimir("no debe salir")', "--verificar"],
         esperado=["no tiene errores léxicos, sintácticos ni semánticos"]),
    caso("L05", "--funciones lista las 15 predefinidas", ["--funciones"],
         esperado=["imprimir", "subcadena", "aleatorio"]),
    caso("L06", "--version", ["--version"], esperado=["Llano 0.2.0"]),
    caso("L07", "Modo interactivo con bloque de varias líneas", [],
         entrada="variable a = 5\na * 2\nfuncion f(n)\n  retornar n + a\nfin\nf(10)\nsalir\n",
         esperado=["llano>", "10", "15"]),
    caso("L08", "Modo interactivo sigue tras un error", [],
         entrada="imprimir(z)\nimprimir(\"sigo\")\nsalir\n", esperado=["'z' no ha sido declarado", "sigo"],
         admite_errores=True),
    caso("L09", "Archivo inexistente", ["no_existe.llano"], esperado=["No se encontró el archivo"], salida=1),
    caso("L10", "Archivo de Windows (CRLF y BOM)", preparar=_crear_crlf_bom, esperado=["ok 42"]),
    caso("L11", "Archivo que no está en UTF-8", preparar=_crear_latin1,
         esperado=["no está guardado en UTF-8"], salida=1),
    caso("L12", "Ruta con espacios, ejecutado desde otra carpeta", preparar=_crear_con_espacios,
         esperado=["desde otra carpeta"]),
    caso("L13", "Enteros grandes (2000! tiene 5736 dígitos)",
         codigo="funcion f(n) si n <= 1 entonces retornar 1 fin retornar n * f(n - 1) fin\n"
                "imprimir(longitud(texto(f(2000))))", esperado=["5736"]),
    caso("L14", "Rendimiento: ciclo de 100 000 vueltas",
         codigo="variable s = 0\npara i desde 1 hasta 100000 hacer s = s + i fin\nimprimir(s)",
         esperado=["5000050000"]),
]

GRUPOS = [
    ("Casos de uso (programas completos)", PROGRAMAS),
    ("Ejemplos del proyecto", EJEMPLOS),
    ("Errores típicos de un principiante", ERRORES),
    ("Línea de comandos y entorno", LINEA_COMANDOS),
]


def ejecutar_caso(c):
    """Ejecuta un caso y devuelve (paso, detalle, salida_completa, segundos)."""
    with tempfile.TemporaryDirectory() as tmp:
        args = list(c["args"])
        cwd = RAIZ
        if c["preparar"]:
            args = c["preparar"](tmp)
            cwd = tmp
        if c["codigo"] is not None:
            args = ["-e", c["codigo"]] + args
        env = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONUTF8="1")
        inicio = time.perf_counter()
        try:
            r = subprocess.run([sys.executable, LLANO] + args, input=c["entrada"].encode("utf-8"),
                               capture_output=True, cwd=cwd, env=env, timeout=120)
        except subprocess.TimeoutExpired:
            return False, "tardó más de 120 s", "", 120.0
        segundos = time.perf_counter() - inicio
    salida = r.stdout.decode("utf-8", "replace").replace("\r\n", "\n")
    errores = r.stderr.decode("utf-8", "replace").replace("\r\n", "\n")
    todo = salida + errores
    problemas = []
    if "Traceback" in todo:
        problemas.append("apareció una traza interna de Python")
    if r.returncode != c["salida"]:
        problemas.append(f"código de salida {r.returncode}, se esperaba {c['salida']}")
    if c["salida"] == 0 and errores.strip() and not c["admite_errores"]:
        problemas.append(f"mensaje inesperado: {errores.strip().splitlines()[0]}")
    for e in c["esperado"]:
        if e not in todo:
            problemas.append(f"falta en la salida: {e!r}")
    return not problemas, "; ".join(problemas), todo, segundos


def main():
    detallado = "-v" in sys.argv
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    filas, fallas, total = [], 0, 0
    inicio = time.perf_counter()
    for titulo, casos in GRUPOS:
        print(f"\n{titulo}")
        print("-" * len(titulo))
        filas.append(f"\n### {titulo}\n\n| ID | Caso | Resultado | Tiempo |\n| --- | --- | --- | --- |")
        for c in casos:
            total += 1
            paso, detalle, todo, seg = ejecutar_caso(c)
            estado = "PASA " if paso else "FALLA"
            fallas += not paso
            print(f"  [{estado}] {c['id']:<6} {c['nombre']}  ({seg:.2f} s)")
            if not paso:
                print(f"           {detalle}")
            if detallado or not paso:
                for linea in todo.strip().splitlines()[:12]:
                    print(f"           | {linea}")
            resultado = "Pasa" if paso else f"**Falla:** {detalle}"
            filas.append(f"| {c['id']} | {c['nombre']} | {resultado} | {seg:.2f} s |")
    duracion = time.perf_counter() - inicio
    resumen = f"{total - fallas} de {total} casos pasan ({fallas} fallas) en {duracion:.1f} s"
    print(f"\n{resumen}")

    informe = [
        "# Resultados de los casos de uso de Llano",
        "",
        f"- Fecha: {datetime.datetime.now():%Y-%m-%d %H:%M}",
        f"- Sistema: {platform.system()} {platform.release()} · Python {platform.python_version()}",
        f"- Resumen: **{resumen}**",
        "",
        "Cada caso ejecuta `python llano.py` como lo haría un usuario y revisa la salida, "
        "el código de salida y que no aparezcan trazas internas de Python.",
    ] + filas
    ruta = os.path.join(RAIZ, "casos_de_uso", "RESULTADOS.md")
    with open(ruta, "w", encoding="utf-8") as f:
        f.write("\n".join(informe) + "\n")
    print(f"Informe guardado en {os.path.relpath(ruta, RAIZ)}")
    return 1 if fallas else 0


if __name__ == "__main__":
    sys.exit(main())
