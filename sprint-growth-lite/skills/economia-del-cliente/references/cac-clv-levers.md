# 04 · CAC, CLV and the levers to move them

The client's goal is one, with two hands: **pay less for each customer and have each customer leave more**. This reference turns that sentence into arithmetic and a work order.

## Customer economics

```
nCAC             = acquisition spend ÷ new customers
CLV (contrib.)   = average ticket × contribution margin × purchases per customer
LTV:CAC          = CLV ÷ nCAC                    (healthy: 3.0x or more)
Maximum CAC      = CLV ÷ 3                       (what can be paid for a customer)
Payback          = nCAC ÷ (CLV ÷ lifetime in months)  (months to recover CAC)
```

- **Always contribution CLV, not revenue.** A revenue CLV is optimism under another name.
- **nCAC, not blended CAC.** Blended CAC (total spend ÷ new customers) includes retargeting and brand, which do not acquire customers: it is shown only as contrast.
- A business with LTV:CAC below 3 does not need more budget: it needs one of the two hands.

## Which hand to move first: the sensitivity

Do not opine by intuition. Compute the table (the script delivers it) and compare:

| CAC | +0.0 purchases/customer | +0.3 | +0.6 |
|---|---|---|---|
| Current | base | … | … |
| −10% | … | … | … |
| −20% | … | … | … |

Reading: see which cell crosses 3.0x with the least real effort. Lowering CAC by 20% usually takes months of creative and audience testing; adding 0.3 purchases per customer usually comes from activating flows that should already exist. **It is not a law: it is arithmetic on the client's numbers, and the table gives the order, not dogma.** It is arithmetic, not forecast: it says what would happen *if* the change is achieved, not that it will be.

## CAC levers (acquisition)

| Symptom | What to look at | Lever | When NOT |
|---|---|---|---|
| Healthy CTR, low conversion | Landing page speed, pixel, purchase event, offer | Fix what happens after the click | If traffic is low-intent on purpose |
| CPM rises 30%+ in two weeks | Fatigue, exhausted audience, season | Creative reset | If it coincides with a commercial event |
| Cost per result rises with high frequency | First impression ratio < 50% (healthy prospecting: 65-80%) | Widen audience or renew | In retargeting, where high frequency is expected |
| Creative with high hook and low hold | Body of the video | Rebuild the body | Low hook: there, change the angle |
| A channel with mROAS below the loss line | Saturation curve | Reallocate 10-20% weekly | With under 12 weeks of data |
| Platform over-attributes | MER gap, CAPI, EMQ (target 6.0 or more) | Fix measurement **before** optimizing | Never optimize on broken measurement |

## CLV levers (retention and value)

**Mother rule: evaluate automated flows BEFORE campaigns.** And never recommend "send more emails" as a solution.

| Lever | Question | Diagnosis |
|---|---|---|
| **Abandoned cart** | Does it exist? Timing at 1 h, 24 h, 72 h? | If it does not exist, it is **always** priority #1 in ecommerce |
| **Welcome** | Does it exist? What is its conversion? | The first email is the most opened of the cycle |
| **Post-purchase** | Does it ask for a review? Cross-sell? | Second purchase: this is where CLV lives |
| **Replenishment and reactivation** | Is there a flow for inactive customers? | Win-back of those past their normal repurchase cycle |
| **Browse abandonment** | Does it exist? | Second tier, after cart |
| **Order value (AOV)** | Is there a free-shipping threshold, bundles, cross-sell? | Raises CLV without touching repurchase |
| **Segmentation** | Is there different content per segment? Are non-openers suppressed after 90 days? | Sending to inactives harms deliverability |

**Email channel health:**
- Revenue attributed to email: reference of 20-30% of the total in ecommerce. Far below usually indicates missing flows.
- Unsubscribe per send above 0.5% → alarm. Bounce above 2% → clean the list. More than 4 sends per week → almost always too many.
- **Revenue per recipient matters more than open rate** (opens are inflated by privacy preloading).
- Net list growth = new − unsubscribes − bounces. Look at the quality of the new ones: do they open, do they buy?

**Coupons: are we buying sales with discounts?** The % of orders with a coupon is computed against **total** orders, not against coupon rows. An order without a code emits no row. Not using coupons is a normal state, not a data gap, and "0% with coupon" is not claimed when what is missing is the sync.

**Abandoned checkouts: how much money reaches the door and does not get in?** **Checkouts are counted, not people.** Abandonment rate = abandoned ÷ (abandoned + orders). The abandoned amount is **not lost revenue 1:1**: it is demand that reached checkout. It is never presented as guaranteed recoverable money.

**Base dependence:** the % of orders from new customers is a signal. A store that only resells to its base is not growing.

## Lead gen: the chain, not the ratio

```
CPL → cost per MQL → cost per SQL → real CAC → LTV:CAC
```

- The MER equivalent is **cost per SQL**. It requires uploading CRM conversion (OCI) so platforms optimize for quality.
- The client's scoring model (lead above a threshold) is the input: it is uploaded as a conversion with value.
- Native-form leads and web leads are **not averaged** (see skill pauta-vara-por-objetivo).
- "Cost per conversation started" (an Ads metric) is not the conversation cost of the WhatsApp Business API: that is a separate platform cost, not included in Meta spend.
- Without offline conversion tracking, CPL is a vanity metric: a cheap lead that does not buy is expensive.

## Suggested work order

1. Confirm margin and revenue source (without them, nothing is reliable).
2. Fix measurement if the over-attribution gap exceeds 30%.
3. Look at the sensitivity table and choose the hand with the best effort/result ratio.
4. If CLV: flows before campaigns. If CAC: what happens after the click before the creative, the creative before the audience.
5. One change at a time. Validate before moving on.
