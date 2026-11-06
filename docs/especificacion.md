# Especificación formal de Llano

Este documento describe Llano con las herramientas del curso: alfabeto, expresiones regulares (ER), autómatas finitos deterministas (AFD), gramáticas libres de contexto (GLC) y, para la discusión de computabilidad, máquinas de Turing (MT). Se usa la notación del curso: **λ** es la cadena vacía.

## 1. Fases del procesamiento

| Fase | Entrada → salida | Modelo formal | Clase en la jerarquía de Chomsky | Implementación |
|---|---|---|---|---|
| Léxica | caracteres → tokens | ER / AFD | Tipo 3 (regular) | `LlanoLexer` (ANTLR) |
| Sintáctica | tokens → árbol de derivación | GLC / autómata de pila | Tipo 2 (libre de contexto) | `LlanoParser` (ANTLR, ALL(*)) |
| Semántica | árbol → árbol validado | Tabla de símbolos | Restricciones dependientes del contexto | `llano/semantico.py` |
| Ejecución | árbol → resultado | Intérprete (equivale a una MT) | Tipo 0 | `llano/interprete.py` |

Cada fase reconoce una clase de lenguajes más amplia que la anterior. Por eso se separan: los tokens se pueden describir con ER, pero el anidamiento de bloques (`si … fin` dentro de `mientras … fin`) necesita una GLC, y la regla "una variable debe declararse antes de usarse" no se puede expresar con una GLC, así que se revisa en la fase semántica.

## 2. Alfabeto

El alfabeto de entrada Σ es el conjunto de caracteres que pueden aparecer en un programa:

- Letras: `a`–`z`, `A`–`Z`, `á é í ó ú Á É Í Ó Ú ñ Ñ ü Ü` y `_`
- Dígitos: `0`–`9`
- Símbolos: `+ - * / % ^ = < > ! ( ) [ ] , . " # \`
- Blancos: espacio, tabulador, salto de línea

Dentro de un texto (`"…"`) y de un comentario (`# …`) se admite cualquier carácter. Un carácter fuera de Σ produce un **error léxico**.

## 3. Componentes léxicos (tokens)

Abreviaturas: `L = [a-zA-Z_áéíóúÁÉÍÓÚñÑüÜ]`, `D = [0-9]`.

| Token | Expresión regular | Ejemplos |
|---|---|---|
| Palabras reservadas | `variable`, `si`, `entonces`, `sino`, `fin`, `mientras`, `hacer`, `para`, `desde`, `hasta`, `paso`, `funcion`, `función`, `retornar`, `verdadero`, `falso`, `nulo`, `y`, `o`, `no` | `mientras` |
| `ID` | `L (L ∪ D)*` | `x`, `total_2`, `año` |
| `NUMERO` | `D⁺ (. D⁺ ∪ λ)` | `42`, `3.14` |
| `TEXTO` | `" (c ∪ \x)* "`, con c ≠ `"`, `\`, salto de línea | `"hola"`, `"dijo \"sí\""` |
| Operadores relacionales | `== ∪ != ∪ <= ∪ >= ∪ < ∪ >` | `<=` |
| Operadores aritméticos | `+ ∪ - ∪ * ∪ / ∪ % ∪ ^` | `^` |
| Asignación | `=` | |
| Delimitadores | `( ∪ ) ∪ [ ∪ ] ∪ ,` | |
| `COMENTARIO` (se descarta) | `# (cualquier carácter salvo salto)*` | `# nota` |
| `ESPACIO` (se descarta) | `(espacio ∪ tab ∪ salto)⁺` | |

**Reglas de desempate del analizador léxico:**

1. **Coincidencia más larga.** `<=` es un solo token, no `<` seguido de `=`. `siempre` es un `ID`, no `si` seguido de `empre`.
2. **Prioridad por orden.** Si dos reglas reconocen la misma cadena con la misma longitud, gana la que aparece primero en la gramática. Por eso las palabras reservadas van antes que `ID`: `si` es `SI` y no `ID`.

Como consecuencia, una palabra reservada no puede usarse como nombre. Un caso típico es `y`: `variable y = 2` es un error de sintaxis, y el mensaje lo explica.

### 3.1 AFD de `ID`

M_ID = ({q0, q1}, Σ, δ, q0, {q1})

| δ | L | D | otro |
|---|---|---|---|
| → q0 | q1 | — | — |
| * q1 | q1 | q1 | — |

(— indica el estado sumidero.)

