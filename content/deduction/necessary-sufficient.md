---
id: necessary-sufficient
title: Necessary and sufficient conditions
type: term
units: [1, 2, 3, 4]
section: deduction
status: checked
related: [logical-operators, translating-symbolising, affirming-the-consequent, denying-the-antecedent, searle-chinese-room, cause]
sources: [bland-reason-3-2, forallx-ch5-conditional-biconditional]
---

# Necessary and sufficient conditions

**A is a necessary condition for B if B cannot be the case without A. A is a sufficient condition for B if A guarantees B.** In logic, both are expressed with the conditional, `⊃`.

## Necessary conditions

If A is necessary for B, then whenever B is true, A is true: `B ⊃ A`. A is required for B, but it may not be the only requirement.

Water is necessary for a plant to grow. Water alone does not guarantee growth: without sunlight or nutrients, the plant will not grow however much it is watered. But if a plant is growing, it has water.

## Sufficient conditions

If A is sufficient for B, then whenever A is true, B is true: `A ⊃ B`.

Breathing is sufficient to show that a person is alive: if a person is breathing, they are alive.

## One conditional, read two ways

"A is necessary for B" says the same as "B is sufficient for A". Both are `B ⊃ A`.

<figure>
<svg viewBox="0 0 320 200" width="320" role="img" aria-labelledby="ns-title">
<title id="ns-title">Euler diagram: the circle of squares lies entirely inside the circle of rectangles.</title>
<ellipse cx="160" cy="100" rx="150" ry="90" fill="none" stroke="#1f4fbf" stroke-width="2"/>
<text x="160" y="36" text-anchor="middle" font-size="15">Rectangles</text>
<ellipse cx="160" cy="115" rx="70" ry="45" fill="none" stroke="#1f4fbf" stroke-width="2" stroke-dasharray="6 4"/>
<text x="160" y="120" text-anchor="middle" font-size="15">Squares</text>
</svg>
<figcaption>Every square is a rectangle. Being a square is sufficient for being a rectangle; being a rectangle is necessary for being a square.</figcaption>
</figure>

*Text alternative:* the region for squares lies wholly inside the region for rectangles. Anything in the inner region is also in the outer one, but not the reverse.

## Necessary and sufficient

When each condition guarantees the other, A is necessary *and* sufficient for B. This is two conditionals at once, joined by conjunction: `(A ⊃ B) & (B ⊃ A)`. For whole numbers, being divisible by 2 is necessary and sufficient for being even.

(Some texts express this with a separate operator, the biconditional `≡`. It is not one of the syllabus operators.)

## Reading the wording

| Wording | Symbolic | Reading |
| --- | --- | --- |
| If A, then B | `A ⊃ B` | A is sufficient for B |
| B if A | `A ⊃ B` | A is sufficient for B |
| A only if B | `A ⊃ B` | B is necessary for A |

Watch which part follows which word. The part after "if" is the antecedent; the part after "only if" is the consequent.

Take "A student can attend the formal only if they are in Year 12". Dictionary: `F = "The student can attend the formal."` `Y = "The student is in Year 12."` The sentence is `F ⊃ Y`: being in Year 12 is necessary for attending. It does not say that being in Year 12 is sufficient.

## Kinds of connection

A conditional can rest on different kinds of connection:

- a cause (water and plant growth)
- a definition (squares and rectangles)
- a rule or convention (the formal)
- evidence (breathing and being alive).

The symbol `⊃` records only that if the antecedent is true, so is the consequent. It does not say *why*, and in particular it does not express a causal connection.

## Two common mistakes

**Treating a necessary condition as if it were sufficient.** Take "If this plant is growing, then it has water; this plant has water; so it is growing". With `G = "This plant is growing."` and `W = "This plant has water."`, this reasons from `G ⊃ W` and `W` to `G`, which is [affirming the consequent](affirming-the-consequent).

**Treating a sufficient condition as if it were necessary.** Take "If a person is breathing, then they are alive; this person is not breathing; so they are not alive". With `B = "The person is breathing."` and `L = "The person is alive."`, this reasons from `B ⊃ L` and `~B` to `~L`, which is [denying the antecedent](denying-the-antecedent). The person might be holding their breath.

Many philosophical claims are claims about necessary or sufficient conditions. For example, the [Chinese room argument](searle-chinese-room) of John Searle (1932–2025) concludes that running a program is not sufficient for having a mind.

## Related concepts
[Logical operators](logical-operators) · [Translating and symbolising propositions](translating-symbolising) · [Affirming the consequent](affirming-the-consequent) · [Denying the antecedent](denying-the-antecedent) · [Searle's Chinese room argument](searle-chinese-room) · [Cause](cause)

## Sources
- Bland, *Reason* (Revised Edition), ch. 3, §3.2 pp. 42–43. CC BY-NC 4.0.
- Magnus, Button, Trueman and Zach, *forall x: Calgary* (Fall 2025), ch. 5, §§5.4–5.5, pp. 39–41. CC BY 4.0.
- Cole, D., "The Chinese Room Argument", *Stanford Encyclopedia of Philosophy* (rev. 23 Oct 2024; accessed 25 Nov 2026) (Searle's dates).
