# Divisible and Non-divisible Sums Difference

**Difficulty:** easy

## Problem

Given positive integers `n` and `m`, compute:

- `num1`: the sum of integers from `1` to `n` that are not divisible by `m`
- `num2`: the sum of integers from `1` to `n` that are divisible by `m`

Return `num1 - num2`.

## Examples

```
Input: n = 10, m = 3
Output: 19
```

```
Input: n = 5, m = 6
Output: 15
```

## Constraints

- 1 <= n, m <= 1000

## Pattern note

Partitioned sum: scan `1..n` and add or subtract each value based on
divisibility.