### 3.2 AFD de `NUMERO`

M_NUM = ({q0, q1, q2, q3}, Σ, δ, q0, {q1, q3})

| δ | D | `.` | otro |
|---|---|---|---|
| → q0 | q1 | — | — |
| * q1 | q1 | q2 | — |
| q2 | q3 | — | — |
| * q3 | q3 | — | — |

q2 no es de aceptación: `3.` no es un número válido.

ANTLR combina las ER de todos los tokens en una sola red de transiciones (ATN) y, al analizar, construye y guarda en caché los estados del AFD equivalente. Es la construcción ER → AFND → AFD vista en clase, hecha automáticamente.

## 4. Sintaxis: gramática libre de contexto

G = (V_N, V_T, P, S), donde:

- V_N son las reglas en minúscula de `gramatica/Llano.g4` (`programa`, `sentencia`, `expresion`, …).
- V_T son los tokens de la sección 3.
- S = `programa`.
- P está a continuación, en EBNF: `*` significa cero o más, `+` una o más, `?` opcional, `|` alternativa.

```ebnf
programa    → sentencia* EOF
bloque      → sentencia*
sentencia   → declaracion | asignacion | condicional | mientras | para
            | funcion | retorno | expresion

declaracion → 'variable' ID ( '=' expresion )?
asignacion  → ID indice* '=' expresion
condicional → 'si' expresion 'entonces' bloque
              ( 'sino' 'si' expresion 'entonces' bloque )*
              ( 'sino' bloque )?
              'fin'
mientras    → 'mientras' expresion 'hacer' bloque 'fin'
para        → 'para' ID 'desde' expresion 'hasta' expresion ( 'paso' expresion )?
              'hacer' bloque 'fin'
funcion     → 'funcion' ID '(' parametros? ')' bloque 'fin'
parametros  → ID ( ',' ID )*
retorno     → 'retornar' expresion

expresion   → disyuncion
disyuncion  → conjuncion ( 'o' conjuncion )*
conjuncion  → negacion ( 'y' negacion )*
negacion    → 'no' negacion | comparacion
comparacion → suma ( opRel suma )?
suma        → producto ( ('+' | '-') producto )*
producto    → unario ( ('*' | '/' | '%') unario )*
unario      → '-' unario | potencia
potencia    → postfijo ( '^' unario )?
postfijo    → primario ( llamada | indice )*
llamada     → '(' argumentos? ')'
argumentos  → expresion ( ',' expresion )*
indice      → '[' expresion ']'
primario    → NUMERO | TEXTO | 'verdadero' | 'falso' | 'nulo' | ID
            | '[' argumentos? ']' | '(' expresion ')'
```

Cada operador EBNF se puede reescribir como BNF pura, es decir, como producciones de una GLC estándar. Por ejemplo, `suma → producto ( '+' producto )*` equivale a:

```
suma  → producto suma'
suma' → '+' producto suma' | λ
```

### 4.1 Precedencia y ambigüedad

La gramática "natural" de expresiones, E → E + E | E * E | n, es **ambigua**: `2 + 3 * 4` tiene dos árboles de derivación distintos, uno que da 14 y otro que da 20. Llano evita la ambigüedad con **un no terminal por nivel de precedencia**. Un operador de menor precedencia queda más arriba en el árbol, así que se aplica después.

| Nivel (de menor a mayor) | Operadores | Asociatividad |
|---|---|---|
| `disyuncion` | `o` | izquierda |
| `conjuncion` | `y` | izquierda |
| `negacion` | `no` | prefijo |
| `comparacion` | `== != < > <= >=` | no asociativa (`a < b < c` es un error) |
| `suma` | `+ -` | izquierda |
| `producto` | `* / %` | izquierda |
| `unario` | `-` | prefijo |
| `potencia` | `^` | derecha (`2^3^2 = 2^9`) |
| `postfijo` | llamada `f(x)`, índice `l[i]` | izquierda |

Derivación por la izquierda de `2 + 3 * 4` (resumida en la parte de expresiones):

```
suma ⇒ producto + producto
     ⇒ 2 + producto
     ⇒ 2 + unario * unario
     ⇒ 2 + 3 * unario
     ⇒ 2 + 3 * 4
```

La multiplicación queda dentro del segundo `producto`, más abajo en el árbol, y por eso se evalúa primero. Se puede comprobar con:

```
python llano.py -e "variable x = 2 + 3 * 4" --arbol
```

