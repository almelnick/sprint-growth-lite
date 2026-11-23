---
name: rrss-anti-slop
description: Quality gate for social copy and scripts - detects generic, AI-sounding, empty or unprovable writing and rewrites it into specific, human, on-brand text. Use before publishing any caption, script, carousel or ad copy, or when the user says content sounds generic, robotic, "AI-written" or repetitive. Also: "suena a IA", "contenido genérico", "revisar copy".
---

# Social media: anti-slop gate

Generic copy is invisible. This skill finds it and replaces it with something specific and provable. Reply in the user's language (Chilean Spanish, never voseo, when the user writes in Spanish).

## Process

1. **Run the linter** on the text: `python3 scripts/rrss_lint.py --archivo copy.txt`. It flags clichés, voseo, generic calls to action, and excess hashtags, emojis, exclamations and long dashes. Exit code 1 means a high-severity finding (voseo).
2. **Apply the manual checklist** in `references/anti-slop-checklist.md`: specificity, proof, voice, structure, rhythm.
3. **Rewrite each flagged line** with a concrete detail: a number, a name, a place, a use case, a customer sentence.
4. **Re-run the linter** and read the piece aloud once. The linter finds patterns; only a person judges voice.
5. **Return** the cleaned copy plus a short list of what changed and why.

## Rules

1. Never invent facts to sound specific. If the detail is missing, ask for it or leave a clearly marked gap.
2. No voseo in Chilean Spanish copy; use tuteo or a neutral form.
3. Keep the brand's own words and quirks; remove generic filler, not personality.
4. A clean linter result does not mean good copy.
5. Do not claim a text is "undetectable as AI". The goal is quality, not disguise.

## Output

Cleaned copy; change log with reasons; open gaps that need a real fact from the client.

## Method signature

- A finding is a signal, not a sentence: a person decides.
- Replace the cliché with a fact only the brand can prove.
- Orwell's rule applies: if it can be cut, cut it.

## Foundations

`references/foundations.md`; checklist in `references/anti-slop-checklist.md`.

---
© Alan Melnick · alanmelnick.com. All rights reserved. Created and modified by Alan Melnick; distribution, resale, sharing or republishing, in whole or in part, without his written authorization is prohibited.
