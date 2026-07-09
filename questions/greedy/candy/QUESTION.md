# Candy

**Difficulty:** hard

## Problem

There are `n` children standing in a line. Each child has a rating given by
`ratings[i]`.

Give candies to the children using these rules:

- Every child must get at least one candy.
- Any child with a higher rating than an immediate neighbor must get more
  candies than that neighbor.

Return the minimum total number of candies needed.

## Examples

Example 1:
```
Input: ratings = [1,0,2]
Output: 5
Explanation: Give candies [2,1,2].
```

Example 2:
```
Input: ratings = [1,2,2]
Output: 4
Explanation: Give candies [1,2,1].
```

## Constraints

- `1 <= len(ratings) <= 2 * 10^4`
- `0 <= ratings[i] <= 2 * 10^4`

## Pattern note

Greedy local constraints: one left-to-right pass satisfies increasing slopes
from the left, and one right-to-left pass satisfies increasing slopes from the
right. Each child keeps the larger requirement.