El `^` se agrupa a la derecha porque su operando derecho vuelve a `unario` (la regla se llama a sí misma por la derecha). `-2^2` vale −4 porque `potencia` está por debajo de `unario`, igual que en matemáticas.

### 4.2 Otras decisiones de sintaxis

- **Sin separador de sentencias.** No hay `;` ni saltos de línea obligatorios: las palabras clave delimitan los bloques. Hay un caso límite: una expresión entre paréntesis al inicio de una línea se pega a la anterior como llamada (`f` en una línea y `(1)` en la siguiente se leen como `f(1)`).
- **`sino si`** encadena condiciones sin anidar otro `fin`. En el árbol, el `si` que sigue a `sino` pertenece al mismo `condicional`.
- **Emparejamiento de bloques.** Cuando falta un `fin`, Llano busca el bloque abierto con una pila: apila cada `si`, `mientras`, `para` o `funcion` y desapila con cada `fin`. Es la idea del autómata de pila aplicada al diagnóstico de errores.

## 5. Semántica estática (antes de ejecutar)

El análisis semántico recorre el árbol con una **tabla de símbolos** organizada por ámbitos encadenados:

```
nativo (imprimir, leer, …)
 └─ global
     ├─ función f (parámetros y variables locales)
     │   └─ bloque de un si / mientras / para
     └─ …
```

Reglas que revisa:

| Regla | Error si no se cumple |
|---|---|
| Todo nombre usado está declarado en el ámbito actual o en uno que lo contiene | `'x' no ha sido declarado` |
| No se declara dos veces un nombre en el mismo ámbito | `'a' ya fue declarada en este ámbito` |
| Los parámetros de una función tienen nombres distintos | `el parámetro 'a' está repetido` |
| No se asigna a una función ni se redefine una predefinida | `'f' es una función; no se le puede asignar un valor` |
| `retornar` solo aparece dentro de una función | `'retornar' solo puede usarse dentro de una función` |
| Una llamada a una función conocida usa la cantidad correcta de argumentos | `'f' recibe 2 argumentos, pero se le pasaron 1` |

Detalles:

- Cada bloque de `si`, `mientras` o `para` crea un ámbito. Una variable puede ocultar a otra del mismo nombre declarada afuera.
- La variable de un `para` se crea para el ciclo si no existía antes. Si ya existía, el ciclo la reutiliza.
- **Elevación de funciones:** las funciones de un bloque se registran antes de revisar el resto del bloque. Así se pueden usar antes de la línea donde están escritas y dos funciones pueden llamarse entre sí (recursión mutua).
- Se informan **todos** los errores semánticos juntos y el programa no se ejecuta si hay alguno.

Estas reglas son **dependientes del contexto**. El lenguaje { w c w | w ∈ Σ* }, que sirve de modelo para "declarar un nombre y luego usar el mismo nombre", no es libre de contexto. Por eso no se pueden incluir en la GLC y van en una fase aparte.

## 6. Semántica dinámica (ejecución)

### 6.1 Tipos

| Tipo | Valores | `tipo(v)` |
|---|---|---|
| número | enteros de tamaño arbitrario y reales (`3`, `3.5`) | `"número"` |
| texto | cadenas Unicode | `"texto"` |
| lógico | `verdadero`, `falso` | `"lógico"` |
| nulo | `nulo` | `"nulo"` |
| lista | secuencias mutables `[1, "a", [2]]` | `"lista"` |
| función | definidas por el usuario o predefinidas | `"función"` |

Llano tiene **tipado dinámico**: los tipos se revisan al ejecutar. También es **fuerte**: no hay conversiones implícitas, salvo la concatenación con texto.

### 6.2 Operadores

| Operación | Tipos válidos | Resultado |
|---|---|---|
| `a + b` | número + número | suma |
| | texto + cualquiera, cualquiera + texto | concatenación (el otro operando se convierte a texto) |
| | lista + lista | concatenación de listas |
| `a - b`, `a * b`, `a % b` | números | aritmética |
| `t * n`, `n * t` | texto y entero n ≥ 0 | potencia de una cadena: tⁿ |
| `a / b` | números, b ≠ 0 | entero si la división es exacta; si no, real |
| `a ^ b` | números | potencia |
| `==`, `!=` | cualquiera | valores de tipos distintos nunca son iguales (`1 == "1"` es falso) |
| `< > <= >=` | número con número o texto con texto | orden numérico u orden lexicográfico |
| `y`, `o`, `no` | lógicos | evaluación en cortocircuito |
| `l[i]` | lista o texto, i entero, 0 ≤ i < longitud | elemento o carácter |

