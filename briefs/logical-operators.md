---
id: logical-operators
type: term
section: symbolic-logic
units: [1, 2, 3, 4]
stage: briefed
approved_scope: yes
---

# Brief: Logical operators (~, &, ∨, ⊃) (term)

## Syllabus dot points (verbatim)
Unit 1 Topic 1, p. 11:
- translate and symbolise propositions using logical operators: negation ( ~ ), conjunction ( & ), inclusive disjunction ( ∨ ), conditional ( ⊃ )

Unit 2 (all topics, pp. 14–16), Unit 3 (both topics, pp. 18–19), Unit 4 (both topics, pp. 22–23): "translate and symbolise propositions using logical operators".

## John's unit material
Bland's text stands in for unit material for all of Unit 1 (John, 25 Nov 2026).

## Proposed scope (400–550 words; longer than a usual term because of the four tables)
1. **Definition**: a logical operator (connective) builds a compound proposition from simpler ones; its truth value is fixed by the truth values of its parts (Bland pp. 36–37; forall x ch. 5, ch. 10.1 "truth-functional").
2. **The four operators**, each with symbol, name, English reading, one example with dictionary, and its truth table (1 = true, 0 = false):
   - Negation `~` (tilde): unary; reverses the truth value (Bland pp. 36–37).
   - Conjunction `&` (ampersand): true only when both conjuncts are true (p. 37).
   - Inclusive disjunction `∨` (vel): false only when both disjuncts are false; "or" is read as inclusive by default (p. 38).
   - Conditional `⊃` (hook): false only when the antecedent is true and the consequent false (pp. 39–40).
3. **Why a conditional with a false antecedent counts as true** (2–3 sentences): the shapes argument in forall x ch. 10.3 (after Edgington); `⊃` is the best truth-functional conditional, but it does not capture every English "if" (e.g. subjunctive conditionals). See Q2.
4. **Main operator and brackets** (Bland pp. 44–45): the main operator fixes the truth value of the whole; worked examples `R ⊃ (S ∨ G)`, `~(R & H)`. Well-formed formulae, briefly (the four rules, restricted to the four operators).
5. **Other connectives with the four operators**: "P or Q but not both" as `(P ∨ Q) & ~(P & Q)`; "P if and only if Q" as `(P ⊃ Q) & (Q ⊃ P)`. Note on `≡` and `≢` (see Q1).
6. **Related**: translating and symbolising, proposition, necessary and sufficient conditions, the valid forms, deductively valid and invalid.

## Planned sources
- Bland, *Reason*, §3.1 pp. 36–41, §3.3 pp. 44–45, summary chart p. 47. Project file.
- forall x: Calgary (CC BY 4.0), ch. 5 (connectives), ch. 9 (characteristic truth tables), ch. 10 (truth-functionality; indicative vs subjunctive). Project file; convert ¬ ∧ → to ~ & ⊃.

## Visuals
Four small truth tables (static; verified by code at Checked). Optional: one interactive "operator explorer" (pick P and Q, see each operator's value). Proposed: static only.

## Accuracy flags (Bland)
- p. 36: "A negation simply indicates that a proposition is false." Imprecise: `~P` is true when P is false. The entry uses Bland's own p. 37 wording ("reverses the truth value").
- p. 39: the conditional is explained with "If you board the train, then you must have a ticket", a rule with "must". The table is right, but a rule can be broken without being false. The entry uses a descriptive example.

## Questions for John
1. **`≡` and `≢`**: Bland gives both a full section (pp. 40–41). Proposed, consistent with the necessary-and-sufficient decision: write both with the four operators (item 5), and mention `≡` and `≢` in one note as symbols students may meet in other texts.
2. **False antecedents**: include item 3 (2–3 sentences, forall x ch. 10.3)? Proposed: yes; students regularly ask why "if pigs fly, then..." comes out true.
3. **Units**: the operators are used in every unit. Set `units` to 1;2;3;4 (as for necessary and sufficient conditions)? Proposed: yes.

## Scope decision (John, 26 Nov 2026)
Approved.
Q1: yes, write both with the four operators; `≡` and `≢` in a note only. Q2: yes, include item 3. Q3: yes, units 1–4.
