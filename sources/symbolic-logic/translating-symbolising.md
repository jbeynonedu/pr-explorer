# Source pack: translating and symbolising propositions

Project files read 26 Nov 2026: Bland, *Reason* (Revised Edition), CC BY-NC 4.0; forall x: Calgary (Fall 2025), CC BY 4.0. Convert forall x notation.

## bland-reason-dictionary
Bland, ch. 3, p. 36: a dictionary "is basically just a list of all propositions in an argument and the letters that you are using to represent them. We do this for convenience, so that we are not writing out entire sentences over and over again."
Bland, ch. 2, p. 25: "This is a compound proposition, meaning it is a logical expression that connects two or more propositions using a logical connective."

## bland-reason-wordings
Bland, p. 26 (and p. 40): "If R, then W." "If R, W." "W if R." "R only if W." "R is sufficient for W." "W is necessary for R." Footnote 6: "Be careful with this form. It's the only time that you will see the consequent (W) directly follow the word 'if'." (Glennie School example.)

## bland-reason-chart
Bland, Symbolising Summary Chart, p. 47 (four-operator rows only):
- Conjunction: P and Q; Both P and Q; P as well as Q; P but Q; P, however Q; P, yet Q; P, although Q; P, even though Q → P & Q
- Inclusive disjunction: P or Q; Either P or Q; P or Q or both; P unless Q → P ∨ Q
- Conditional: If P, then Q; Q if P; Q provided that P; Q in the case that P; Q whenever P; P implies Q; P leads to Q; P is sufficient for Q; Q is necessary for P; P only if Q → P ⊃ Q
- Other: Neither P nor Q → ~(P ∨ Q) or ~P & ~Q; Not both P and Q → ~(P & Q) or ~P ∨ ~Q
Footnote 8: "'P unless Q' is a tricky one. In English, the expression 'P unless Q' is usually interpreted as 'If not Q, then P'." Jog example; "The inferential statement ~Q ⊃ P is logically equivalent to P ∨ Q."

## bland-reason-brackets
Bland, §3.3 pp. 44–45: R ⊃ (S ∨ G); ~(R & H); three disjuncts: "(S ∨ F) ∨ C OR S ∨ (F ∨ C)".

## bland-reason-brendon
Bland, p. 38: "Brendon is a dangerous driver, yet he passed his driving test." The word "yet" "is loaded with implication"; "from a logical perspective, you need to remove all of the emotion and subtlety and hidden messages from this statement."

## forallx-ch5-but-although
forall x, ch. 5.2, pp. 35–36: "Although Barbara is energetic, she is not athletic" symbolised (E ∧ ¬B) [B = "Barbara is athletic"]: "we have lost all sorts of nuance in this symbolization [...] TFL does not (and cannot) preserve these nuances." Note: negative clause written with ¬ on a positive letter (supports the best-practice point; John: best practice, not a rule).

## forallx-5-6-unless
forall x, §5.6, pp. 42–43: "Unless you wear a jacket, you will catch a cold." Three correct symbolisations: (¬J → D), (¬D → J), (J ∨ D).
> If a sentence can be paraphrased as 'Unless A, B,' then it can be symbolized as '(¬A→ B)' or '(A∨ B)'.

Complication (p. 43): ordinary speakers "often use 'unless' to mean something more like the biconditional, or like exclusive disjunction" ("I will go running unless it rains"). "be aware of this when interpreting what other people have said, but be precise in your writing."

## forallx-5-3-neither
forall x, §5.3, p. 39: "You will get neither soup nor salad" → ¬(S1 ∨ S2); "Either you will not get soup, or you will not get salad" → (¬S1 ∨ ¬S2).

## forallx-10-2-symbolising-vs-translating
forall x, §10.2, pp. 73–74: sarcasm, poetry, implicature, emphasis "are important parts of everyday discourse, but none of this is retained in TFL." Five "Dana" sentences (and / although / despite / but also / notwithstanding) all symbolised the same way.
> This is why we will speak of symbolizing English sentences, rather than of translating them.

> When we treat a TFL sentence as symbolizing an English sentence, we are stipulating that the TFL sentence is to take the same truth value as that English sentence.

## unit2-example: searle-1990-axiom3 (from the Searle source pack)
Searle, J. R. (1990), "Is the Brain's Mind a Computer Program?", *Scientific American* 262: 26–31. In copyright: short quotation only. Fetched copy and flag as recorded in `sources/philosophy-of-mind/searle-chinese-room.md`. Second copy confirmed by checker (26 Nov 2026): scan at https://mail.joelvelasco.net/teaching/hum9/scientificamerican0190-26.pdf — Axiom 3 on p. 27, wording matches.
> Axiom 3. Syntax by itself is neither constitutive of nor sufficient for semantics.

Use: "neither ... nor" → `~C & ~S` (or `~(C ∨ S)`), with C = "Syntax by itself is constitutive of semantics.", S = "Syntax by itself is sufficient for semantics." Links to the Chinese room entry (status: checked).

## Logic checks (code, 26 Nov 2026)
`~Q ⊃ P` ≡ `P ∨ Q`; `~(P ∨ Q)` ≡ `~P & ~Q`; `~(P & Q)` ≡ `~P ∨ ~Q`: confirmed.
