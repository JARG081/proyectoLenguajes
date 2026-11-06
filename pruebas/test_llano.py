"""Pruebas de Llano. Ejecutar desde la carpeta del proyecto con:

    python -m unittest discover -s pruebas -v
"""

import os
import sys
import unittest

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, RAIZ)

from llano import ErrorLlano, ErroresLlano, ejecutar, verificar  # noqa: E402
from llano.analisis import analizar, analizar_lexico, arbol_texto  # noqa: E402
from llano.generado.LlanoLexer import LlanoLexer  # noqa: E402


def correr(codigo, entradas=()):
    """Ejecuta código y devuelve las líneas impresas."""
    salida = []
    pendientes = list(entradas)
    ejecutar(codigo, salida=salida.append, entrada=lambda _: pendientes.pop(0))
    return salida


def error_de(codigo):
    """Devuelve (fase, mensaje, línea) del primer error del programa."""
    try:
        correr(codigo)
    except ErroresLlano as e:
        primero = e.errores[0]
        return primero.fase, primero.mensaje, primero.linea
    except ErrorLlano as e:
        return e.fase, e.mensaje, e.linea
    raise AssertionError("se esperaba un error")


class PruebasLexico(unittest.TestCase):
    def tipos(self, codigo):
        return [LlanoLexer.symbolicNames[t.type] for t in analizar_lexico(codigo).tokens][:-1]

    def test_palabras_reservadas_antes_que_identificadores(self):
        self.assertEqual(self.tipos("si sino siempre fin final"),
                         ["SI", "SINO", "ID", "FIN", "ID"])

    def test_numeros_textos_y_operadores(self):
        self.assertEqual(self.tipos('x <= 3.14 "hola" == != ^'),
                         ["ID", "MENORIGUAL", "NUMERO", "TEXTO", "IGUAL", "DIFERENTE", "POT"])

    def test_identificadores_con_tildes_y_enie(self):
        self.assertEqual(self.tipos("año canción función funcion"), ["ID", "ID", "FUNCION", "FUNCION"])

    def test_comentarios_y_espacios_se_ignoran(self):
        self.assertEqual(self.tipos("x # comentario\n  y"), ["ID", "Y"])

    def test_caracter_fuera_del_alfabeto(self):
        fase, mensaje, linea = error_de("variable x = 1\nx = 2 $ 3")
        self.assertEqual((fase, linea), ("lexico", 2))
        self.assertIn("'$'", mensaje)

    def test_texto_sin_cerrar(self):
        fase, mensaje, _ = error_de('imprimir("hola)')
        self.assertEqual(fase, "lexico")
        self.assertIn("sin cerrar", mensaje)


class PruebasSintaxis(unittest.TestCase):
    def test_precedencia_en_el_arbol(self):
        # 2 + 3 * 4: la multiplicación queda más abajo en el árbol (se hace primero)
        arbol = arbol_texto(analizar("variable x = 2 + 3 * 4"))
        self.assertLess(arbol.index("suma"), arbol.index("producto"))

    def test_falta_fin(self):
        fase, mensaje, linea = error_de("variable x = 1\nsi x > 0 entonces\n  imprimir(x)\n")
        self.assertEqual((fase, linea), ("sintactico", 2))
        self.assertIn("falta el 'fin'", mensaje)

    def test_fin_de_mas(self):
        fase, mensaje, _ = error_de("mientras falso hacer fin fin")
        self.assertEqual(fase, "sintactico")
        self.assertIn("sobra 'fin'", mensaje)

    def test_palabra_reservada_como_nombre(self):
        fase, mensaje, _ = error_de("variable y = 3")
        self.assertEqual(fase, "sintactico")
        self.assertIn("palabra reservada", mensaje)

    def test_sino_si_no_requiere_fin_extra(self):
        self.assertEqual(correr("variable n = 5\nsi n < 0 entonces imprimir(1)\n"
                                "sino si n < 10 entonces imprimir(2)\nsino imprimir(3) fin"), ["2"])


