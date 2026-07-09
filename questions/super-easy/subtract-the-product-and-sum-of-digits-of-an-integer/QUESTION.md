# Subtract the Product and Sum of Digits of an Integer

**Difficulty:** easy

## Problem

Given a positive integer `n`, return the product of its digits minus the sum
of its digits.

## Examples

```
Input: n = 234
Output: 15
Explanation: 2 * 3 * 4 - (2 + 3 + 4) = 24 - 9.
```

```
Input: n = 4421
Output: 21
```

## Constraints

- 1 <= n <= 10^5

## Pattern note

Digit scanning: keep one accumulator for product and one for sum.
