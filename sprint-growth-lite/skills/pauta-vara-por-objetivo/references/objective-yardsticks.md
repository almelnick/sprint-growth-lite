# The yardstick of each objective

Before any business metric, a more basic question must be answered: **which number decides whether this campaign is doing well?** If the question has no answer, the campaign stays without a verdict and its spend becomes invisible.

> **Rule:** two campaigns share a bucket only if they share the yardstick. And the yardstick is not the diagnosis: the yardstick is ONE and decides the verdict; the diagnosis is the set of numbers that explain why the yardstick moved, and they never decide alone.

## Yardstick table (Meta, six ODAX objectives)

The primary KPI derives from the **optimization goal**, not only from the objective. An Engagement campaign can optimize for interactions, ThruPlay or conversations: three different KPIs.

| Objective | Optimization goal | Yardstick (decides) | Diagnosis (explains) | Vanity (do not use as yardstick) |
|---|---|---|---|---|
| Awareness | Reach / ThruPlay | Cost per person reached | Frequency, CPM, reach | Absolute impressions, likes |
| Traffic | Landing Page Views | **Cost per LPV** (more honest than CPC) | Clicks, LPV/clicks, outbound CTR | Isolated clicks |
| Engagement (post) | Post Engagement | Cost per interaction | Engagement rate | Total reactions |
| Engagement (video) | ThruPlay | Cost per ThruPlay | Hook rate, hold rate, retention | Started plays |
| Engagement (messages) | Conversations | Cost per conversation started | CTR, blocks | Impressions |
| Leads (form) | Leads | **CPL** | Completed form rate | Clicks |
| Leads (CRM) | Conversion Leads | Cost per qualified lead | Gross CPL, close rate | Gross CPL alone |
| App | Installs / Events | CPI / cost per event | Install→event | Installs without retention |
| Sales | Conversions / Value | **ROAS and CPA** | AOV, CVR, MER, ROAS of new customers | Pixel ROAS without context |

Google equivalent: Search and Shopping are judged by ROAS (ecommerce) or CPL (leads); Performance Max, the same; reach-focused Display/Demand Gen, by cost per reach.

## Four frequent mistakes

**a) Traffic is not awareness.** The most expensive mistake because it is the most common: platforms return objectives such as `LINK_CLICKS` and it is tempting to file them as "brand". A traffic campaign has an honest, actionable yardstick (CPC or, better, cost per LPV). Leaving it without judgment equals not looking at that spend. Awareness does lack a conversion yardstick; traffic does not.

**b) The awareness yardstick is not CPM.** CPM measures impressions; awareness buys **people**. Two campaigns with identical CPM can be opposites: one reaches 100,000 people once, the other 5,000 people twenty times. Cost per person reached separates them and frequency explains which is which. When cost per reach spikes, new audience has almost always run out.
⚠️ Reach **does not add up**: summing daily reach counts the same person every day. Reach for a period is requested by window and level, or it is not used as a yardstick.

**c) Video is not awareness.** You can have terrible cost per reach and excellent cost per view: you reach few people, but those reached keep watching. That is a finding, and it is lost if they share a bucket.
Reading video: high hook + low hold = fix the body; low hook + high hold = fix the first 3 seconds; both low = change the angle, not the edit. Fixed formulas: hook rate = 3-second plays ÷ impressions; hold rate = ThruPlays ÷ 3-second plays. Fix ONE definition and keep it (the industry does not standardize it).

**d) Downloads are not purchases, and calls are not leads.** A campaign optimizing **installs** is measured by cost per download, never by the ROAS of purchases the bid attributes to it: ROAS can print 100x of fiction while its real product is downloads. A **calls** campaign is measured by cost per call. The trap: that category contains the word "lead" and, carelessly, falls into the lead bucket where its CPL means nothing. Detect it by the dominant conversion category and let the client correct it upstream.

## The limit of the rule

If an objective has no yardstick the source can measure, the campaign stays **without a verdict** and that is said. The yardstick of another objective is not lent to it so as to be able to give an opinion: a judgment with the wrong yardstick is worse than none, because it looks equally confident.

## Native lead is not comparable with GA4 (hard rule)

Meta reports two different products under the same word `lead`:

| Meta action | Where it was filled | Does GA4 see it? |
|---|---|---|
| `onsite_conversion.lead*` | **Inside Facebook/Instagram** (native form) | **Never** |
| `lead` minus the native one | On your landing page | Yes |

`onsite` means *inside Meta*, not inside your site. If the person never left the app, there was no visit for Analytics to record.

> **Rule:** before comparing "what the platform says" with "what the backend sees", subtract the native-form lead.

**The case that exposed it:** a contradiction engine compared 251 leads reported by the platform against 24 seen by GA4 and issued "90% over-attribution, critical". But 228 of those leads were native forms. After subtracting them, about 23 web leads remained against GA4's 24: the two sources matched almost exactly. The system was telling the admin to ignore 90% of their real leads.

Corollaries:
- The two numbers **add up**, they are not contrasted: they are different acquisition channels.
- On screen they are named by origin ("Leads (Meta form)" and "Web leads"). Calling them the same invites subtracting them.
- Over-attribution is still measured on web leads, which both sources see. If there is no volume there, no judgment is issued.
- Native leads convert cheaper and usually qualify worse. The CPLs of the two worlds are **not averaged** without saying so.

## Bid strategies (cross-cutting)

Highest volume (default, no cost control) · Cost per result goal (set 10-20% above target CPA) · Bid cap (needs 50-100 conversions) · Highest value · Minimum ROAS. **Changing the bid strategy restarts learning.**

## Two levels: judge fine, count big

- **Campaign level, judge with its yardstick:** each campaign with its metric profile.
- **Strategic level, count by funnel stage:** Awareness (TOFU) = reach + engagement; Consideration (MOFU) = traffic; Conversion (BOFU) = leads + sales. Count the spend **mix** ("20% / 15% / 65%, balanced" or "everything in BOFU: you are not feeding the top").

**Rule when grouping:** do not mix KPIs of different nature into one number (do not add cost per LPV to ROAS). Show (a) the mix by stage, which does add up because it is money, and (b) each stage's own KPI next to it. Never a Frankenstein number.
