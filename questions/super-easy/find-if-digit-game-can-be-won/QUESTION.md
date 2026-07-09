# Find if Digit Game Can Be Won

**Difficulty:** easy

## Problem

Given a list of positive integers `nums`, Alice can choose either all
single-digit numbers or all double-digit numbers from the list.

Alice wins if the sum of the chosen group is strictly greater than the sum of
the remaining numbers. Return `True` if Alice can win, otherwise return
`False`.

## Examples

```
Input: nums = [1, 2, 3, 4, 10]
Output: False
```

```
Input: nums = [1, 2, 3, 4, 5, 14]
Output: True
```

## Constraints

- 1 <= len(nums) <= 100
- 1 <= nums[i] <= 99

## Pattern note

Grouped sums: compare the sum of one-digit values against the sum of two-digit
values. Alice wins if either group has the larger sum.
