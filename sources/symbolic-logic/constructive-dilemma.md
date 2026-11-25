# Source pack: constructive dilemma

## bland-reason-ch2-cd
Bland, *Reason* (Revised Edition), ch. 2, p. 29. CC BY-NC 4.0. Project file.
> This argument is very similar to the modus ponens structure, but instead of containing just the one conditional statement, we have two conditionals, accompanied by a disjunction between the two antecedents. (p. 29)

Example (p. 29): "If I drive to my friend's house, then I'll save time. On the other hand, if I take the bus to my friend's house, then I'll save money. I'll either drive or catch the bus to my friend's house. Therefore, I'll either save time or save money." D, B, T, M. 1. If D then T. 2. If B then M. 3. D or B. C. Therefore, T or M.
Form box: CONSTRUCTIVE DILEMMA 1. If P then Q. 2. If R then S. 3. P or R. C. Therefore, Q or S.
> Remember that although all of these argument forms are valid, we know nothing about their soundness. To evaluate soundness, we need to take the further step of assessing the truth of the premises. (p. 29)

Exercise 2.1 Q1(d) (p. 30): 1. If L then M. 2. If N then O. 3. N or L. C. Therefore, M or O. (disjunct order varies). Exercise 3.4 Q1(c) (p. 53): test the drive/bus example by truth table.

## iep-prop-logic-cd
Klement, K. C., "Propositional Logic", *Internet Encyclopedia of Philosophy*, §5.b "Rules of Inference". https://iep.utm.edu/propositional-logic-sentential-logic/ (Chrome, 26 Nov 2026). Rule CD: (α→γ)∧(β→δ), α∨β ∴ γ∨δ. Note: IEP states the two conditionals as one conjunction; Bland as two premises. Same content.

## wilson-good-reasoning-12-3
Wilson, D. C., *A Guide to Good Reasoning: Cultivating Intellectual Virtues*, ch. 12, §12.3 "Dilemmas". University of Minnesota Libraries open textbook, CC BY-NC 4.0. https://open.lib.umn.edu/goodreasoning/chapter/chapter-12-either-or-arguments-and-more/ (Chrome, 26 Nov 2026).
> In popular jargon—which presumes that dilemmas are problems—the two alternatives expressed in the first premise are often referred to as the horns of the dilemma. Showing that the either–or premise is false is termed escaping between the horns of the dilemma, since it provides a way out of the forced choice. And showing that one of the if–then premises is false is termed attacking a horn of the dilemma, since this renders the choice harmless by removing the threat of the purported consequence.

Also: "Dilemmas are usually enthymematic. Sometimes both the either–or premise and the conclusion are implicit; sometimes both of the if–then premises are implicit." (links hidden premise). Wilson: "There are no widely accepted names for these forms; so, when evaluating a valid dilemma, identify it simply as correct form for a dilemma." (re variant forms; the entry uses the syllabus name).
Terminology varies: Wilson "attacking a horn"; other texts "taking/grasping the dilemma by the horns" (search results only: Wikipedia "Dilemma"; Naugle handout). Entry uses Wilson's two terms, or describes the moves without names.

## destructive-dilemma
Wikipedia "Constructive dilemma" (search snippet, 26 Nov 2026): "Constructive dilemma is the disjunctive version of modus ponens, whereas, destructive dilemma is the disjunctive version of modus tollens." Tertiary; the form and validity are verified by code, so no quotation needed. One look-alike row only.

## Logic checks (code, 26 Nov 2026)
- `P ⊃ Q, R ⊃ S, P ∨ R ∴ Q ∨ S`: valid; 16 rows; conclusion false in 4 (Q 0, S 0), each with at least one false premise.
- Simple case `P ⊃ Q, R ⊃ Q, P ∨ R ∴ Q`: valid.
- Destructive dilemma `P ⊃ Q, R ⊃ S, ~Q ∨ ~S ∴ ~P ∨ ~R`: valid.
- "Affirming the consequents" `P ⊃ Q, R ⊃ S, Q ∨ S ∴ P ∨ R`: invalid; counterexamples (P,Q,R,S) = (0,1,0,1), (0,1,0,0), (0,0,0,1).
