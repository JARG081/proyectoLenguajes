# Plan del proyecto final: Llano

## 1. Qué se evalúa

La rúbrica (`RÚBRICA PARA EVALUAR PROYECTO FINAL DE CURSO.pdf`) califica **el informe y la sustentación**, no el software como tal. El intérprete entra como **evidencia** en la metodología y los resultados del informe, y como **demostración** en la sustentación.

| Bloque | Criterio | Nivel Excelente (4.0–5.0) | Cómo lo cubre este proyecto |
|---|---|---|---|
| Informe | Contenido y rigor | Información precisa, bien investigada, con lenguaje técnico | Especificación formal (`docs/especificacion.md`): ER, AFD, GLC, precedencia, semántica, computabilidad. Resultados medibles: pruebas, ejemplos, errores por fase |
| Informe | Estructura y organización | Título, Autores, Resumen ejecutivo, Introducción, Marco teórico, Metodología, Resultados, Discusión, Conclusiones, Referencias; tabla de contenido; **norma del profesor** | Esquema de la sección 3 de este plan |
| Informe | Estilo y presentación | Escritura clara, citas **actualizadas** y suficientes en la norma pedida, presentación visual profesional | Bibliografía clásica más fuentes recientes; figuras numeradas (árboles, AFD, arquitectura, capturas) |
| Sustentación | Claridad y organización | Estructura lógica, **se respeta el tiempo**, hilo conductor | Guion con tiempos (sección 4) y ensayos cronometrados |
| Sustentación | Comunicación y enganche | Presentación dinámica y **elementos creativos** | Demo en vivo: el público propone un programa o un error y Llano lo analiza en directo |
| Sustentación | Dominio del tema y preguntas | Respuestas precisas y seguras | Banco de preguntas (sección 5) y dominio de cada fase del código |

> **Pendiente de confirmar con la profesora:** la rúbrica dice "siguiendo la norma establecida por el profesor para trabajos escritos", pero no la nombra. Mientras tanto se usa **APA 7**. También hay que confirmar la fecha de entrega, la duración de la sustentación y si el trabajo es individual o en grupo.

## 2. Estado del software

| Parte | Estado |
|---|---|
| Gramática ANTLR (léxico + GLC) | ✅ `gramatica/Llano.g4` |
| Variables, tipos, operadores con precedencia | ✅ |
| `si` / `sino si` / `sino`, `mientras`, `para … paso` | ✅ |
| Funciones, recursión, cierres, elevación | ✅ |
| Listas y textos con operaciones de la Unidad 1 | ✅ |
| Análisis semántico con tabla de símbolos por ámbitos | ✅ |
| Errores en español por fase, con línea, columna, marca y pistas para errores típicos | ✅ |
| `--tokens`, `--arbol`, `--dot`, `--verificar`, modo interactivo | ✅ |
| 11 ejemplos y 4 ejemplos de error | ✅ |
| Pruebas unitarias (43) y 55 casos de uso de punta a punta | ✅ `probar.bat` |
| Opcional: `romper` / `continuar` | ⏳ si sobra tiempo |
| Opcional: editor web o resaltado de sintaxis para VS Code | ⏳ solo si sobra tiempo; no suma en la rúbrica |

**Recomendación:** congelar el código pronto y dedicar el tiempo restante al informe y a la sustentación, que son lo que se califica.

## 3. Esquema del informe

| Sección | Contenido | Material de base |
|---|---|---|
| Portada | Título ("Llano: diseño e implementación de un lenguaje de programación en español con ANTLR"), autores, curso, profesora, fecha | — |
| Tabla de contenido | Automática en Word | — |
| Resumen ejecutivo | ~200 palabras: problema, qué se hizo, resultados (cobertura del curso, pruebas superadas), conclusión principal | Al final |
| 1. Introducción | Motivación: barrera del inglés al aprender a programar; lenguajes en español existentes (PSeInt, Latino); objetivo general y específicos; alcance | — |
| 2. Marco teórico | Alfabetos y cadenas; lenguajes y operaciones; ER; AFD y AFND; GLC, BNF, árboles de derivación y ambigüedad; autómatas de pila; MT y computabilidad; fases de un compilador o intérprete; ANTLR y el análisis ALL(*) | Diapositivas del curso, Hopcroft, Aho, Parr |
| 3. Metodología | Diseño del lenguaje (decisiones y por qué); especificación léxica (tabla de ER y AFD); gramática (EBNF y precedencia); arquitectura por fases; análisis semántico; intérprete (patrón Visitor); estrategia de pruebas | `docs/especificacion.md`, `README.md` |
| 4. Resultados | Programas de ejemplo con su salida; tokens y árbol de derivación de un ejemplo (figuras); un ejemplo de error por fase; resultados de las pruebas; ejemplos que conectan con el curso (AFD, Mealy/Moore, MT) | `ejemplos/`, `--tokens`, `--arbol`, `--dot` |
| 5. Discusión | Comparación con PSeInt y Python; por qué la semántica no cabe en la GLC; Turing completitud e indecidibilidad del problema de la parada; limitaciones; trabajo futuro | Secciones 1, 5, 8 y 9 de la especificación |
| 6. Conclusiones | 4 o 5 conclusiones ligadas a los objetivos específicos | — |
| Referencias | En la norma pedida; incluir fuentes de 2019 en adelante | Ver sección 6 |
| Anexos | Gramática completa; manual de usuario breve | `Llano.g4`, `README.md` |

