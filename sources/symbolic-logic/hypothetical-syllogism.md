# Source pack: hypothetical syllogism

## bland-reason-ch2-hs
Bland, *Reason* (Revised Edition), ch. 2, pp. 27–28. CC BY-NC 4.0. Project file.
> Modus ponens and modus tollens are formal methods of affirming or denying the conclusion of an argument, respectively. However, there is another valid inferential argument form whose conclusion is itself a conditional statement. (p. 27)

Example (p. 27): "If it's a weekday morning, then I need to go to work. If I need to go to work, then I should set the alarm. Therefore, if it's a weekday morning, then I should set the alarm." M, W, A. 1. If M, then W. 2. If W, then A. C. Therefore, if M, then A.
Form box (p. 28): HYPOTHETICAL SYLLOGISM 1. If P, then Q. 2. If Q, then R. C. Therefore, if P then R.
> Hopefully you can see how this argument functions as a conditional chain — by linking M and W, then linking W and A, we can complete the chain and conclude that M is linked to A also. In fact, this kind of argument can be set up to have as many premises as you wish — as long as each conditional is linked to the one that precedes it, you have a guaranteed connection between the antecedent of the first premise and the consequent of the last premise. (p. 28)

## bland-reason-ch3-hs-table
Bland, ch. 3, p. 52: 1. M ⊃ W 2. W ⊃ A C. M ⊃ A; eight rows. "there are only two rows where the conclusion is false (the 5th and 6th rows), and for each of those, there is at least one false premise. So again, we can confidently declare that the argument is valid."
Note: Bland's table lists columns A M W (p. 52 header "A M W"); row positions depend on column order. Entry should state the rows by truth values (M true, A false), not by row number.

## iep-prop-logic-hs
Klement, K. C., "Propositional Logic", *Internet Encyclopedia of Philosophy*, §5.b "Rules of Inference". https://iep.utm.edu/propositional-logic-sentential-logic/ (Chrome, 26 Nov 2026). Rule HS: α→β, β→γ ∴ α→γ.
> (Hypothetical syllogism is sometimes also called "chain reasoning" or "chain deduction".)

## slippery-slope-link (one line, per John)
No source needed for the logical point (verified by code). Link only to the slippery slope entry (not started).

## Logic checks (code, 26 Nov 2026)
- `P ⊃ Q, Q ⊃ R ∴ P ⊃ R`: valid; conclusion false in 2 of 8 rows (P true, R false), each with a false premise.
- `P ⊃ Q, R ⊃ Q ∴ P ⊃ R`: invalid; counterexample P 1, Q 1, R 0.
- `P ⊃ Q, P ⊃ R ∴ Q ⊃ R`: invalid; counterexample P 0, Q 1, R 0.
- `P ⊃ Q, Q ⊃ R ∴ R ⊃ P`: invalid; counterexamples P 0, R 1 (Q either value).
