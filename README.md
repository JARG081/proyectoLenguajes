# Llano

**Llano** es un lenguaje de programación sencillo con palabras clave en español. Tiene variables, condicionales, ciclos, funciones, listas y textos. Su analizador léxico y sintáctico se genera con **ANTLR 4.13.2** a partir de una gramática libre de contexto, y el intérprete está escrito en **Python**.

Proyecto final del curso *Lenguajes de Programación* — Ingeniería de Sistemas, Universidad de los Llanos.

```
funcion factorial(n)
    si n <= 1 entonces
        retornar 1
    fin
    retornar n * factorial(n - 1)
fin

para i desde 1 hasta 5 hacer
    imprimir(i, "! =", factorial(i))
fin
```

## Requisitos

- Python 3.10 o superior.
- Java 11 o superior **solo** si se modifica la gramática (para regenerar el analizador). Los analizadores ya generados vienen en `llano/generado/`.

## Instalación

| Dónde | Comando |
|---|---|
| Windows (CMD o doble clic) | `instalar.bat` |
| Git Bash, Linux o macOS | `./instalar.sh` |
| Manual | `python -m pip install -r requirements.txt` |

El instalador revisa la versión de Python, instala el runtime de ANTLR y ejecuta las pruebas.

## Uso

| Comando | Qué hace |
|---|---|
| `python llano.py programa.llano` | Ejecuta un programa |
| `python llano.py` | Modo interactivo (escribe `salir` para terminar) |
| `python llano.py -e "imprimir(2 + 3)"` | Ejecuta código escrito en la línea |
| `python llano.py programa.llano --tokens` | Muestra los tokens: resultado del **análisis léxico** |
| `python llano.py programa.llano --arbol` | Muestra el **árbol de derivación** (compacto) |
| `python llano.py programa.llano --arbol-completo` | Árbol con todas las reglas de precedencia |
| `python llano.py programa.llano --dot` | Árbol en formato Graphviz DOT |
| `python llano.py programa.llano --verificar` | Solo analiza (léxico, sintaxis, semántica), no ejecuta |
| `python llano.py --funciones` | Lista las funciones predefinidas |
| `python llano.py programa.llano --max-iteraciones 5000` | Cambia el máximo de vueltas de un ciclo (por defecto 1.000.000; `0` = sin límite) |
| `python llano.py programa.llano --depurar` | Muestra la traza de Python si falla el intérprete (solo para desarrollo) |
| `probar.bat` (o `./probar.sh`) | Ejecuta las pruebas unitarias y los casos de uso |
| `python -m unittest discover -s pruebas -v` | Solo las pruebas unitarias |
| `python pruebas/casos_de_uso.py -v` | Solo los casos de uso, mostrando la salida de cada uno |

Los archivos `.llano` deben guardarse en UTF-8 (es lo normal en VS Code).

## El lenguaje en una página

```
# Comentario hasta el final de la línea

variable x = 10                 # declarar (obligatorio antes de usar)
x = x + 1                       # asignar
variable nombre = "Ana"         # texto
variable activo = verdadero     # lógico: verdadero / falso
variable nada = nulo
variable lista = [1, 2, 3]      # listas; posiciones desde 0
lista[0] = 99

si x > 10 y activo entonces     # y, o, no
    imprimir("grande")
sino si x == 10 entonces
    imprimir("diez")
sino
    imprimir("pequeño")
fin

mientras x > 0 hacer
    x = x - 3
fin

para i desde 1 hasta 10 hacer           # límites incluidos
    imprimir(i)
fin
para i desde 10 hasta 0 paso -2 hacer   # paso opcional (por defecto 1)
    imprimir(i)
fin

mientras verdadero hacer                # salidas de un ciclo:
    variable dato = leer("Dato: ")
    si dato == "salir" entonces romper fin        # termina el ciclo
    si dato == "" entonces continuar fin          # pasa a la siguiente vuelta
    imprimir("Leí", dato)
fin

funcion area(base, altura)
    retornar base * altura / 2
fin
imprimir("Área:", area(4, 3))
```

- Operadores, de menor a mayor precedencia: `o` · `y` · `no` · `== != < > <= >=` · `+ -` · `* / %` · `-` (negativo) · `^` (potencia, asociativa a la derecha).
- `+` con un texto concatena (`"n=" + 5` da `"n=5"`); `"ab" * 3` da `"ababab"` (potencia de una cadena).
- Cada bloque `si`, `mientras` o `para` tiene su propio ámbito. Las funciones pueden llamarse antes de la línea donde se definen.
- Las condiciones deben ser `verdadero` o `falso`: `si 1 entonces` es un error.
- `funcion` también puede escribirse `función`.
- `romper` termina el ciclo más interno; `continuar` salta a su siguiente vuelta (en un `para`, la variable avanza igual). Solo valen dentro de un `mientras` o un `para`. `retornar` también sale de los ciclos de una función.

