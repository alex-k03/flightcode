# Two Sum

**Difficulty:** easy

## Problem

Given an array of integers `nums` and an integer `target`, return the
indices of the two numbers that add up to `target`.

Exactly one solution exists; you may not use the same element twice.
Return indices in ascending order.

## Examples

```
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
```

## Constraints

- 2 <= len(nums) <= 10^4
- Only one valid answer exists

## Pattern note

Hash map: trade O(n) space for O(1) lookup of the complement.
