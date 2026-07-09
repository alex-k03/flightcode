# Squares of a Sorted Array

**Difficulty:** easy

## Problem

Given an integer array `nums` sorted in non-decreasing order, return a new
array containing the square of each number, also sorted in non-decreasing
order.

## Examples

```
Input: nums = [-4, -1, 0, 3, 10]
Output: [0, 1, 9, 16, 100]
```

```
Input: nums = [-7, -3, 2, 3, 11]
Output: [4, 9, 9, 49, 121]
```

## Constraints

- 1 <= len(nums) <= 10^4
- -10^4 <= nums[i] <= 10^4
- `nums` is sorted in non-decreasing order

## Pattern note

Two pointers: the largest square must come from one of the two ends.
