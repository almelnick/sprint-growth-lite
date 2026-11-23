#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pruebas. Correr con:  python3 -m unittest discover -s tests -v"""
import os
import sys
import unittest

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "scripts"))
import economia as e  # noqa: E402


class Economia(unittest.TestCase):
    def test_caso_base(self):
        r = e.calcular(58000, 2.2, 0.55, 29675)
        self.assertAlmostEqual(r["clv"], 70180)
        self.assertEqual(e.ratio(r["ltv_cac"]), "2,4x")
        self.assertEqual(r["estado"], "ajustado")

    def test_sensibilidad(self):
        s = e.calcular(58000, 2.2, 0.55, 29675)["sensibilidad"]
        self.assertEqual(e.ratio(s["cac_menos_20"]), "3,0x")
        self.assertEqual(e.ratio(s["mas_03_compras"]), "2,7x")
        self.assertEqual(e.ratio(s["ambas"]), "3,4x")

    def test_cac_maximo_y_recuperacion(self):
        r = e.calcular(58000, 2.2, 0.55, 29675)
        self.assertAlmostEqual(r["cac_maximo"], 70180 / 3)
        self.assertAlmostEqual(r["compras_para_recuperar"], 29675 / 31900)

    def test_rechaza_datos_imposibles(self):
        with self.assertRaises(ValueError):
            e.calcular(58000, 2.2, 55, 29675)
        with self.assertRaises(ValueError):
            e.calcular(58000, 0, 0.55, 29675)
        with self.assertRaises(ValueError):
            e.calcular(58000, 2.2, 0.55, None)

    def test_formato_chileno(self):
        self.assertEqual(e.pesos(1234567), "$1.234.567")

    def test_cli(self):
        self.assertEqual(e.main(["--ticket", "58000", "--compras", "2.2", "--margen", "0.55", "--cac", "29675"]), 0)
        self.assertEqual(e.main(["--ticket", "0", "--compras", "2.2", "--margen", "0.55", "--cac", "1"]), 2)


if __name__ == "__main__":
    unittest.main()
