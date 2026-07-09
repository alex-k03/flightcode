# Next Permutation

**Difficulty:** medium

## Problem

Given a list of integers `nums`, return the next lexicographically greater
permutation of the list.

If no greater permutation exists, return the lowest possible order instead.

Do not sort all permutations.

## Examples

Example 1:
```
Input: nums = [1,2,3]
Output: [1,3,2]
```

Example 2:
```
Input: nums = [3,2,1]
Output: [1,2,3]
```

## Constraints

- `1 <= len(nums) <= 100`
- `0 <= nums[i] <= 100`

## Pattern note

Suffix reasoning: find the first position from the right that can be increased.
Swap it with the smallest larger value in the suffix, then reverse the suffix
to make the result as small as possible.