**Funciones predefinidas:** `imprimir`, `leer`, `numero`, `texto`, `entero`, `longitud`, `agregar`, `quitar`, `invertir`, `subcadena`, `tipo`, `raiz`, `logaritmo`, `absoluto`, `redondear`, `aleatorio`.

### Protección contra ciclos infinitos

Decidir si cualquier programa termina es imposible (problema de la parada), así que Llano combina tres defensas:

| Defensa | Cuándo actúa | Ejemplo |
|---|---|---|
| Error semántico (antes de ejecutar) | Ciclos infinitos evidentes | `mientras verdadero hacer … fin` sin `romper` ni `retornar`; `para … paso 0` |
| Advertencia (el programa sí se ejecuta) | La condición no puede cambiar dentro del ciclo, o el ciclo nunca se ejecuta | `mientras i < 3 hacer imprimir(i) fin` (falta `i = i + 1`); `mientras falso` |
| Límite de repeticiones (en ejecución) | Un ciclo pasa de 1.000.000 de vueltas | Se detiene con un error que sugiere usar `romper`. Se cambia con `--max-iteraciones N` (0 = sin límite) |

Además, **Ctrl+C** detiene cualquier programa (también en el modo interactivo, que sigue funcionando) y la recursión está limitada a 3000 llamadas anidadas.

### Restricciones lógicas y matemáticas

| Restricción | Mensaje |
|---|---|
| `a / 0`, `a % 0` | división por cero / módulo por cero |
| `0 ^ n` con n < 0 | división por cero (0 elevado a un exponente negativo) |
| `(-8) ^ 0.5` | una base negativa solo admite exponentes enteros |
| `raiz(x)` con x < 0 | no existe la raíz cuadrada real de un número negativo |
| `logaritmo(x, b)` con x ≤ 0, b ≤ 0 o b = 1 | el logaritmo solo existe para números mayores que 0 / la base debe ser mayor que 0 y distinta de 1 |
| Resultados infinitos o indeterminados (`1.5 ^ 5000`) | el resultado es demasiado grande para representarse (desbordamiento) |
| Enteros de más de 1.000.000 de cifras, textos de más de 10.000.000 de caracteres | el número/texto es demasiado grande |
| Condiciones de `si` y `mientras` | deben ser `verdadero` o `falso`; `si 1 entonces` es un error |
| `y`, `o`, `no` | solo con valores lógicos (`1 y 2` es un error) |
| Comparar tipos distintos con `<` | no se puede comparar número con texto |

Si la expresión es **constante** (solo literales y funciones puras como `raiz`), el error se detecta en el análisis semántico, antes de ejecutar: `imprimir(x / 0)` o `raiz(-4)` nunca llegan a correr. Con variables, se detecta al ejecutar.

Todos los errores se muestran en español: si una operación falla dentro de Python por un caso no previsto, el intérprete lo convierte en un error de Llano con la línea y la columna. La traza de Python solo aparece con `--depurar` (para desarrollo).

La especificación formal (alfabeto, expresiones regulares, AFD de los tokens, gramática y semántica) está en [`docs/especificacion.md`](docs/especificacion.md).

## Mensajes de error

Los errores se informan en español, con la fase en que se detectan, la línea, la columna y una marca:

```
Error semántico en la línea 3, columna 1: la variable 'totl' no ha sido declarada (declárala con: variable totl = ...)
    totl = total + 1
    ^
```

| Fase | Ejemplo | Archivo |
|---|---|---|
| Léxica | carácter que no pertenece al alfabeto, texto sin cerrar | `ejemplos/errores/1_lexico.llano` |
| Sintáctica | falta un `fin`, sobra un símbolo, palabra reservada como nombre | `ejemplos/errores/2_sintactico.llano` |
| Semántica | variable sin declarar, declaración repetida, número de argumentos, `romper` fuera de un ciclo, ciclo infinito evidente, división por cero constante | `ejemplos/errores/3_semantico.llano` |
| Ejecución | división por cero con variables, posición fuera de rango, condición no lógica, ciclo que supera el límite de repeticiones | `ejemplos/errores/4_ejecucion.llano` |
| Advertencia | posible ciclo infinito, ciclo que nunca se ejecuta (no detiene el programa) | — |

Los errores semánticos se reportan todos juntos y **antes** de ejecutar el programa.

Cuando el error es típico de quien empieza, el mensaje agrega una pista: `=` en lugar de `==`, una palabra clave mal escrita o en mayúscula (`mientra`, `Si`), un nombre parecido a uno declarado (`totl` → `total`), `;`, `&&` o comillas simples traídos de otros lenguajes, o `retornar` sin valor.

