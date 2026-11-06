# Resultados de los casos de uso de Llano

- Fecha: 2026-10-30 22:17
- Sistema: Linux 6.18.44-fc-v185 · Python 3.13.18
- Resumen: **55 de 55 casos pasan (0 fallas) en 5.3 s**

Cada caso ejecuta `python llano.py` como lo haría un usuario y revisa la salida, el código de salida y que no aparezcan trazas internas de Python.

### Casos de uso (programas completos)

| ID | Caso | Resultado | Tiempo |
| --- | --- | --- | --- |
| CU01 | Saludo personalizado (leer un dato) | Pasa | 0.07 s |
| CU02 | Promedio de notas con validación de rango | Pasa | 0.08 s |
| CU03 | Tabla Celsius a Fahrenheit (para con paso) | Pasa | 0.08 s |
| CU04 | Números primos hasta escribir 0 | Pasa | 0.08 s |
| CU05 | FizzBuzz (sino si encadenado) | Pasa | 0.09 s |
| CU06 | Contar vocales con tilde | Pasa | 0.08 s |
| CU07a | Palíndromo: frase que sí lo es | Pasa | 0.09 s |
| CU07b | Palíndromo: frase que no lo es | Pasa | 0.08 s |
| CU08 | Lista de compras (agregar, quitar, total) | Pasa | 0.08 s |
| CU09 | Búsqueda binaria | Pasa | 0.12 s |
| CU10 | Ordenamiento por selección y mediana | Pasa | 0.10 s |
| CU11 | Suma y transpuesta de matrices | Pasa | 0.08 s |
| CU12 | Torres de Hanói (recursión) | Pasa | 0.07 s |
| CU13 | Cajero automático con menú | Pasa | 0.16 s |
| CU14 | Validar identificadores con un AFD | Pasa | 0.15 s |
| CU15 | Conversión decimal y binario | Pasa | 0.09 s |

### Ejemplos del proyecto

| ID | Caso | Resultado | Tiempo |
| --- | --- | --- | --- |
| EJ01 | Ejemplo: hola mundo | Pasa | 0.06 s |
| EJ05 | Ejemplo: funciones y recursión | Pasa | 0.19 s |
| EJ07 | Ejemplo: cadenas (Unidad 1) | Pasa | 0.10 s |
| EJ08 | Ejemplo: AFD (Unidad 2) | Pasa | 0.10 s |
| EJ09 | Ejemplo: Mealy y Moore | Pasa | 0.14 s |
| EJ10 | Ejemplo: máquina de Turing aⁿbⁿ | Pasa | 0.14 s |
| EJ11 | Ejemplo: calculadora interactiva | Pasa | 0.18 s |

### Errores típicos de un principiante

| ID | Caso | Resultado | Tiempo |
| --- | --- | --- | --- |
| E01 | Usar = para comparar | Pasa | 0.06 s |
| E02 | Olvidar el 'fin' de un ciclo | Pasa | 0.06 s |
| E03 | Nombre de variable mal escrito | Pasa | 0.07 s |
| E04 | Palabra clave mal escrita | Pasa | 0.08 s |
| E05 | Palabra clave en mayúscula | Pasa | 0.06 s |
| E06 | Texto sin cerrar | Pasa | 0.06 s |
| E07 | Operadores de otros lenguajes (&&) | Pasa | 0.05 s |
| E08 | Punto y coma al final | Pasa | 0.05 s |
| E09 | Usar 'y' como nombre de variable | Pasa | 0.06 s |
| E10 | 'retornar' sin valor | Pasa | 0.06 s |
| E11 | Argumentos de más | Pasa | 0.07 s |
| E12 | División por cero | Pasa | 0.06 s |
| E13 | Posición fuera de la lista | Pasa | 0.06 s |
| E14 | Condición que no es lógica | Pasa | 0.06 s |
| E15 | Recursión sin caso base | Pasa | 0.10 s |
| E16 | Texto que no es número | Pasa | 0.06 s |
| E17 | Leer cuando ya no hay datos | Pasa | 0.06 s |
| E18 | Varios errores semánticos a la vez | Pasa | 0.06 s |

### Línea de comandos y entorno

| ID | Caso | Resultado | Tiempo |
| --- | --- | --- | --- |
| L01 | --tokens muestra el análisis léxico | Pasa | 0.05 s |
| L02 | --arbol muestra la precedencia | Pasa | 0.05 s |
| L03 | --dot genera Graphviz | Pasa | 0.05 s |
| L04 | --verificar no ejecuta | Pasa | 0.06 s |
| L05 | --funciones lista las 15 predefinidas | Pasa | 0.05 s |
| L06 | --version | Pasa | 0.05 s |
| L07 | Modo interactivo con bloque de varias líneas | Pasa | 0.07 s |
| L08 | Modo interactivo sigue tras un error | Pasa | 0.06 s |
| L09 | Archivo inexistente | Pasa | 0.05 s |
| L10 | Archivo de Windows (CRLF y BOM) | Pasa | 0.06 s |
| L11 | Archivo que no está en UTF-8 | Pasa | 0.05 s |
| L12 | Ruta con espacios, ejecutado desde otra carpeta | Pasa | 0.06 s |
| L13 | Enteros grandes (2000! tiene 5736 dígitos) | Pasa | 0.12 s |
| L14 | Rendimiento: ciclo de 100 000 vueltas | Pasa | 0.90 s |
