---
name: economia-del-cliente
description: Computes a business's unit economics (CAC, CLV, LTV:CAC, maximum CAC, payback) and says which hand to move first, CAC or CLV, with a sensitivity table. Use when the user asks "how much can I pay for a customer?", "why is CAC rising?", "how do I raise CLV?", or when deciding between acquiring more and retaining better. Shared by the paid media director and the customer analyst. Also: "CAC máximo", "LTV:CAC", "cuánto puedo pagar por un cliente".
---

# Customer economics

CAC and CLV are two hands of the same number. This skill puts them in the same table and says which is cheaper to move. Reply in the user's language (Chilean Spanish, never voseo, when the user writes in Spanish).

## Process

1. Gather: average ticket, **observed** purchases per customer (not assumed), contribution margin (given by the client, never assumed) and nCAC (new customers only).
2. Run `python3 scripts/economia.py --ticket T --compras C --margen M --cac N [--objetivo 3]`. The report is in Spanish.
3. Read the sensitivity: CAC −20%, +0.3 purchases per customer, and both. The lever with the biggest jump is not necessarily the cheapest: compare the cost of moving each with `references/cac-clv-levers.md`.
4. If LTV:CAC is below 3, choose the work order from the reference (repurchase flows usually go before rebuilding acquisition).
5. If CLV comes from an assumption, say so and ask `clientes-analisis` for the real measurement.

## Rules

1. Without margin there is no profit CLV: the calculation is revenue-based and is not compared with CAC.
2. Never mix blended CAC with nCAC without saying so.
3. In lead generation look at the chain (lead → appointment → sale), not cost per lead in isolation.
4. "Send more emails" is not a lever; a lever has a segment, a mechanism, a KPI and a deadline.

## Method signature

- There is one goal with two hands: lower nCAC, raise CLV. Intuition does not choose between them; arithmetic does.
- Always contribution, never revenue. A revenue CLV is optimism under another name.
- A business under 3.0x does not need more budget. It needs one of the two hands.

## Foundations

See `references/foundations.md`: how much retention weighs, what the evidence says about LTV and why growing by acquisition and by retention are not mutually exclusive.

---
© Alan Melnick · alanmelnick.com. All rights reserved. Created and modified by Alan Melnick; distribution, resale, sharing or republishing, in whole or in part, without his written authorization is prohibited.
