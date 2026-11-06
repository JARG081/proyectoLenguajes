"""Ejecuta los casos de uso de punta a punta dentro de unittest."""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import casos_de_uso  # noqa: E402


class PruebasCasosDeUso(unittest.TestCase):
    def test_casos_de_uso(self):
        for titulo, casos in casos_de_uso.GRUPOS:
            for c in casos:
                with self.subTest(grupo=titulo, caso=c["id"], nombre=c["nombre"]):
                    paso, detalle, todo, _ = casos_de_uso.ejecutar_caso(c)
                    self.assertTrue(paso, f"{detalle}\n{todo}")


if __name__ == "__main__":
    unittest.main()
