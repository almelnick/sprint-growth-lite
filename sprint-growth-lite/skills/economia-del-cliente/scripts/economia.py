#!/usr/bin/env python3
# © Alan Melnick · alanmelnick.com. All rights reserved. Distribution without written authorization is prohibited.
# -*- coding: utf-8 -*-
"""economia.py - Economía del cliente: CLV, LTV:CAC, recuperación y sensibilidad (Sprint Latam).

Responde una pregunta: ¿qué mano del número conviene mover, el CAC o el CLV?

Uso:
  python3 economia.py --ticket 58000 --compras 2.2 --margen 0.55 --cac 29675 [--objetivo 3] [--json]

Fórmulas:
  CLV (ganancia)  = ticket x compras por cliente x margen de contribución
  LTV:CAC         = CLV / CAC          (sano: 3x o más)
  CAC máximo      = CLV / objetivo     (lo más que se puede pagar por un cliente y seguir en el objetivo)
  Recuperación    = CAC / (ticket x margen)   (compras necesarias para recuperar lo invertido)
Sensibilidad: CAC -20%, +0,3 compras por cliente, y ambas a la vez.
"""
import argparse
import json
import sys


def pesos(x):
    return "$" + f"{round(x):,}".replace(",", ".")


def ratio(x):
    return f"{x:.1f}".replace(".", ",") + "x"


def calcular(ticket, compras, margen, cac, objetivo=3.0):
    for nombre, v in (("ticket", ticket), ("compras", compras), ("margen", margen), ("cac", cac)):
        if v is None or v <= 0:
            raise ValueError(f"'{nombre}' debe ser un número mayor que cero")
    if margen > 1:
        raise ValueError("el margen va como fracción entre 0 y 1 (ej. 0.55)")
    ganancia_compra = ticket * margen
    clv = ganancia_compra * compras
    base = clv / cac

    def esc(cac_x, compras_x):
        return ganancia_compra * compras_x / cac_x

    sens = {
        "base": base,
        "cac_menos_20": esc(cac * 0.8, compras),
        "mas_03_compras": esc(cac, compras + 0.3),
        "ambas": esc(cac * 0.8, compras + 0.3),
    }
    # Con las dos palancas aisladas, la más barata de mover es la de mayor salto.
    salto_cac = sens["cac_menos_20"] - base
    salto_clv = sens["mas_03_compras"] - base
    return {
        "ticket": ticket, "compras": compras, "margen": margen, "cac": cac, "objetivo": objetivo,
        "clv": clv, "ltv_cac": base, "cac_maximo": clv / objetivo,
        "compras_para_recuperar": cac / ganancia_compra,
        "sensibilidad": sens,
        "palanca_mayor": "CAC" if salto_cac > salto_clv else "CLV",
        "estado": "sano" if base >= objetivo else ("ajustado" if base >= 2 else "bajo"),
    }


def render(r):
    s = r["sensibilidad"]
    L = [
        "## Economía del cliente",
        "",
        "| Medida | Valor |", "|---|---|",
        f"| CAC | {pesos(r['cac'])} |",
        f"| CLV (ganancia) | {pesos(r['clv'])} |",
        f"| LTV:CAC | **{ratio(r['ltv_cac'])}** ({r['estado']}; objetivo {ratio(r['objetivo'])}) |",
        f"| CAC máximo para llegar al objetivo | {pesos(r['cac_maximo'])} |",
        f"| Compras para recuperar el CAC | {r['compras_para_recuperar']:.1f}".replace(".", ",") + " |",
        "",
        "| Si pasa esto | LTV:CAC |", "|---|---|",
        f"| Nada cambia | {ratio(s['base'])} |",
        f"| CAC baja 20% | {ratio(s['cac_menos_20'])} |",
        f"| Cada cliente compra 0,3 veces más | {ratio(s['mas_03_compras'])} |",
        f"| Las dos juntas | {ratio(s['ambas'])} |",
        "",
        f"Palanca de mayor salto con estos supuestos: **{r['palanca_mayor']}**. "
        "Antes de decidir, comparar el costo de mover cada una: los flujos de recompra suelen ser más baratos que la adquisición.",
    ]
    return "\n".join(L)


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--ticket", type=float, required=True, help="ticket promedio por compra")
    p.add_argument("--compras", type=float, required=True, help="compras por cliente en su vida (observadas)")
    p.add_argument("--margen", type=float, required=True, help="margen de contribución, fracción (0.55)")
    p.add_argument("--cac", type=float, required=True, help="CAC de clientes nuevos (nCAC)")
    p.add_argument("--objetivo", type=float, default=3.0, help="LTV:CAC objetivo (por defecto 3)")
    p.add_argument("--json", action="store_true", help="salida en JSON")
    a = p.parse_args(argv)
    try:
        r = calcular(a.ticket, a.compras, a.margen, a.cac, a.objetivo)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 2
    print(json.dumps(r, ensure_ascii=False, indent=2) if a.json else render(r))
    return 0


if __name__ == "__main__":
    sys.exit(main())
