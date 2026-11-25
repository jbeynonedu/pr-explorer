---
id: gamblers-fallacy
title: Gambler's fallacy
type: fallacy
units: [1]
section: informal-fallacies
status: drafted
related: [induction, hasty-generalisation, cognitive-bias, strong-weak, informal-fallacy]
sources: [bland-reason-ch4, iep-fallacies]
---

# Gambler's fallacy

**The gambler's fallacy is the belief that past outcomes of independent random events change the probability of the next outcome.** For example, someone might think a result is "due" because it has not happened for a while. It is an [informal fallacy](informal-fallacy) of weak induction.

## The pattern

```sf
1. X has not happened in the last several independent trials.
C. Therefore, X is more likely on the next trial.
```

The mistake also runs the other way: believing that a streak is more likely to continue.

## Independence is the key

Events are *independent* when one has no effect on the next. A fair coin or die has no memory. Suppose a fair die has landed on 1 five times in a row. The chance of a 1 on the next roll is still 1 in 6. The other numbers are not "overdue", and the streak is not more likely to continue.

## Why it is tempting

Over many trials, the proportion of heads from a fair coin does tend to settle near half. But it settles because later results swamp the early ones, not because the coin makes up for them. Suppose 10 tosses give 7 heads (70 per cent). If the next 1,000 tosses give an expected 500 heads, the total is 507 heads in 1,010 tosses, about 50.2 per cent. The early excess of heads has not been cancelled; it has been diluted.

Try it yourself. In the simulator below, look at the tosses that come straight after a run of three or more heads. Over many tosses, about half of them are heads, just like every other toss.

<!-- interactive: coin-sim -->

## Examples

At a roulette table, red has come up five spins in a row. A player says, "Black is due," and bets on it.

```sf
1. Red has come up on the last five spins.
C. Therefore, black is more likely on the next spin.
```

Each spin of a fair wheel is independent: landing on red has no effect on the colour of the next spin. The chance of black is the same as it always was.

A lottery player says, "Number 17 hasn't come up for months. It's overdue."

```sf
1. Number 17 has not been drawn in recent draws.
C. Therefore, number 17 is more likely to be drawn next.
```

In a fair draw, every number has the same chance each time. Past draws do not change it.

## When it is not fallacious

- **When the events are not independent.** In a card game where drawn cards are not replaced, the past does change the odds. If an ace has been drawn, there is one fewer ace left, so another ace is less likely next.
- **When a streak is evidence that the set-up is not fair.** A very long run of heads can be a reason to suspect that the coin is biased. Revising your belief about the coin is reasonable; expecting a fair coin to "balance out" is not.

## Related concepts
[Induction](induction) · [Hasty generalisation](hasty-generalisation) · [Cognitive bias](cognitive-bias) · [Inductively strong and weak](strong-weak) · [Informal fallacies](informal-fallacy)

## Sources
- Bland, *Reason* (Revised Edition), ch. 4, §4.2 p. 79 (incl. fn. 18). CC BY-NC 4.0.
- Dowden, B., "Fallacies", *Internet Encyclopedia of Philosophy*, "Gambler's". https://iep.utm.edu/fallacy/
