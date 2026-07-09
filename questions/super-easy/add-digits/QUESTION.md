# Add Digits

**Difficulty:** easy

## Problem

Given a non-negative integer `num`, repeatedly add all of its digits until
only one digit remains. Return that final single-digit value.

## Examples

```
Input: num = 38
Output: 2
Explanation: 3 + 8 = 11, then 1 + 1 = 2.
```

```
Input: num = 0
Output: 0
```

## Constraints

- 0 <= num <= 2^31 - 1

## Pattern note

Digit math: the repeated digit sum is the digital root. It can be solved with
simulation or a constant-time modulo observation.
