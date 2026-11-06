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

**Funciones predefinidas:** `imprimir`, `leer`, `numero`, `texto`, `entero`, `longitud`, `agregar`, `quitar`, `invertir`, `subcadena`, `tipo`, `raiz`, `absoluto`, `redondear`, `aleatorio`.

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
| Semántica | variable sin declarar, declaración repetida, número de argumentos | `ejemplos/errores/3_semantico.llano` |
| Ejecución | división por cero, posición fuera de rango, condición no lógica | `ejemplos/errores/4_ejecucion.llano` |

Los errores semánticos se reportan todos juntos y **antes** de ejecutar el programa.

Cuando el error es típico de quien empieza, el mensaje agrega una pista: `=` en lugar de `==`, una palabra clave mal escrita o en mayúscula (`mientra`, `Si`), un nombre parecido a uno declarado (`totl` → `total`), `;`, `&&` o comillas simples traídos de otros lenguajes, o `retornar` sin valor.

## Casos de uso

La carpeta `casos_de_uso/` tiene 15 programas como los que escribiría un estudiante: promedio de notas, primos, FizzBuzz, palíndromos, lista de compras, búsqueda binaria, ordenamiento, matrices, Torres de Hanói, cajero automático, validación de identificadores con un AFD y conversión a binario. Varios leen datos del teclado.

`pruebas/casos_de_uso.py` ejecuta 55 casos de punta a punta, igual que un usuario: esos programas con sus entradas, los ejemplos, 18 errores típicos y las opciones de la línea de comandos (tokens, árbol, modo interactivo, archivos de Windows, rutas con espacios, enteros grandes). Comprueba la salida y el código de salida, y que nunca aparezca una traza interna de Python. El resultado queda en `casos_de_uso/RESULTADOS.md`.

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