**Figuras sugeridas:** diagrama de fases (pipeline), AFD de `ID` y `NUMERO`, árbol de derivación de `2 + 3 * 4` (con `--dot` y Graphviz Online), captura de un error con su marca, traza de la MT aⁿbⁿ.

## 4. Guion de la sustentación (ajustar al tiempo asignado; ejemplo para 15 minutos)

| Minutos | Bloque | Contenido |
|---|---|---|
| 0–1 | Gancho | Mostrar `para i desde 1 hasta 5 hacer imprimir(i) fin` y preguntar: "¿qué hace falta para que el computador entienda esto?" |
| 1–3 | Problema y objetivo | Por qué un lenguaje en español; qué se propuso |
| 3–7 | De la teoría al código | Las fases como la jerarquía de Chomsky: ER/AFD → tokens (`--tokens`), GLC → árbol (`--arbol`), semántica → tabla de símbolos |
| 7–11 | Demo en vivo | Ejecutar ejemplos; el público dicta un error y se ve en qué fase lo detecta Llano; cerrar con la MT aⁿbⁿ escrita en Llano |
| 11–13 | Resultados y discusión | Pruebas, cobertura del curso, Turing completitud, limitaciones |
| 13–15 | Conclusiones y preguntas | — |

Plan B: grabar un video corto de la demo por si falla el equipo.

## 5. Banco de preguntas probables

1. **¿Por qué ANTLR y no un parser hecho a mano?** Porque la gramática queda como especificación formal y ejecutable, y ANTLR se usó en el Laboratorio 7. El precio es depender de una herramienta; a cambio se puede mostrar la GLC exacta.
2. **¿Qué tipo de parser genera ANTLR?** Descendente, ALL(*) (LL adaptativo), con predicción dinámica. No admite recursión izquierda indirecta. La directa sí la admite, pero en Llano la precedencia se escribió por niveles.
3. **¿Cómo resolvieron la ambigüedad de las expresiones?** Con un no terminal por nivel de precedencia; mostrar el árbol de `2 + 3 * 4`.
4. **¿Por qué `y` no puede ser un nombre de variable?** Por la regla de prioridad del léxico: las palabras reservadas van antes que `ID`.
5. **¿Por qué la comprobación de variables declaradas no está en la gramática?** Porque es una restricción dependiente del contexto (modelo { w c w }), que no es libre de contexto.
6. **¿Es Turing completo?** Sí: simula una MT (ejemplo 10). Por eso detectar ciclos infinitos es indecidible.
7. **¿Dónde está el autómata de pila?** Toda GLC necesita una pila para reconocerse; en el parser es la pila de llamadas de las funciones recursivas. También se usa una pila explícita para encontrar el `fin` faltante.
8. **¿Compilador o intérprete?** Intérprete de recorrido de árbol; no genera código máquina.
9. **¿Qué pasa con `1 == "1"`?** Es falso: el tipado es fuerte y no hay conversiones implícitas en la igualdad.

## 6. Referencias de partida (completar y pasar a la norma definitiva)

- Aho, A. V., Lam, M. S., Sethi, R. y Ullman, J. D. (2008). *Compiladores: principios, técnicas y herramientas* (2.ª ed.). Pearson.
- Hopcroft, J. E., Motwani, R. y Ullman, J. D. (2007). *Introducción a la teoría de autómatas, lenguajes y computación* (3.ª ed.). Pearson.
- De Castro Korgi, R. (2004). *Teoría de la computación: lenguajes, autómatas, gramáticas*. Universidad Nacional de Colombia.
- Parr, T. (2013). *The definitive ANTLR 4 reference*. The Pragmatic Bookshelf.
- Parr, T., Harwell, S. y Fisher, K. (2014). Adaptive LL(*) parsing: The power of dynamic analysis. *ACM SIGPLAN Notices, 49*(10), 579–598.
- Nystrom, R. (2021). *Crafting interpreters*. Genever Benning.
- Cardona Román, D. M. (s. f.). Diapositivas del curso Lenguajes de Programación. Universidad de los Llanos.
- Pendiente: 2 o 3 artículos recientes (2019 en adelante) sobre lenguajes de programación en la lengua materna y aprendizaje de la programación.

## 7. Próximos pasos

1. Confirmar con la profesora la norma, la fecha, la duración de la sustentación y si es individual o en grupo.
2. Probar la instalación en el computador donde se va a sustentar (`instalar.bat`).
3. Redactar el informe siguiendo la sección 3.
4. Preparar las diapositivas y ensayar con cronómetro al menos tres veces.
