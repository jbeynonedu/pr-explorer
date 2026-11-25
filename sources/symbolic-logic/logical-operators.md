# Source pack: logical operators

Project files read 26 Nov 2026: Bland, *Reason* (Revised Edition), CC BY-NC 4.0; forall x: Calgary (Magnus, Button, Trueman, Zach; Fall 2025), CC BY 4.0. forall x uses ¬ ∧ → ↔: convert to ~ & ⊃ in entries.

## bland-reason-3-1-negation
Bland, ch. 3, §3.1, pp. 36–37.
> A negation simply indicates that a proposition is false. The operator itself is referred to as a tilde [...] You can think of the tilde as meaning "NOT". (p. 36)

> This is the simplest operator we will use, and it's the only operator that applies to a single proposition. Because of this, we call it a unary operator. (p. 36)

> By convention, in these tables we use a "1" to mean "true" and a "0" to mean "false". The tilde sign basically reverses the truth value of an individual proposition (p. 37)

Example (p. 36): "It is not raining." R = "It is raining." ~R. Table (p. 37): P 1 → ~P 0; P 0 → ~P 1.
**Flag:** the p. 36 sentence is imprecise (~P is true when P is false); use p. 37 "reverses the truth value".

## bland-reason-3-1-conjunction
Bland, p. 37: conjunction is "a simple binary operator, meaning that it connects two propositions"; "equivalent to joining two propositions with the word 'AND'"; symbol "known as an ampersand".
Example: "I have done my homework and brushed my teeth." H = "I have done my homework." T = "I have brushed my teeth." H & T. "it is only true if both of the component propositions are true also."
Table: 1 1 → 1; 1 0 → 0; 0 1 → 0; 0 0 → 0.
p. 38: "Brendon is a dangerous driver, yet he passed his driving test" — "from a logical perspective [...] you are simply asserting two propositions to be true."

## bland-reason-3-1-disjunction
Bland, p. 38: "An inclusive disjunction is a binary operator that most commonly substitutes for the word 'OR'. The symbol for this operator is known as a vel". Example: "I will buy a book, or I will buy a swimsuit." B ∨ S; true if both bought; "the only case in which your sister's statement would be false is if she were to arrive home with neither a book nor a swimsuit." Tip: "when you see the word 'OR' joining two propositions, you should always assume that this is an inclusive disjunction unless there are very specific reasons for assuming otherwise."
Table: 1 1 → 1; 1 0 → 1; 0 1 → 1; 0 0 → 0.

## bland-reason-3-1-conditional
Bland, pp. 39–40. Symbol "known as a hook". Example: "If you board the train, then you must have a ticket." B ⊃ T, reasoned as a rule: rows (A) 1 1, (C) 0 1, (D) 0 0 "abide by the rule"; (B) 1 0 "breaks the conditional rule".
> As you can see from the table, the only situation where a conditional is false is if the antecedent is true and the consequent is false. (p. 40)

Table: 1 1 → 1; 1 0 → 0; 0 1 → 1; 0 0 → 1. Equivalent wordings (p. 40): If P, then Q / If P, Q / Q if P / P only if Q / P is sufficient for Q / Q is necessary for P.
**Flag:** the "rule" with "must" is normative; a rule can be broken without the statement being false. Entry uses a descriptive example.

## bland-reason-3-1-bicond-xor (note only, per John)
Bland, pp. 40–41: bi-conditional ≡ ("tribar"), "if and only if"; exclusive disjunction ≢ ("slashed tribar"), "A or B BUT NOT BOTH". Summary chart p. 47 gives the English cues.

## bland-reason-3-3-main-operator
Bland, §3.3, pp. 44–45.
> This final operator is called the main operator of the expression, and it determines the truth value for the entire expression. (p. 44)

Examples: "If it's raining, then I'll either study or play computer games." R ⊃ (S ∨ G). "It's not true that I'm relaxing and on holiday." ~(R & H): "the tilde (~) is the main operator. This is because it's the last thing that you need to do to process the meaning of the expression". WFF rules (p. 45): 1. a main operator governs the formula (atomic proposition excepted); 2. binary operators connect exactly two WFFs, ~ applies to exactly one; 3. parentheses paired; 4. no stray symbols.

## forallx-ch5-connectives
forall x: Calgary, ch. 5, p. 32: connectives "can be used to form new sentences out of old ones". 'unless' and 'neither ... nor ...' "can be expressed by the connectives we will discuss, while the last ['because'] cannot. 'Because', in contrast to the others, is not truth functional."
§5.3 (p. 38): "The TFL symbol '∨' always symbolizes an inclusive or." Menu example of exclusive or ("Entrees come with either soup or salad"). Exclusive or symbolised (p. 39) as ( (S1 ∨ S2) ∧ ¬(S1 ∧ S2)): "Although the TFL symbol '∨' always symbolizes inclusive or, we can symbolize an exclusive or in TFL. We just have to use a few other symbols as well."

## forallx-ch10-truth-functional
forall x, ch. 10.1 (idea of truth-functionality) and 10.3 "Indicative versus subjunctive conditionals", pp. 74–76. Justification of the conditional's table "which follows Dorothy Edgington" (footnote: Edgington, "Conditionals", SEP Fall 2020): claim "If any shape is grey, then that shape is also circular" is true if no shape is grey and not circular; so its instances with false antecedents (shapes C, D) must be true; only a grey non-circular shape (B) makes it false.
> What this argument shows is that '→' is the best candidate for a truth-functional conditional. (p. 76)

Limit (p. 76): two subjunctive conditionals with false antecedents and false consequents differ in truth value (Hillary Clinton examples), so "the truth value of the whole sentence is not uniquely determined by the truth value of the parts."
> '→' is the only candidate for a truth-functional conditional for TFL, but that many English conditionals cannot be represented adequately using '→'. (p. 76)

## iep-prop-logic-material-implication
Klement, K. C., "Propositional Logic", *Internet Encyclopedia of Philosophy*, §3.b "Truth Functions and Truth Tables". https://iep.utm.edu/propositional-logic-sentential-logic/ (Chrome, 26 Nov 2026).
> If α is false, then ┌(α→β)┐ is regarded as true, whether or not there is any connection between the falsity of α and the truth-value of β.

> The sign '⊃' is sometimes used instead of '→' for material implication.

## Logic checks (code, 26 Nov 2026)
Exclusive or `(P ∨ Q) & ~(P & Q)` true exactly when P and Q differ: confirmed. "Neither" `~(P ∨ Q)` ≡ `~P & ~Q`; "not both" `~(P & Q)` ≡ `~P ∨ ~Q`: confirmed.
