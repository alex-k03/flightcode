# Product of Array Except Self

**Difficulty:** medium

## Problem

Given an integer array `nums`, return an array `answer` where `answer[i]` is the
product of every value in `nums` except `nums[i]`.

Do not use division.

## Examples

Example 1:
```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
```

Example 2:
```
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

## Constraints

- `2 <= len(nums) <= 10^5`
- `-30 <= nums[i] <= 30`
- The product of any prefix or suffix fits in a 32-bit signed integer

## Pattern note

Prefix and suffix products: the product excluding `i` is everything to its left
times everything to its right. You can build those two pieces without division.