class PruebasSemantica(unittest.TestCase):
    def test_variable_no_declarada(self):
        fase, mensaje, _ = error_de("x = 5")
        self.assertEqual(fase, "semantico")
        self.assertIn("no ha sido declarada", mensaje)

    def test_redeclaracion_en_el_mismo_ambito(self):
        self.assertEqual(error_de("variable a = 1\nvariable a = 2")[0], "semantico")

    def test_retornar_fuera_de_funcion(self):
        self.assertEqual(error_de("retornar 1")[0], "semantico")

    def test_cantidad_de_argumentos(self):
        fase, mensaje, _ = error_de("funcion f(a, b) retornar a fin\nimprimir(f(1))")
        self.assertEqual(fase, "semantico")
        self.assertIn("recibe 2 argumentos", mensaje)

    def test_reporta_todos_los_errores_semanticos(self):
        with self.assertRaises(ErroresLlano) as ctx:
            verificar("a = 1\nimprimir(b)\nretornar 3")
        self.assertEqual(len(ctx.exception.errores), 3)

    def test_no_ejecuta_si_hay_error_semantico(self):
        salida = []
        with self.assertRaises(ErroresLlano):
            ejecutar('imprimir("antes")\nz = 1', salida=salida.append)
        self.assertEqual(salida, [])

    def test_funciones_elevadas_y_recursion_mutua(self):
        codigo = """
        imprimir(es_par(10), es_par(7))
        funcion es_par(n) si n == 0 entonces retornar verdadero fin retornar es_impar(n - 1) fin
        funcion es_impar(n) si n == 0 entonces retornar falso fin retornar es_par(n - 1) fin
        """
        self.assertEqual(correr(codigo), ["verdadero falso"])

    def test_ambito_de_bloque(self):
        codigo = "variable x = 1\nsi verdadero entonces variable x = 2 imprimir(x) fin\nimprimir(x)"
        self.assertEqual(correr(codigo), ["2", "1"])
        self.assertEqual(error_de("si verdadero entonces variable t = 1 fin\nimprimir(t)")[0], "semantico")


class PruebasEjecucion(unittest.TestCase):
    def test_aritmetica(self):
        self.assertEqual(correr("imprimir(7 / 2, 8 / 2, 7 % 3, 2 ^ 3 ^ 2, -2 ^ 2, 2 + 3 * 4)"),
                         ["3.5 4 1 512 -4 14"])

    def test_enteros_grandes(self):
        self.assertEqual(correr("imprimir(2 ^ 100)"), [str(2 ** 100)])

    def test_textos(self):
        self.assertEqual(correr('imprimir("ab" * 3, "n=" + 5, longitud("año"), invertir("abc"))'),
                         ["ababab n=5 3 cba"])

    def test_comparaciones_y_logica(self):
        self.assertEqual(correr('imprimir(1 == 1.0, "a" < "b", 1 == "1", no falso o falso y falso)'),
                         ["verdadero verdadero falso verdadero"])

    def test_cortocircuito(self):
        # si 'o' evaluara la derecha, la división por cero produciría un error
        self.assertEqual(correr("imprimir(verdadero o 1 / 0 == 1)"), ["verdadero"])

    def test_ciclos(self):
        self.assertEqual(correr("para i desde 1 hasta 3 hacer imprimir(i) fin"), ["1", "2", "3"])
        self.assertEqual(correr("para i desde 6 hasta 1 paso -2 hacer imprimir(i) fin"), ["6", "4", "2"])
        self.assertEqual(correr("para i desde 0 hasta -1 hacer imprimir(i) fin"), [])
        self.assertEqual(correr("variable n = 3\nmientras n > 0 hacer imprimir(n) n = n - 1 fin"),
                         ["3", "2", "1"])

    def test_declarar_dentro_de_un_ciclo(self):
        self.assertEqual(correr("para i desde 1 hasta 2 hacer variable c = i * 10 imprimir(c) fin"),
                         ["10", "20"])

    def test_recursion(self):
        codigo = "funcion f(n) si n <= 1 entonces retornar 1 fin retornar n * f(n - 1) fin\nimprimir(f(200) > 0)"
        self.assertEqual(correr(codigo), ["verdadero"])

    def test_cierres(self):
        codigo = """
        funcion contador()
            variable c = 0
            funcion siguiente()
                c = c + 1
                retornar c
            fin
            retornar siguiente
        fin
        variable s = contador()
        s()
        s()
        imprimir(s())
        """
        self.assertEqual(correr(codigo), ["3"])

    def test_listas(self):
        codigo = "variable l = [1, [2, 3]]\nl[1][0] = 9\nagregar(l, \"x\")\nimprimir(l, longitud(l))"
        self.assertEqual(correr(codigo), ['[1, [9, 3], "x"] 3'])

    def test_leer(self):
        self.assertEqual(correr("variable n = numero(leer())\nimprimir(n * 2)", ["21"]), ["42"])

    def test_errores_de_ejecucion(self):
        casos = {
            "imprimir(1 / 0)": "división por cero",
            "si 1 entonces fin": "debe ser verdadero o falso",
            "imprimir([1][3])": "fuera de rango",
            'imprimir("a" - 1)': "no se puede aplicar '-'",
            "funcion f(n) retornar f(n) fin\nf(1)": "demasiadas llamadas",
            'imprimir(numero("x"))': "no es un número válido",
            "para i desde 1 hasta 3 paso 0 hacer fin": "no puede ser 0",
        }
        for codigo, esperado in casos.items():
            with self.subTest(codigo=codigo):
                fase, mensaje, _ = error_de(codigo)
                self.assertEqual(fase, "ejecucion")
                self.assertIn(esperado, mensaje)


