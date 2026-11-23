#!/usr/bin/env python3
# © Alan Melnick · alanmelnick.com. All rights reserved. Distribution without written authorization is prohibited.
"""Anti-slop linter for social copy (Spanish and English).

Flags generic AI-sounding patterns, voseo (never allowed in this project's
Chilean Spanish copy), empty hype, hashtag and emoji excess. It reports
findings; a person decides what to change. Stdlib only.
"""
import argparse
import json
import re
import sys

CLICHES = [
    r"en el (acelerado |cambiante )?mundo (de hoy|actual)", r"hoy en d[ií]a", r"sum[eé]rgete",
    r"desbloquea", r"revoluciona", r"lleva (tu|su) \w+ al siguiente nivel", r"cambia las reglas del juego",
    r"no es solo \w+(,| sino| es)", r"descubre el poder de", r"te presentamos", r"imperdible",
    r"in today'?s (fast-paced )?world", r"unlock (the )?(power|potential)", r"game[- ]changer",
    r"elevate your", r"dive into", r"take .{0,20} to the next level",
]
# Voseo verb forms and pronouns (Rioplatense). The project writes tuteo or neutral Chilean.
VOSEO = [
    r"\bvos\b",
    # Voseo forms carry a written accent; the unaccented forms (mira, sabes) are tuteo.
    r"\b(tenés|querés|podés|sabés|venís|decís|hacés|andás|pensás|mirás|vivís)\b",
    r"\b(mirá|escuchá|andá|pensá|decime|dejá|vení|tené|hacé|fijate|suscribite|seguinos|comprá|probá|empezá)\b",
]
GENERIC_CTA = [r"s[ií]guenos para m[aá]s", r"d[ií]nos en los comentarios", r"link in bio", r"d[eé]janos tu opini[oó]n"]
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿]")


def buscar(patrones, texto, flags=re.IGNORECASE):
    hallazgos = []
    for p in patrones:
        for m in re.finditer(p, texto, flags):
            hallazgos.append((m.group(0), m.start()))
    return hallazgos


def analizar(texto):
    h = []
    for frase, pos in buscar(CLICHES, texto):
        h.append({"tipo": "cliché", "texto": frase, "pos": pos, "gravedad": "media"})
    for frase, pos in buscar(VOSEO, texto):
        h.append({"tipo": "voseo", "texto": frase, "pos": pos, "gravedad": "alta"})
    for frase, pos in buscar(GENERIC_CTA, texto):
        h.append({"tipo": "CTA genérico", "texto": frase, "pos": pos, "gravedad": "baja"})
    rayas = texto.count("—")
    palabras = max(1, len(texto.split()))
    if rayas >= 3 and rayas / palabras > 0.02:
        h.append({"tipo": "exceso de rayas largas", "texto": f"{rayas} en {palabras} palabras", "pos": 0, "gravedad": "baja"})
    hashtags = len(re.findall(r"#\w+", texto))
    if hashtags > 5:
        h.append({"tipo": "exceso de hashtags", "texto": f"{hashtags} hashtags", "pos": 0, "gravedad": "baja"})
    emojis = len(EMOJI.findall(texto))
    if emojis > 6:
        h.append({"tipo": "exceso de emojis", "texto": f"{emojis} emojis", "pos": 0, "gravedad": "baja"})
    exclam = texto.count("!")
    if exclam > 4:
        h.append({"tipo": "exceso de exclamaciones", "texto": f"{exclam} signos", "pos": 0, "gravedad": "baja"})
    return sorted(h, key=lambda x: x["pos"])


def render(hallazgos, nombre="pieza"):
    if not hallazgos:
        return f"# Revisión anti-relleno: {nombre}\n\nSin hallazgos. Una persona debe leerla igual.\n"
    l = [f"# Revisión anti-relleno: {nombre}", "", "| Tipo | Texto | Gravedad |", "|---|---|---|"]
    for x in hallazgos:
        l.append(f"| {x['tipo']} | {x['texto'].replace('|', '/')} | {x['gravedad']} |")
    l += ["", "Los hallazgos son señales, no sentencias: una persona decide qué cambiar."]
    return "\n".join(l) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description="Revisa texto de redes sociales.")
    ap.add_argument("--archivo", required=True)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    try:
        with open(a.archivo, encoding="utf-8") as f:
            texto = f.read()
    except OSError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 2
    h = analizar(texto)
    print(json.dumps(h, ensure_ascii=False, indent=2) if a.json else render(h, a.archivo))
    return 1 if any(x["gravedad"] == "alta" for x in h) else 0


if __name__ == "__main__":
    sys.exit(main())
