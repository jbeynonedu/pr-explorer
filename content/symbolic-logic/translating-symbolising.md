---
id: translating-symbolising
title: Translating and symbolising propositions
type: term
units: [1, 2, 3, 4]
section: symbolic-logic
status: checked
related: [logical-operators, proposition, standard-form, necessary-sufficient, modus-tollens, searle-chinese-room]
sources: [bland-reason-dictionary, bland-reason-wordings, bland-reason-chart, bland-reason-brackets, bland-reason-brendon, forallx-ch5-but-although, forallx-5-6-unless, forallx-5-3-neither, forallx-10-2-symbolising-vs-translating, searle-1990-axiom3]
---

# Translating and symbolising propositions

**To symbolise a proposition is to write it with capital letters for its simple propositions and [logical operators](logical-operators) for the connections between them. Translating also runs the other way: reading a symbolic expression back into English.** With `R = "It is raining."` and `J = "I will go for a jog."`, `~R ⊃ J` reads "If it is not raining, then I will go for a jog." Symbolising shows an argument's form, so it can be named or tested with a truth table.

## Step 1: the dictionary

A dictionary lists each simple proposition and the letter that stands for it. One letter stands for one proposition, with the same wording every time it appears.

It is good practice to state each proposition positively and write negatives with `~`. With `R = "It is raining."`, "It is not raining" is `~R`. A separate letter for the negative (`N = "It is not raining."`) hides the link between the two, and can make a valid form harder to see.

## Step 2: match the wording to an operator

| English | Symbolic |
| --- | --- |
| P and Q; P but Q; P, yet Q; P, although Q; P, however Q | `P & Q` |
| P or Q; either P or Q | `P ∨ Q` |
| If P, then Q; Q if P; Q provided that P; Q whenever P; P implies Q | `P ⊃ Q` |
| P only if Q; P is sufficient for Q; Q is necessary for P | `P ⊃ Q` |

## Tricky cases

- **"Only if."** "You can sit the exam only if you have your student card" (`E = "You can sit the exam."`, `C = "You have your student card."`) is `E ⊃ C`, not `C ⊃ E`. The part after "only if" is the consequent. See [necessary and sufficient conditions](necessary-sufficient).
- **"Unless."** "P unless Q" is usually read as "if not Q, then P": `~Q ⊃ P`, which is equivalent to `P ∨ Q`. "I'll go for a jog unless it is raining" (`J = "I will go for a jog."`, `R = "It is raining."`) is `~R ⊃ J`. Speakers sometimes mean more than this ("if and only if it is not raining"), so check the context when interpreting someone else.
- **"Neither … nor."** "Neither P nor Q" is `~(P ∨ Q)`, or equivalently `~P & ~Q`.
- **"Not both."** "Not both P and Q" is `~(P & Q)`, or equivalently `~P ∨ ~Q`. "You will not have both the pie and the sausage roll" (`I = "You will have the pie."`, `S = "You will have the sausage roll."`) is `~(I & S)`: you may have one, or neither. It is not the same as "neither".
- **"Q if P."** "The game is cancelled if it storms" (`G = "The game is cancelled."`, `T = "It storms."`) is `T ⊃ G`. The part after "if" is the antecedent, wherever it comes in the sentence.

## Step 3: brackets
With more than one operator, brackets show the structure. Build the formula from the parts outwards. "If the bus is late and it is raining, then I will walk":

Dictionary:

- `B = "The bus is late."`
- `R = "It is raining."`
- `W = "I will walk."`

1. The antecedent is a conjunction: `B & R`.
2. The whole sentence is a conditional with that conjunction as its antecedent: `(B & R) ⊃ W`.

The main operator is `⊃`, the last one applied. Moving the brackets changes the meaning: `B & (R ⊃ W)` says that the bus *is* late, and that if it rains I'll walk. Without brackets, `B & R ⊃ W` is not well formed.

## An example from philosophy of mind

In a 1990 summary of his Chinese room argument, John Searle (1932–2025) set out a series of axioms. The third reads:

> Axiom 3. Syntax by itself is neither constitutive of nor sufficient for semantics.

John R. Searle, "Is the Brain's Mind a Computer Program?", *Scientific American* 262 (1990), p. 27.

Dictionary:

- `C = "Syntax by itself is constitutive of semantics."`
- `S = "Syntax by itself is sufficient for semantics."`

Symbolic form: `~(C ∨ S)`, or equivalently `~C & ~S`. See [Searle's Chinese room argument](searle-chinese-room).

## What symbolising leaves out

With `D = "Brendon is a dangerous driver."` and `P = "Brendon passed his driving test."`, "Brendon is a dangerous driver, yet he passed his driving test" and "Brendon is a dangerous driver and he passed his driving test" are both `D & P`. The surprise carried by "yet" is lost. A symbolic expression keeps only the truth value of the English: it is true in exactly the cases where the English is true. For this reason some logicians prefer to speak of *symbolising* rather than *translating*.

## Related concepts
[Logical operators](logical-operators) · [Proposition](proposition) · [Standard form](standard-form) · [Necessary and sufficient conditions](necessary-sufficient) · [Modus tollens](modus-tollens) · [Searle's Chinese room argument](searle-chinese-room)

## Sources
- Bland, *Reason* (Revised Edition), ch. 2, pp. 25–26; ch. 3, pp. 36, 38, 44–47. CC BY-NC 4.0.
- Magnus, Button, Trueman and Zach, *forall x: Calgary* (Fall 2025), ch. 5, §§5.2–5.3, 5.6, pp. 35–39, 42–43; ch. 10, §10.2, pp. 73–74. CC BY 4.0.
- Searle, J. R., "Is the Brain's Mind a Computer Program?", *Scientific American* 262 (1990), pp. 26–31.