class PruebasPistas(unittest.TestCase):
    """Los mensajes de error orientan al principiante (regresión de las pruebas de uso)."""

    def test_pistas(self):
        casos = {
            "variable x = 5\nsi x = 5 entonces fin": "se usa '=='",
            "variable i = 0\nmientra i < 3 hacer fin": "¿quisiste escribir 'mientras'",
            "Si verdadero entonces fin": "escribe 'si'",
            "funcion f()\n retornar\nfin": "retornar nulo",
            "imprimir(3 ** 2)": "se usa '^'",
            "imprimir(verdadero && falso)": "la palabra y",
            "variable x = 1;": "no usa ';'",
            "imprimir('hola')": "comillas dobles",
            "variable total = 1\ntotl = 2": "¿quisiste decir 'total'?",
            "imprimi(1)": "¿quisiste decir 'imprimir'?",
            "funcion f() retorna 1 fin": "palabra clave 'retornar'",
            "imprimir((1)": "antes del final",
        }
        for codigo, pista in casos.items():
            with self.subTest(codigo=codigo):
                self.assertIn(pista, error_de(codigo)[1])

    def test_un_solo_error_por_caracter_repetido(self):
        with self.assertRaises(ErroresLlano) as ctx:
            verificar("imprimir(verdadero && falso)")
        self.assertEqual(len(ctx.exception.errores), 1)


class PruebasCasosLimite(unittest.TestCase):
    def test_leer_sin_datos_es_error_de_llano(self):
        def sin_datos(_):
            raise EOFError
        with self.assertRaises(ErrorLlano) as ctx:
            ejecutar("leer()", salida=lambda _: None, entrada=sin_datos)
        self.assertIn("no recibió datos", ctx.exception.mensaje)

    def test_redondeo_escolar(self):
        self.assertEqual(correr("imprimir(redondear(2.5), redondear(-2.5), redondear(3.14159, 2))"),
                         ["3 -3 3.14"])

    def test_enteros_de_mas_de_4300_digitos(self):
        codigo = "funcion f(n) si n <= 1 entonces retornar 1 fin retornar n * f(n - 1) fin\n" \
                 "imprimir(longitud(texto(f(2000))))"
        self.assertEqual(correr(codigo), ["5736"])

    def test_texto_demasiado_grande(self):
        self.assertIn("demasiado grande", error_de('imprimir("ab" * 6000000)')[1])

    def test_archivo_vacio_y_solo_comentarios(self):
        self.assertEqual(correr(""), [])
        self.assertEqual(correr("# nada\n# que hacer"), [])


class PruebasEjemplos(unittest.TestCase):
    """Todos los ejemplos se ejecutan sin errores y dan los resultados esperados."""

    CARPETA = os.path.join(RAIZ, "ejemplos")

    def correr_ejemplo(self, nombre, entradas=()):
        with open(os.path.join(self.CARPETA, nombre), encoding="utf-8") as f:
            return correr(f.read(), entradas)

    def test_todos_los_ejemplos(self):
        for nombre in sorted(os.listdir(self.CARPETA)):
            if nombre.endswith(".llano") and nombre != "11_calculadora.llano":
                with self.subTest(ejemplo=nombre):
                    self.assertTrue(self.correr_ejemplo(nombre))

    def test_resultados_clave(self):
        self.assertIn("mcd(1071, 462) = 21", self.correr_ejemplo("04_ciclos.llano"))
        self.assertIn("|Σ³| = 8 = 2³", self.correr_ejemplo("07_cadenas.llano"))
        afd = self.correr_ejemplo("08_automata_afd.llano")
        self.assertEqual(afd.count("  ACEPTADA"), 3)
        mt = self.correr_ejemplo("10_maquina_turing.llano")
        self.assertIn("aaabbb -> verdadero", mt)
        self.assertIn("abab -> falso", mt)

    def test_calculadora(self):
        salida = self.correr_ejemplo("11_calculadora.llano", ["*", "6", "7", "fin"])
        self.assertIn("Resultado: 42", salida)

    def test_ejemplos_de_errores(self):
        fases = ["lexico", "sintactico", "semantico", "ejecucion"]
        archivos = sorted(os.listdir(os.path.join(self.CARPETA, "errores")))
        self.assertEqual(len(archivos), 4)
        for archivo, fase in zip(archivos, fases):
            with self.subTest(archivo=archivo):
                with open(os.path.join(self.CARPETA, "errores", archivo), encoding="utf-8") as f:
                    self.assertEqual(error_de(f.read())[0], fase)


if __name__ == "__main__":
    unittest.main()
