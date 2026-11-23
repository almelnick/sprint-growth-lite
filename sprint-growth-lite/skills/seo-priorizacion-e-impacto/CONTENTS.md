# SEO Prioritization and Impact

`seo-priorizacion-e-impacto` · SEO and GEO

> A work order with honest ranges, never a promised ranking.

## What it does

- Scores actions by impact times confidence divided by effort in days.
- Estimates extra clicks and value only as ranges, with the assumption stated beside the number.
- Fixes the measurement window before the work starts.
- Reads a CSV and writes a ranked plan in Spanish.

## The method signature

How this skill thinks and works:

- Ranges, never a single figure. The assumption lives next to the number.
- No tactic promises a position. Large effects are rare; results that look too good deserve suspicion first.
- Decide what not to do now and write down why.

## What is inside

| File | Role |
|---|---|
| `SKILL.md` | Entry point: trigger description, process, output contract (under 150 lines). |
| `references/foundations.md` | The sources behind the method and exactly what is used from each. |
| `scripts/seo_priorizar.py` | Stdlib-only Python script. Client-facing output in Spanish (Chilean format). |
| `templates/actions.csv` | Template to fill with the client's real data. |
| `tests/test_seo_priorizar.py` | Unit tests for the script. |
| `preview/preview.html` | Interactive illustration, opens in any browser. Synthetic data only. |
| `assets/banner.svg` | English banner for GitHub. |
| `assets/README-snippet.md` | Paste-ready block that embeds the banner. |

## Credits and sources

Estimation caution from experimentation literature (Lewis and Rao; Kohavi et al.). AI-summary click impact: Pew Research Center (2025).

Full citations are in `biblioteca/referencias.md` (and in each skill's `references/foundations.md`).

## Data policy

Every example, fixture and preview number in this skill is synthetic and made up. No real client, brand or customer data is included. Replace the templates with the real data of the engagement.

---
© Alan Melnick · alanmelnick.com. All rights reserved. Created and modified by Alan Melnick; distribution, resale, sharing or republishing, in whole or in part, without his written authorization is prohibited.
