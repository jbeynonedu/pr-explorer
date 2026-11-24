# PR Explorer — Style guide (v0.1, draft until the Phase 0 exemplars are approved)

## 1. Audience and voice
- Readers: Year 11 and 12 students, including students meeting an idea for the first time. Entries also serve Year 12 exam revision.
- Never oversimplify or overgeneralise. If a simplification is needed, say what it leaves out.
- Clear, precise, calm. Address the reader as "you" sparingly. No slang, filler, hype or rhetorical questions as padding.
- Define each technical term at first use and link it to its entry.
- Sentences generally under 25 words; paragraphs of 2–4 sentences.
- Australian spelling: analyse, generalisation, scepticism, behaviour, judgement.

## 2. Terminology (precise use is enforced)
- **House standard:** Bland's *Reason* definitions, aligned with the QCAA syllabus wording.
- Deductive arguments are **valid/invalid** and **sound/unsound**. Inductive arguments are **strong/weak**. Never cross these over.
- Never use "prove" or "proof" for inductive conclusions. Inductive premises *support* or *make probable*.
- Validity and soundness are all-or-nothing. Never write "partly valid" or "more sound".
- Claims are **true/false**; they may also be **plausible** or **credible** (syllabus terms). Arguments are not true or false.
- Use "argument" in its technical sense only; for a disagreement say "debate" or "dispute".
- Use the syllabus's own name for each item (e.g. "illicit appeal to popular opinion").
- Add rules to this list whenever John flags a misuse.

## 3. Notation and standard form
- Logical operators (syllabus): negation `~`, conjunction `&`, inclusive disjunction `∨`, conditional `⊃`. Therefore: `∴`.
- Never use →, ∧ or ¬ (forall x uses them); convert when adapting.
- Give a dictionary of propositions before symbolising: `L = "I win the lotto."`
- Standard form, as in Bland: numbered premises `1.`, `2.`, conclusion labelled `C.`, hidden premises labelled `(HP)`.
- Symbolic line form: `P ⊃ Q, ~Q ∴ ~P`.

## 4. Naming
- Fallacies: Latin name first, as in the syllabus, with the English as a subtitle (e.g. **Ad hominem**, *attacking the person*).
- Thinkers: full name at first mention with dates (e.g. David Hume (1711–1776)), surname after that.
- Works: italic title, then year of first publication at first mention.

## 5. Examples
- Prefer Australian contexts (Parliament, Australian media, Queensland issues, school life) when they work as well as generic ones.
- Examples must be accurate. A real-world example is sourced like any other fact.
- Avoid examples that take a side on a live political issue, unless the entry is presenting both sides.
- Use worked examples to show the method, not just the answer.

## 6. Primary texts and quotation
- Quote philosophers' own words wherever this helps. Every quotation is copied from a fetched source.
- Cite under each quotation: author, *work*, section/chapter/page, translator or edition. For Early Modern Texts versions, credit Jonathan Bennett with a link to earlymoderntexts.com.
- Quote as written, including gendered language ("man", "he"); no warning note is needed.
- Use `[...]` for omissions and square brackets for clarifying insertions.
- Public-domain texts may be quoted at length. In-copyright works: short quotations only, each discussed in the entry.
- After a difficult passage, add a plain-English gloss ("In other words...") that does not distort it.

## 7. Contested questions
- Present the strongest version of each position, as its own defenders would state it.
- Pair objections with replies where replies exist.
- The Explorer gives no verdict on God, ethical or political questions. Evaluation sections show *how* to evaluate (premise by premise), not what to conclude.

## 8. Entry types (minimum contents; shape the rest to the concept)
| Type | Must contain | Typical length |
| --- | --- | --- |
| Term | Definition; explanation; example; related concepts | 150–350 words |
| Logic form | Definition; symbolic form; standard-form example; why valid/invalid (truth table); look-alike forms | 300–600 words |
| Fallacy | Definition; the pattern; 2–3 examples from real contexts; when it is *not* fallacious; related fallacies | 300–600 words |
| Argument | Primary-text extract; context; standard form; argument map; objections and replies; how to evaluate it | 800–1,500 words |
| Theory / thinker | Core principles; primary extracts; how it works; applied to a dilemma; criticisms and replies; links | 1,200–2,500 words, split into sub-entries |

- "Common mistakes" and "exam tips" only where genuinely useful. No quick-check questions for now.
- Every entry ends with related concepts (links) and sources.

## 9. Visuals
- Use a visual only where it explains something prose cannot: truth tables (interactive for logic forms), Venn/Euler diagrams, argument maps, process diagrams (e.g. the falsification cycle), concept diagrams (e.g. state of nature → social contract).
- Label every visual. Keep it accessible: text alternatives, no meaning carried by colour alone.
- Colour by branch: Reason cobalt, Philosophy coral.

## 10. Entry file format (repo)
`content/<section>/<entry-id>.md` with front matter:
```
---
id: modus-tollens
title: Modus tollens
type: logic-form        # term | logic-form | fallacy | argument | theory
units: [1]
section: symbolic-logic
status: drafted         # briefed | sourced | drafted | checked | approved | live
related: [modus-ponens, denying-the-antecedent, popper-falsification]
sources: [bland-reason-ch2, forallx-calgary]
---
```
