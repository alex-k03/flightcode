# Count the Digits That Divide a Number

**Difficulty:** easy

## Problem

Given an integer `num`, count how many of its digits divide `num` evenly.

The input will not contain the digit `0`.

## Examples

```
Input: num = 121
Output: 2
Explanation: 1 and 1 divide 121, but 2 does not.
```

```
Input: num = 1248
Output: 4
```

## Constraints

- 1 <= num <= 10^9
- `num` does not contain the digit `0`

## Pattern note

Digit scanning: keep the original number, then inspect each digit with
division and modulo.
