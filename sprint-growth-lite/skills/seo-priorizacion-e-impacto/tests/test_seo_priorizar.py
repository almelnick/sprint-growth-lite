#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pruebas. Correr con:  python3 -m unittest discover -s tests -v"""
import os
import sys
import tempfile
import unittest

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "scripts"))
import seo_priorizar as p  # noqa: E402

PLANTILLA = os.path.join(RAIZ, "templates", "actions.csv")


def csv_tmp(texto):
    f = tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False, encoding="utf-8")
    f.write(texto)
    f.close()
    return f.name


class Priorizar(unittest.TestCase):
    def test_orden_por_puntaje(self):
        acc, av = p.cargar(PLANTILLA)
        self.assertEqual(av, [])
        self.assertEqual(acc[0]["accion"], "Agregar JSON-LD de producto")  # 2*0.8/1 = 1.6
        self.assertAlmostEqual(acc[0]["puntaje"], 1.6)
        self.assertEqual([a["puntaje"] for a in acc], sorted((a["puntaje"] for a in acc), reverse=True))

    def test_rango_nunca_cifra_unica(self):
        acc, _ = p.cargar(PLANTILLA)
        canon = next(a for a in acc if a["accion"].startswith("Corregir canonicals"))
        lo, hi, vlo, vhi = canon["rango"]
        self.assertEqual((lo, hi), (160.0, 480.0))
        self.assertEqual((vlo, vhi), (160 * 420, 480 * 420))

    def test_sin_datos_de_clics_no_hay_estimacion(self):
        acc, _ = p.cargar(PLANTILLA)
        nueva = next(a for a in acc if a["accion"].startswith("Crear página"))
        self.assertIsNone(nueva["rango"])

    def test_filas_invalidas_se_avisan(self):
        ruta = csv_tmp("accion,impacto,confianza,esfuerzo_dias\nA,9,0.5,1\nB,3,1.5,1\nC,3,0.5,0\n,3,0.5,1\nD,3,0.5,2\n")
        acc, av = p.cargar(ruta)
        self.assertEqual([a["accion"] for a in acc], ["D"])
        self.assertEqual(len(av), 4)

    def test_min_mayor_que_max_se_intercambia(self):
        ruta = csv_tmp("accion,impacto,confianza,esfuerzo_dias,clics_mes_actuales,mejora_pct_min,mejora_pct_max\nA,3,0.5,1,1000,20,10\n")
        acc, av = p.cargar(ruta)
        self.assertEqual(acc[0]["rango"][:2], (100.0, 200.0))
        self.assertTrue(any("se intercambian" in x for x in av))

    def test_formato_chileno_y_punto_y_coma(self):
        ruta = csv_tmp("accion;impacto;confianza;esfuerzo_dias;clics_mes_actuales;mejora_pct_min;mejora_pct_max;valor_por_clic\nA;3;0,5;2;12.000;5%;10%;$1.200\n")
        acc, _ = p.cargar(ruta)
        self.assertEqual(acc[0]["clics"], 12000)
        self.assertEqual(acc[0]["valor"], 1200)

    def test_render_y_cli(self):
        self.assertIn("rango, no promesa", p.render(*p.cargar(PLANTILLA)))
        self.assertEqual(p.main(["--acciones", PLANTILLA, "--salida", os.devnull]), 0)
        self.assertEqual(p.main(["--acciones", "/no/existe.csv"]), 2)


if __name__ == "__main__":
    unittest.main()