## Casos de uso

La carpeta `casos_de_uso/` tiene 16 programas como los que escribiría un estudiante: promedio de notas, primos, FizzBuzz, palíndromos, lista de compras, búsqueda binaria, ordenamiento, matrices, Torres de Hanói, cajero automático, validación de identificadores con un AFD y conversión a binario y un menú que termina con `romper`. Varios leen datos del teclado.

`pruebas/casos_de_uso.py` ejecuta 75 casos de punta a punta, igual que un usuario: esos programas con sus entradas, los ejemplos, 18 errores típicos, 19 casos de salidas de ciclos y restricciones matemáticas, y las opciones de la línea de comandos (tokens, árbol, modo interactivo, archivos de Windows, rutas con espacios, enteros grandes). Comprueba la salida y el código de salida, y que nunca aparezca una traza interna de Python. El resultado queda en `casos_de_uso/RESULTADOS.md`.

## Ejemplos

| Archivo | Tema |
|---|---|
| `01_hola.llano` | Primer programa |
| `02_variables.llano` | Tipos, operadores y precedencia |
| `03_condicionales.llano` | `si` / `sino si` / `sino`, operadores lógicos |
| `04_ciclos.llano` | `para`, `mientras`, algoritmo de Euclides |
| `05_funciones.llano` | Recursión, primos, funciones como valores |
| `06_listas.llano` | Promedio, máximo, burbuja, matrices |
| `07_cadenas.llano` | **Unidad 1:** longitud, concatenación, potencia, reflexión, palíndromos, prefijos, sufijos, Σᵏ |
| `08_automata_afd.llano` | **Unidad 2:** simulación de un AFD con su tabla de transiciones |
| `09_traductor_mealy.llano` | **Unidad 2:** máquinas de Mealy y Moore (ejemplo de clase) |
| `10_maquina_turing.llano` | **MT** que reconoce aⁿbⁿ: Llano puede simular una máquina de Turing |
| `11_calculadora.llano` | Programa interactivo con `leer()` |
| `12_salidas_y_restricciones.llano` | `romper`, `continuar`, `retornar` dentro de un ciclo; restricciones matemáticas |

## Arquitectura

```
fuente .llano
   │  análisis léxico      (LlanoLexer, generado por ANTLR desde las ER)
   ▼
tokens
   │  análisis sintáctico  (LlanoParser, generado por ANTLR desde la GLC)
   ▼
árbol de derivación
   │  análisis semántico   (llano/semantico.py: tabla de símbolos por ámbitos)
   ▼
árbol validado
   │  interpretación       (llano/interprete.py: recorre el árbol con un Visitor)
   ▼
resultado
```

```
gramatica/Llano.g4        Gramática: componentes léxicos (ER) y sintaxis (GLC)
llano/
├─ generado/              Analizadores generados por ANTLR (no editar a mano)
├─ analisis.py            Fases léxica y sintáctica, --tokens, --arbol, --dot
├─ semantico.py           Análisis semántico
├─ interprete.py          Intérprete (Visitor)
├─ valores.py             Tipos, conversión a texto y funciones predefinidas
├─ errores.py             Errores y traducción de los mensajes de ANTLR
└─ __init__.py            API: ejecutar(), verificar()
llano.py                  Línea de comandos y modo interactivo
ejemplos/                 Programas de ejemplo y de errores
casos_de_uso/             15 programas de casos de uso y RESULTADOS.md
pruebas/                  Pruebas unitarias y casos de uso de punta a punta
herramientas/             ANTLR 4.13.2 y script para regenerar el analizador
docs/                     Especificación del lenguaje y plan del proyecto
```

## Modificar la gramática

1. Edita `gramatica/Llano.g4`.
2. Ejecuta `python herramientas/generar_parser.py` (requiere Java).
3. Ajusta `llano/semantico.py` y `llano/interprete.py` si agregaste reglas.
4. Ejecuta las pruebas.

## Referencias

- Aho, A. V., Lam, M. S., Sethi, R. y Ullman, J. D. (2008). *Compiladores: principios, técnicas y herramientas* (2.ª ed.). Pearson.
- Hopcroft, J. E., Motwani, R. y Ullman, J. D. (2007). *Introducción a la teoría de autómatas, lenguajes y computación* (3.ª ed.). Pearson.
- Parr, T. (2013). *The definitive ANTLR 4 reference*. The Pragmatic Bookshelf.
- Parr, T., Harwell, S. y Fisher, K. (2014). Adaptive LL(*) parsing: The power of dynamic analysis. *ACM SIGPLAN Notices, 49*(10), 579–598. https://doi.org/10.1145/2714064.2660202
- Nystrom, R. (2021). *Crafting interpreters*. Genever Benning. https://craftinginterpreters.com
# proyectoLenguajes
