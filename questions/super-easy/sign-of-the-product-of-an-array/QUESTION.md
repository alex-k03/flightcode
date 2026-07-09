# Sign of the Product of an Array

**Difficulty:** easy

## Problem

Given an integer array `nums`, return the sign of the product of all numbers:

- Return `1` if the product is positive.
- Return `-1` if the product is negative.
- Return `0` if the product is zero.

You do not need to compute the full product.

## Examples

```
Input: nums = [-1, -2, -3, -4, 3, 2, 1]
Output: 1
```

```
Input: nums = [1, 5, 0, 2, -3]
Output: 0
```

## Constraints

- 1 <= len(nums) <= 1000
- -100 <= nums[i] <= 100

## Pattern note

Sign tracking: zero decides immediately; otherwise the parity of negative
values decides the sign.
