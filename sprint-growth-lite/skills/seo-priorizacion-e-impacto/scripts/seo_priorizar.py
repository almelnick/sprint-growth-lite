#!/usr/bin/env python3
# © Alan Melnick · alanmelnick.com. All rights reserved. Distribution without written authorization is prohibited.
# -*- coding: utf-8 -*-
"""seo_priorizar.py - Ordena acciones SEO/GEO por impacto, confianza y esfuerzo, y estima el efecto como RANGO.

Entrada CSV (UTF-8, coma o punto y coma). Columnas:
  accion, impacto (1-5), confianza (0-1), esfuerzo_dias (>0),
  [clics_mes_actuales, mejora_pct_min, mejora_pct_max, valor_por_clic]
Puntaje = impacto x confianza / esfuerzo_dias.  Estimación = clics actuales x mejora (rango) x valor por clic.
Nunca entrega una cifra única: un rango, con su supuesto a la vista.

Uso: python3 seo_priorizar.py --acciones acciones.csv [--salida plan.md] [--json]
"""
import argparse
import csv
import json
import sys


def num(x):
    if x is None or str(x).strip() == "":
        return None
    s = str(x).strip().replace("%", "").replace("$", "").replace(" ", "")
    if "," in s and "." in s:
        s = s.replace(".", "").replace(",", ".")
    elif "," in s:
        s = s.replace(",", ".")
    elif s.count(".") > 1 or (s.count(".") == 1 and len(s.split(".")[1]) == 3 and len(s.split(".")[0]) <= 3 and float(s.replace(".", "")) >= 1000):
        s = s.replace(".", "")
    return float(s)


def pesos(x):
    return "$" + f"{round(x):,}".replace(",", ".")


def cargar(ruta):
    with open(ruta, encoding="utf-8-sig", newline="") as f:
        muestra = f.read(2048)
        f.seek(0)
        delim = ";" if muestra.count(";") > muestra.count(",") else ","
        filas = list(csv.DictReader(f, delimiter=delim))
    acciones, avisos = [], []
    for i, r in enumerate(filas, start=2):
        r = {(k or "").strip().lower(): v for k, v in r.items()}
        try:
            a = {"accion": (r.get("accion") or "").strip(), "impacto": num(r.get("impacto")),
                 "confianza": num(r.get("confianza")), "esfuerzo": num(r.get("esfuerzo_dias")),
                 "clics": num(r.get("clics_mes_actuales")), "min": num(r.get("mejora_pct_min")),
                 "max": num(r.get("mejora_pct_max")), "valor": num(r.get("valor_por_clic"))}
        except ValueError:
            avisos.append(f"Fila {i}: hay un número ilegible; se omite.")
            continue
        if not a["accion"] or None in (a["impacto"], a["confianza"], a["esfuerzo"]):
            avisos.append(f"Fila {i}: faltan accion, impacto, confianza o esfuerzo_dias; se omite.")
            continue
        if not (1 <= a["impacto"] <= 5) or not (0 < a["confianza"] <= 1) or a["esfuerzo"] <= 0:
            avisos.append(f"Fila {i} ('{a['accion']}'): impacto 1-5, confianza 0-1 y esfuerzo > 0; se omite.")
            continue
        a["puntaje"] = a["impacto"] * a["confianza"] / a["esfuerzo"]
        a["rango"] = None
        if a["clics"] is not None and a["min"] is not None and a["max"] is not None:
            if a["min"] > a["max"]:
                avisos.append(f"Fila {i}: mejora_pct_min mayor que mejora_pct_max; se intercambian.")
                a["min"], a["max"] = a["max"], a["min"]
            lo, hi = a["clics"] * a["min"] / 100, a["clics"] * a["max"] / 100
            a["rango"] = (lo, hi, lo * a["valor"] if a["valor"] else None, hi * a["valor"] if a["valor"] else None)
        acciones.append(a)
    acciones.sort(key=lambda a: -a["puntaje"])
    return acciones, avisos


def render(acciones, avisos):
    L = ["# Plan priorizado", "", "Puntaje = impacto × confianza ÷ esfuerzo (días). Es un orden de trabajo, no una predicción.", ""]
    if not acciones:
        L.append("No hay acciones válidas.")
    else:
        L += ["| # | Acción | Impacto | Confianza | Esfuerzo (días) | Puntaje |", "|---|---|---|---|---|---|"]
        for n, a in enumerate(acciones, 1):
            L.append(f"| {n} | {a['accion']} | {a['impacto']:g} | {a['confianza']:.0%} | {a['esfuerzo']:g} | {a['puntaje']:.2f} |".replace(".", ","))
        con = [a for a in acciones if a["rango"]]
        if con:
            L += ["", "## Efecto estimado (rango, no promesa)", "", "| Acción | Clics extra por mes | Valor por mes |", "|---|---|---|"]
            for a in con:
                lo, hi, vlo, vhi = a["rango"]
                v = f"{pesos(vlo)} a {pesos(vhi)}" if vlo is not None else "sin valor por clic"
                L.append(f"| {a['accion']} | {lo:,.0f} a {hi:,.0f} | {v} |".replace(",", "."))
            L += ["", "Supuesto: la mejora porcentual la declara quien llena el archivo y se confirma con Search Console en un plazo fijado de antemano. "
                  "Los efectos de acciones distintas se solapan: no se suman."]
    if avisos:
        L += ["", "## Avisos", ""] + [f"- {x}" for x in avisos]
    return "\n".join(L)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--acciones", required=True)
    ap.add_argument("--salida")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    try:
        acc, av = cargar(a.acciones)
    except OSError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 2
    out = json.dumps({"acciones": acc, "avisos": av}, ensure_ascii=False, indent=2, default=str) if a.json else render(acc, av)
    if a.salida:
        with open(a.salida, "w", encoding="utf-8") as f:
            f.write(out + "\n")
    else:
        print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
