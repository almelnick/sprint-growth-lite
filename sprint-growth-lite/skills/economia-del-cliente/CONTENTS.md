# Customer Economics

`economia-del-cliente` · Customer economics

> Pay less for each customer, or have each customer leave more.

## What it does

- Computes contribution CLV, LTV:CAC, maximum CAC and payback from four inputs.
- Builds a sensitivity table to show which hand to move first, with the least real effort.
- Links symptoms to levers: what to look at, which lever, and when not to pull it.
- Gives a Spanish client report with Chilean formatting through a small stdlib script.

## The method signature

How this skill thinks and works:

- There is one goal with two hands: lower nCAC, raise CLV. Intuition does not choose between them; arithmetic does.
- Always contribution, never revenue. A revenue CLV is optimism under another name.
- A business under 3.0x does not need more budget. It needs one of the two hands.

## What is inside

| File | Role |
|---|---|
| `SKILL.md` | Entry point: trigger description, process, output contract (under 150 lines). |
| `references/cac-clv-levers.md` | Reference loaded on demand. |
| `references/foundations.md` | The sources behind the method and exactly what is used from each. |
| `scripts/economia.py` | Stdlib-only Python script. Client-facing output in Spanish (Chilean format). |
| `tests/test_economia.py` | Unit tests for the script. |
| `preview/preview.html` | Interactive illustration, opens in any browser. Synthetic data only. |
| `assets/banner.svg` | English banner for GitHub. |
| `assets/README-snippet.md` | Paste-ready block that embeds the banner. |

## Credits and sources

LTV:CAC and payback conventions from the library (Reichheld and Sasser; Fader, Hardie and Lee).

Full citations are in `biblioteca/referencias.md` (and in each skill's `references/foundations.md`).

## Data policy

Every example, fixture and preview number in this skill is synthetic and made up. No real client, brand or customer data is included. Replace the templates with the real data of the engagement.

---
© Alan Melnick · alanmelnick.com. All rights reserved. Created and modified by Alan Melnick; distribution, resale, sharing or republishing, in whole or in part, without his written authorization is prohibited.
