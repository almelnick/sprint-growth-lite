---
name: seo-priorizacion-e-impacto
description: Turns SEO and GEO findings into an ordered plan with effort, confidence and an impact RANGE (never a single figure). Use after an audit, when the user asks what to fix first, how much traffic or revenue a change could bring, how to justify an SEO budget, or how to report results. Also use to push back on promises like "we will rank first in 3 months". Also: "qué arreglo primero", "cuánto tráfico traería".
---

# SEO: prioritization and impact

Auditors list 40 findings. The client needs the five that move money, in order, with honest uncertainty. Reply in the user's language (Chilean Spanish, never voseo, when the user writes in Spanish).

## Process

1. **Collect the actions** from `seo-auditoria-tecnica`, `seo-contenido-semantico` and `geo-visibilidad-en-ia` into `templates/actions.csv`: action, impact (1-5), confidence (0-1), effort in days.
2. **Ground impact in the account's own data.** Pull current clicks and impressions per page group from Search Console. Impact without a baseline is an opinion.
3. **Declare a percentage range** per action (minimum and maximum improvement) and the value per click (from conversion rate × margin, supplied by the client).
4. **Run** `python3 scripts/seo_priorizar.py --acciones actions.csv --salida plan.md`. Score = impact × confidence ÷ effort. Output is Spanish.
5. **Read the result critically.** Quick wins first, but keep one strategic bet (new page, new content cluster) even if its score is low: it has the longest horizon.
6. **Set the confirmation rule up front:** which metric, which window, which comparison (same period last year, or a matched set of untouched pages).

## Rules

1. Always a range, with the assumption beside it. Never "this will bring 30% more traffic".
2. Effects of different actions overlap; never add them up.
3. No ranking promises. Search results depend on factors outside the site and change without notice.
4. Distinguish correlation from effect: a before/after chart without a comparison group proves little (see the experiment references).
5. Report GEO separately and honestly: citation tests are samples, not rankings.
6. Revenue claims need the client's conversion and margin data; without them, stop at clicks.

## Output

Ranked table; ranges with assumptions; the one strategic bet; confirmation rule; what will not be promised.

## Method signature

- Ranges, never a single figure. The assumption lives next to the number.
- No tactic promises a position. Large effects are rare; results that look too good deserve suspicion first.
- Decide what not to do now and write down why.

## Foundations

`references/foundations.md`.

---
© Alan Melnick · alanmelnick.com. All rights reserved. Created and modified by Alan Melnick; distribution, resale, sharing or republishing, in whole or in part, without his written authorization is prohibited.
