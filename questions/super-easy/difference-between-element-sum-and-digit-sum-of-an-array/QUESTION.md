# Difference Between Element Sum and Digit Sum of an Array

**Difficulty:** easy

## Problem

Given a list of positive integers `nums`, compute:

- the element sum: the sum of all numbers in `nums`
- the digit sum: the sum of every decimal digit across all numbers in `nums`

Return the absolute difference between those two sums.

## Examples

```
Input: nums = [1, 15, 6, 3]
Output: 9
Explanation: Element sum is 25, digit sum is 16.
```

```
Input: nums = [1, 2, 3, 4]
Output: 0
```

## Constraints

- 1 <= len(nums) <= 2000
- 1 <= nums[i] <= 2000

## Pattern note

Digit scanning: add the numbers normally, then add their digits separately.
