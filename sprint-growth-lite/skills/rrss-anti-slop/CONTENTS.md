# Anti-Slop Gate

`rrss-anti-slop` · Social media

> Generic copy is invisible. Find it, and replace it with something provable.

## What it does

- Scans copy for generic AI-sounding phrases, empty hype and generic calls to action.
- Flags voseo as high severity, always; the project writes tuteo or neutral Chilean.
- Counts hashtags, emojis, exclamations and long dashes against sane limits.
- Rewrites with a change log and lists the real facts still missing from the client.

## The method signature

How this skill thinks and works:

- A finding is a signal, not a sentence: a person decides.
- Replace the cliché with a fact only the brand can prove.
- Orwell's rule applies: if it can be cut, cut it.

## What is inside

| File | Role |
|---|---|
| `SKILL.md` | Entry point: trigger description, process, output contract (under 150 lines). |
| `references/anti-slop-checklist.md` | Reference loaded on demand. |
| `references/foundations.md` | The sources behind the method and exactly what is used from each. |
| `scripts/rrss_lint.py` | Stdlib-only Python script. Client-facing output in Spanish (Chilean format). |
| `tests/test_rrss_lint.py` | Unit tests for the script. |
| `preview/preview.html` | Interactive illustration, opens in any browser. Synthetic data only. |
| `assets/banner.svg` | English banner for GitHub. |
| `assets/README-snippet.md` | Paste-ready block that embeds the banner. |

## Credits and sources

Writing discipline after George Orwell, Politics and the English Language (1946).

Full citations are in `biblioteca/referencias.md` (and in each skill's `references/foundations.md`).

## Data policy

Every example, fixture and preview number in this skill is synthetic and made up. No real client, brand or customer data is included. Replace the templates with the real data of the engagement.

---
© Alan Melnick · alanmelnick.com. All rights reserved. Created and modified by Alan Melnick; distribution, resale, sharing or republishing, in whole or in part, without his written authorization is prohibited.
