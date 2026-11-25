---
id: logical-operators
title: Logical operators (~, &, ∨, ⊃)
type: term
units: [1, 2, 3, 4]
section: symbolic-logic
status: drafted
related: [translating-symbolising, proposition, necessary-sufficient, valid, modus-ponens, modus-tollens, disjunctive-syllogism]
sources: [bland-reason-3-1, bland-reason-3-3, forallx-ch5-connectives, forallx-ch10-truth-functional, iep-prop-logic-material-implication]
---

# Logical operators (~, &, ∨, ⊃)

**A logical operator (or connective) builds a compound proposition from one or more simpler propositions.** Four operators are used here: negation `~`, conjunction `&`, inclusive disjunction `∨` and the conditional `⊃`. For each of them, the truth value of the compound is fixed entirely by the truth values of its parts. (Not every English connective works this way: whether "P because Q" is true depends on more than whether P and Q are true.)

Each operator is defined by a truth table, which lists every combination of truth values for the parts (1 = true, 0 = false).

## Negation `~` ("not")

Negation (symbol: tilde) applies to a single proposition and reverses its truth value. With `R = "It is raining."`, "It is not raining" is `~R`.

| P | `~P` |
| --- | --- |
| 1 | 0 |
| 0 | 1 |

## Conjunction `&` ("and")

A conjunction (symbol: ampersand) joins two propositions, its *conjuncts*. It is true only when both conjuncts are true. With `H = "I have done my homework."` and `T = "I have brushed my teeth."`, "I have done my homework and brushed my teeth" is `H & T`.

| P | Q | `P & Q` |
| --- | --- | --- |
| 1 | 1 | 1 |
| 1 | 0 | 0 |
| 0 | 1 | 0 |
| 0 | 0 | 0 |

## Inclusive disjunction `∨` ("or")

A disjunction (symbol: vel) joins two propositions, its *disjuncts*. It is false only when both disjuncts are false. It is *inclusive*: it is still true when both are true. With `L = "I will study Legal Studies."` and `E = "I will study Economics."`, "I will study Legal Studies or Economics" is `L ∨ E`, and it is true if I study both. Read "or" as inclusive unless there is a clear reason not to.

| P | Q | `P ∨ Q` |
| --- | --- | --- |
| 1 | 1 | 1 |
| 1 | 0 | 1 |
| 0 | 1 | 1 |
| 0 | 0 | 0 |

## Conditional `⊃` ("if … then")

The conditional (symbol: hook) joins two propositions. In `P ⊃ Q`, P is the *antecedent* and Q is the *consequent*. With `F = "The oval is flooded."` and `G = "The game is cancelled."`, "If the oval is flooded, then the game is cancelled" is `F ⊃ G`. A conditional is false only when the antecedent is true and the consequent is false.

| P | Q | `P ⊃ Q` |
| --- | --- | --- |
| 1 | 1 | 1 |
| 1 | 0 | 0 |
| 0 | 1 | 1 |
| 0 | 0 | 1 |

The last two rows can seem odd. Suppose someone says of a page of shapes: "If a shape is grey, then it is circular." Only a grey shape that is not circular would show the claim to be false. Shapes that are not grey cannot count against it, so the claim about each of them ("If this shape is grey, then it is circular") comes out true. If the conditional is truth-functional, each row of its table must take the value of these instances, which gives the table above.

This makes `⊃` the best conditional a truth-functional logic can offer, but it does not capture every English "if". "If it had rained, the game would have been cancelled" is a *subjunctive* conditional: it describes what would have happened. Its truth depends on more than the truth values of its parts, so `⊃` cannot represent it adequately.

## The main operator and brackets

Brackets show which operator applies to which parts, as in arithmetic. The operator applied last is the **main operator**; it fixes the truth value of the whole expression.

- "If it's raining, then I'll either study or play computer games." With `R = "It is raining."`, `S = "I will study."` and `C = "I will play computer games."`, this is `R ⊃ (S ∨ C)`. The main operator is `⊃`.
- "It's not true that I'm relaxing and on holiday." With `X = "I am relaxing."` and `H = "I am on holiday."`, this is `~(X & H)`. The main operator is `~`, applied to the whole conjunction.

In a well-formed formula, each `&`, `∨` and `⊃` joins exactly two formulas, `~` applies to exactly one, and brackets come in pairs. Every well-formed formula except a single letter has exactly one main operator. `P & Q ∨ R` is not well formed, because it could mean `(P & Q) ∨ R` or `P & (Q ∨ R)`.

## Other connectives, built from the four

- "P or Q, but not both" (exclusive disjunction): `(P ∨ Q) & ~(P & Q)`.
- "P if and only if Q" (the biconditional): `(P ⊃ Q) & (Q ⊃ P)`.

(Some texts give these their own symbols: `≢` for exclusive disjunction and `≡` for the biconditional.)

See [translating and symbolising propositions](translating-symbolising) for how to move between English and these symbols.

## Related concepts
[Translating and symbolising propositions](translating-symbolising) · [Proposition](proposition) · [Necessary and sufficient conditions](necessary-sufficient) · [Deductively valid and invalid](valid) · [Modus ponens](modus-ponens) · [Modus tollens](modus-tollens) · [Disjunctive syllogism](disjunctive-syllogism)

## Sources
- Bland, *Reason* (Revised Edition), ch. 3, §3.1 pp. 36–41; §3.3 pp. 44–45. CC BY-NC 4.0.
- Magnus, Button, Trueman and Zach, *forall x: Calgary* (Fall 2025), ch. 5, pp. 32–39; ch. 10, §§10.1–10.3, pp. 72–76 (the shapes argument follows Dorothy Edgington). CC BY 4.0.
- Klement, K. C., "Propositional Logic", *Internet Encyclopedia of Philosophy*, §3.b. https://iep.utm.edu/propositional-logic-sentential-logic/
