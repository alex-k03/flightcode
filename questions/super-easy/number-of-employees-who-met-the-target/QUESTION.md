# Number of Employees Who Met the Target

**Difficulty:** easy

## Problem

Given a list `hours` where `hours[i]` is the number of hours employee `i`
worked, and an integer `target`, return how many employees worked at least
`target` hours.

## Examples

```
Input: hours = [0, 1, 2, 3, 4], target = 2
Output: 3
```

```
Input: hours = [5, 1, 4, 2, 2], target = 6
Output: 0
```

## Constraints

- 1 <= len(hours) <= 50
- 0 <= hours[i] <= 100
- 0 <= target <= 100

## Pattern note

Counting: one pass is enough, adding one for each value greater than or equal
to the target.