Las condiciones de `si` y `mientras` deben ser de tipo lógico. Así se evitan errores como confundir `=` con `==`.

### 6.3 Funciones

- Los parámetros se pasan por valor. Las listas se comparten (como en Python o Java).
- Una función sin `retornar` devuelve `nulo`.
- Las funciones son valores: se pueden guardar en variables y pasar como argumentos.
- Una función recuerda el ámbito donde se definió (es un **cierre** o *closure*). Ver la prueba `test_cierres`.
- El límite de llamadas anidadas es 3000. Superarlo produce un error que sugiere una recursión sin caso base.

### 6.4 Funciones predefinidas

| Función | Descripción |
|---|---|
| `imprimir(v1, v2, …)` | Muestra los valores separados por un espacio |
| `leer(mensaje?)` | Lee una línea del teclado; devuelve texto |
| `numero(t)` | Convierte un texto en número |
| `texto(v)` | Convierte un valor en texto |
| `entero(x)` | Parte entera |
| `longitud(x)` | Longitud \|w\| de un texto o tamaño de una lista |
| `agregar(l, v)` | Agrega `v` al final de la lista `l` |
| `quitar(l, i?)` | Quita y devuelve el último elemento, o el de la posición `i` |
| `invertir(x)` | Reflexión w⁻¹ de un texto, o lista invertida |
| `subcadena(t, i, j?)` | Subcadena con las posiciones de i a j − 1 |
| `tipo(v)` | Nombre del tipo |
| `raiz(x)`, `absoluto(x)`, `redondear(x, d?)`, `aleatorio(a, b)` | Matemáticas (`redondear` usa el redondeo escolar: 2.5 → 3) |

## 7. Relación con los contenidos del curso

| Contenido del curso | Dónde aparece en Llano |
|---|---|
| Alfabetos, cadenas, longitud, concatenación, potencia, reflexión, prefijos, sufijos (Unidad 1) | Alfabeto Σ del lenguaje; tipo texto con `longitud`, `+`, `*`, `invertir`, `subcadena`; ejemplo `07_cadenas.llano` |
| Operaciones con lenguajes: unión, concatenación, estrella de Kleene (Unidad 1) | Construcción de las ER de los tokens; Σᵏ en `07_cadenas.llano` |
| Expresiones regulares (Unidad 2) | Definición de cada token (sección 3) |
| AFD y AFND, equivalencia (Unidad 2) | AFD de `ID` y `NUMERO`; ANTLR convierte las ER en AFD; simulador en `08_automata_afd.llano` |
| Máquinas de Mealy y Moore (Unidad 2) | `09_traductor_mealy.llano`. El analizador léxico es un traductor: lee caracteres y emite tokens |
| Gramáticas libres de contexto, BNF, árbol de derivación, ambigüedad | Gramática `Llano.g4`, `--arbol`, precedencia por niveles (sección 4.1) |
| Autómatas de pila | El análisis sintáctico de una GLC necesita una pila (en el parser, la pila de llamadas); emparejamiento de `fin` (sección 4.2) |
| Máquinas de Turing, computabilidad | `10_maquina_turing.llano`: Llano simula una MT, así que es **Turing completo** (sección 8) |

## 8. Computabilidad

Llano es **Turing completo**. Tiene enteros sin límite, listas que crecen sin límite (la cinta), ciclos `mientras` que pueden no terminar y condicionales, así que puede simular cualquier máquina de Turing. El ejemplo `10_maquina_turing.llano` lo hace con una MT que reconoce { aⁿbⁿ | n ≥ 1 }.

Una consecuencia es que el **problema de la parada** es indecidible para programas Llano: ningún análisis puede decidir, para todo programa, si terminará. Por eso el análisis semántico no intenta detectar ciclos infinitos. Solo revisa propiedades decidibles, como las declaraciones y la cantidad de argumentos.

## 9. Limitaciones conocidas

- No hay `romper` ni `continuar` en los ciclos.
- No hay diccionarios ni registros; se usan listas.
- Los textos no se pueden modificar por posición (`t[0] = "x"` es un error).
- Los errores de tipo se detectan al ejecutar, no antes (tipado dinámico).
- El intérprete recorre el árbol de derivación de ANTLR directamente. Es sencillo de seguir, pero más lento que un intérprete con árbol de sintaxis abstracta (AST) o código intermedio.
