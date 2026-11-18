# Resultados de los casos de uso de Llano

- Fecha: 2026-11-17 17:10
- Sistema: Windows 11 · Python 3.13.6
- Resumen: **75 de 75 casos pasan (0 fallas) en 106.0 s**

Cada caso ejecuta `python llano.py` como lo haría un usuario y revisa la salida, el código de salida y que no aparezcan trazas internas de Python.

### Casos de uso (programas completos)

| ID | Caso | Resultado | Tiempo |
| --- | --- | --- | --- |
| CU01 | Saludo personalizado (leer un dato) | Pasa | 0.98 s |
| CU02 | Promedio de notas con validación de rango | Pasa | 2.17 s |
| CU03 | Tabla Celsius a Fahrenheit (para con paso) | Pasa | 1.59 s |
| CU04 | Números primos hasta escribir 0 | Pasa | 1.43 s |
| CU05 | FizzBuzz (sino si encadenado) | Pasa | 1.18 s |
| CU06 | Contar vocales con tilde | Pasa | 1.59 s |
| CU07a | Palíndromo: frase que sí lo es | Pasa | 1.19 s |
| CU07b | Palíndromo: frase que no lo es | Pasa | 1.49 s |
| CU08 | Lista de compras (agregar, quitar, total) | Pasa | 1.29 s |
| CU09 | Búsqueda binaria | Pasa | 1.63 s |
| CU10 | Ordenamiento por selección y mediana | Pasa | 1.21 s |
| CU11 | Suma y transpuesta de matrices | Pasa | 1.48 s |
| CU12 | Torres de Hanói (recursión) | Pasa | 1.20 s |
| CU13 | Cajero automático con menú | Pasa | 1.77 s |
| CU14 | Validar identificadores con un AFD | Pasa | 1.20 s |
| CU15 | Conversión decimal y binario | Pasa | 1.48 s |

### Ejemplos del proyecto

| ID | Caso | Resultado | Tiempo |
| --- | --- | --- | --- |
| EJ01 | Ejemplo: hola mundo | Pasa | 2.09 s |
| EJ05 | Ejemplo: funciones y recursión | Pasa | 1.03 s |
| EJ07 | Ejemplo: cadenas (Unidad 1) | Pasa | 2.10 s |
| EJ08 | Ejemplo: AFD (Unidad 2) | Pasa | 0.66 s |
| EJ09 | Ejemplo: Mealy y Moore | Pasa | 2.09 s |
| EJ10 | Ejemplo: máquina de Turing aⁿbⁿ | Pasa | 0.72 s |
| EJ11 | Ejemplo: calculadora interactiva | Pasa | 2.08 s |
| EJ12 | Ejemplo: salidas de ciclos y restricciones | Pasa | 0.61 s |

### Errores típicos de un principiante

| ID | Caso | Resultado | Tiempo |
| --- | --- | --- | --- |
| E01 | Usar = para comparar | Pasa | 2.07 s |
| E02 | Olvidar el 'fin' de un ciclo | Pasa | 1.47 s |
| E03 | Nombre de variable mal escrito | Pasa | 1.29 s |
| E04 | Palabra clave mal escrita | Pasa | 1.40 s |
| E05 | Palabra clave en mayúscula | Pasa | 1.19 s |
| E06 | Texto sin cerrar | Pasa | 1.39 s |
| E07 | Operadores de otros lenguajes (&&) | Pasa | 1.24 s |
| E08 | Punto y coma al final | Pasa | 1.40 s |
| E09 | Usar 'y' como nombre de variable | Pasa | 1.22 s |
| E10 | 'retornar' sin valor | Pasa | 1.38 s |
| E11 | Argumentos de más | Pasa | 1.23 s |
| E12 | División por cero | Pasa | 1.43 s |
| E13 | Posición fuera de la lista | Pasa | 1.20 s |
| E14 | Condición que no es lógica | Pasa | 1.50 s |
| E15 | Recursión sin caso base | Pasa | 1.23 s |
| E16 | Texto que no es número | Pasa | 1.45 s |
| E17 | Leer cuando ya no hay datos | Pasa | 1.23 s |
| E18 | Varios errores semánticos a la vez | Pasa | 1.44 s |

### Salidas de los ciclos y restricciones

| ID | Caso | Resultado | Tiempo |
| --- | --- | --- | --- |
| C01 | 'romper' sale de un ciclo 'mientras verdadero' | Pasa | 1.21 s |
| C02 | 'continuar' salta a la siguiente repetición | Pasa | 1.44 s |
| C03 | Menú que se repite hasta escribir 'salir' | Pasa | 1.20 s |
| C04 | 'mientras verdadero' sin salida se rechaza antes de ejecutar | Pasa | 1.46 s |
| C05 | Ciclo que nunca termina se detiene al superar el límite | Pasa | 1.39 s |
| C06 | Sin advertencia si el ciclo tiene 'romper' | Pasa | 1.48 s |
| C07 | Advertencia: posible ciclo infinito (olvidó aumentar el contador) | Pasa | 1.50 s |
| C08 | 'romper' fuera de un ciclo | Pasa | 1.41 s |
| C09 | 'continuar' dentro de una función pero fuera de su ciclo | Pasa | 1.25 s |
| C10 | División por cero con variables (en ejecución) | Pasa | 1.41 s |
| C11 | Módulo por cero | Pasa | 1.21 s |
| C12 | Raíz de un número negativo | Pasa | 1.47 s |
| C13 | Logaritmo fuera de su dominio | Pasa | 1.21 s |
| C14 | Base de logaritmo inválida | Pasa | 1.52 s |
| C15 | Desbordamiento de un número real | Pasa | 1.21 s |
| C16 | Cero elevado a un exponente negativo | Pasa | 1.44 s |
| C17 | Condición constante que no es lógica | Pasa | 1.20 s |
| C18 | 'para' con paso 0 se rechaza antes de ejecutar | Pasa | 1.34 s |
| C19 | Nunca se muestra un error de Python | Pasa | 1.24 s |

### Línea de comandos y entorno

| ID | Caso | Resultado | Tiempo |
| --- | --- | --- | --- |
| L01 | --tokens muestra el análisis léxico | Pasa | 1.34 s |
| L02 | --arbol muestra la precedencia | Pasa | 1.23 s |
| L03 | --dot genera Graphviz | Pasa | 1.36 s |
| L04 | --verificar no ejecuta | Pasa | 1.22 s |
| L05 | --funciones lista las 16 predefinidas | Pasa | 1.34 s |
| L06 | --version | Pasa | 1.25 s |
| L07 | Modo interactivo con bloque de varias líneas | Pasa | 1.38 s |
| L08 | Modo interactivo sigue tras un error | Pasa | 1.22 s |
| L09 | Archivo inexistente | Pasa | 1.47 s |
| L10 | Archivo de Windows (CRLF y BOM) | Pasa | 1.19 s |
| L11 | Archivo que no está en UTF-8 | Pasa | 1.36 s |
| L12 | Ruta con espacios, ejecutado desde otra carpeta | Pasa | 1.20 s |
| L13 | Enteros grandes (2000! tiene 5736 dígitos) | Pasa | 3.52 s |
| L14 | Rendimiento: ciclo de 100 000 vueltas | Pasa | 2.11 s |
