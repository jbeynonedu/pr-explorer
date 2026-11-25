# Source pack: denying the antecedent

## bland-reason-ch2-da
Bland, *Reason* (Revised Edition), ch. 2, pp. 32–33. CC BY-NC 4.0. Project file.
Example (p. 32): "If I make the A-grade basketball team, then I'll be popular. I didn't make the A-grade basketball team, therefore I won't be popular." M, P. 1. If M then P. 2. Not M. C. Therefore, not P.
> In this argument, M guarantees P. If we are certain that M is true, then P is true also. However, there might be many other ways of making P (the consequent) true. (p. 32)

> Because we are denying the antecedent of the conditional in the second premise, this formal fallacy is known as denying the antecedent. (p. 33)

Lotto comparison (p. 33): same conditional as the modus tollens example; "The only difference is that we are now denying the antecedent (Not L) rather than denying the consequent (Not W). That single structural change is enough to turn a valid argument into an invalid one — and it shows why form matters more than content when we are evaluating deductive arguments."
Counterexample (p. 33): "A counter-example is a demonstration of how the deductive argument can be invalid".
Form box (p. 33): DENYING THE ANTECEDENT (FORMAL FALLACY) 1. If P then Q. 2. Not P. C. Therefore, not Q.
Variations (Exercise 2.2, pp. 33–34): (d) "1. K only if F. 2. Not K. C. Therefore, not F."; (f) "1. L only if P. 2. Not L. C. Therefore, not P."; Q2(h) "If the power is out, the lights will not work. The power is not out. Therefore, the lights must be working."
Truth-table test: Bland Exercise 3.4 Q1(d) (p. 53), basketball example.

## forallx-5-5-iff
forall x: Calgary (Fall 2025), §5.5, pp. 41–42 (§5.5 begins p. 41; the caution and greens example are on p. 42). CC BY 4.0.
> Ordinary speakers of English often use 'if . . . , then. . . ' when they really mean to use something more like '. . . if and only if . . . '. Perhaps your parents told you, when you were a child: 'if you don't eat your greens, you won't get any dessert'.

The parents are "only committed to the conditional (roughly 'if you get dessert, then you will have eaten your greens'), rather than the biconditional (roughly, 'you get dessert iff you eat your greens'). Well, a tantrum would rightly ensue." "be aware of this when interpreting people; but in your own writing, make sure you use the biconditional iff you mean to."
Note for drafting: forall x's own gloss of the conditional here ("if you get dessert, then you will have eaten your greens") differs from the literal "if you don't eat your greens, you won't get any dessert" (its contrapositive, so equivalent). The child who eats the greens and expects dessert is reasoning from the biconditional.

## Logic checks (code, 26 Nov 2026)
- `P ⊃ Q, ~P ∴ ~Q` invalid; counterexample P 0, Q 1.
- `K ⊃ F, ~K ∴ ~F` invalid; counterexample K 0, F 1.
- `P ⊃ ~L, ~P ∴ L` invalid; counterexample P 0, L 0.
- With biconditional `(P ⊃ Q) & (Q ⊃ P), ~P ∴ ~Q`: valid (checked).
