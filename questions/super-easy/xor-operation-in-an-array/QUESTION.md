# XOR Operation in an Array

**Difficulty:** easy

## Problem

Given integers `n` and `start`, build an array where
`nums[i] = start + 2 * i` for each index `i` from `0` to `n - 1`.

Return the bitwise XOR of all values in that array.

## Examples

```
Input: n = 5, start = 0
Output: 8
```

```
Input: n = 4, start = 3
Output: 8
```

## Constraints

- 1 <= n <= 1000
- 0 <= start <= 1000

## Pattern note

Bit manipulation: generate each arithmetic-progression value and fold it into
an XOR accumulator.
