# PaliGemma-2

## Exploration

### Prompt Ordering

This considers the three prompts "person riding bicycle", "person,
"person on scooter" (indicated by b, p, s respectively) in different
orders. Result is Y for good, YY for very good, and N for bad, based
on a visual comparison.

| Order | Result |
|-------|--------|
| bps   | Y      |
| pbs   | N      |
| psb   | YY     |
| bsp   | Y      |
| sbp   | N      |
| spb   | N |

NB: spb is better for b since gets more.


## Futher Work

1. Try separate prompts for bicycle and scooter, with downstream
   matching with associated person to eliminate double counts.
2. Other prompts. like "person walking" instead of "person".
3. Try bigger models with quantisation to fit in. 
4. Explore 664 models.
