# Minimum Number Game

**Difficulty:** easy

## Problem

Given an array `nums` with an even number of integers, play this game until
the array is empty:

1. Remove the smallest number.
2. Remove the next smallest number.
3. Append those two removed numbers to the answer in reversed order.

Return the final answer array.

## Examples

```
Input: nums = [5, 4, 2, 3]
Output: [3, 2, 5, 4]
```

```
Input: nums = [2, 5]
Output: [5, 2]
```

## Constraints

- 2 <= len(nums) <= 100
- len(nums) is even
- 1 <= nums[i] <= 100

## Pattern note

Sorting: after sorting, swap every adjacent pair.
