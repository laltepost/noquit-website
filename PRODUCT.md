# Product

## Register

brand

## Users

**Primary audience: consistency-seeking functional fitness athletes** in the US — CrossFit-adjacent, hybrid training, 4–6+ sessions per week — who want to maintain quality output when fatigue builds and recover ready for the next session. Supplement-literate; they read labels and treat supplements as part of a training stack.

**Adjacent audience:** serious endurance athletes (runners, cyclists, triathletes). The brand register and aesthetic work for both; copy and imagery should lead with functional fitness and not exclude endurance.

**Context when buying.** Comparison mode, often on mobile, often late at night after a session. They've already seen a dozen supplement sites this month and will leave a site within seconds if it feels like the rest of them. The decision is partly identity ("is this for athletes like me?") and partly evidence ("does the science hold up?").

**Job to be done.** Decide whether to add NØ QUIT to a personal recovery/performance routine, and if so, whether to subscribe vs. one-time. Secondarily: understand phenylcapsaicin enough to defend the purchase to themselves.

## Product Purpose

DTC commerce site for **NØ QUIT Phenylcapsaicin Capsules** (60 capsules, 30 servings, 2.5 mg phenylcapsaicin per serving, powered by aXivite®). US-only market.

Success looks like: a serious athlete finishes the homepage already convinced this brand belongs in their stack, clicks through to the product page, reads enough science to feel responsible, and subscribes. The site has to do this without ever feeling like it's trying.

## Brand Personality

**Performance-luxury.** Three words: precise, restrained, confident.

Closer to Tracksmith, On, or NormaTec than to any supplement brand currently in the category. Editorial typography over hype. Matte black, steel accent, generous whitespace, near-zero color. The aesthetic carries the persuasion; the copy stays out of the way.

**Tone of voice.** Spare sentences, clinical accuracy, no exclamation points, no superlatives, no second-person hectoring. Lines like "Finish Strong. Recover Ready." land because they're terminal — nothing else is shouting.

**Emotional target on landing.** Quiet aspiration. The buyer should want to be the kind of athlete who takes this *before* they finish reading the benefits. Identity-pull first, then evidence.

## Anti-references

The four lanes this site must never feel like:

- **Supplement-bro hype.** Bang / C4 / GNC. Neon green, ALL CAPS GAINS, before/after photos, exclamation marks, urgency timers, stacks of capsules photographed like ammunition.
- **Pharmacy-clinical bland.** CVS / Centrum / Walgreens private label. Blue + white, stock photos of smiling models, regulatory-tone copy, generic "supports immune health" headers.
- **Cottage-wellness.** Goop, Moon Juice, hand-lettered Instagram brands. Pastel + beige, hand-drawn marks, herbal language, "rituals," soft serifs.
- **Generic DTC Shopify.** Inter on off-white, identical hero, identical product grid, rounded everything, the same five testimonial cards every brand uses. The site shouldn't look like it came out of a theme.

## Design Principles

1. **Show capability, don't claim it.** Let the brand, the formulation, and the science do the persuading. If a section requires the word "powerful" or "revolutionary," rewrite the section.
2. **Identity-first persuasion.** A serious athlete should recognize themselves on the page before they encounter a benefit claim. Photography, typography, and pacing carry this — copy supports it.
3. **Earned, not assumed.** Every performance or recovery claim cites mechanism, dose, or peer-reviewed evidence. No lifestyle stock, no vague superlatives, no "studies show" without a study.
4. **Restraint as the signal.** The category is loud. The absence of hype *is* the differentiation. If a design choice raises the noise floor, it loses.
5. **One product, full attention.** The bottle is the protagonist on every page. Copy, photography, and layout defer to it. There is no second product to cross-sell.

## Accessibility & Inclusion

**Target: WCAG AA.**

- Text contrast ≥ 4.5:1 against background. The current palette uses dim text values (`#8A8680`, `#6E6A64`) against near-black; these likely fail AA on body copy and need to be audited.
- Full keyboard navigation across nav, cart drawer, product gallery, accordion, purchase toggle, and forms. Visible focus styles on every interactive element.
- `prefers-reduced-motion` respected for the bottle video, scroll reveals, and any animated transitions.
- Descriptive alt text on all product, brand, and editorial images. Decorative images marked appropriately.
- Form errors announced to screen readers, not only shown visually.
- Color is never the sole carrier of meaning (e.g. subscribe vs. one-time state, error states).
