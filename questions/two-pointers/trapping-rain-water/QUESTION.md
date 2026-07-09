# Trapping Rain Water

**Difficulty:** hard

## Problem

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

## Examples

Example 1:
```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water are being trapped.
```

Example 2:
```
Input: height = [4,2,0,3,2,5]
Output: 9
```

## Constraints

- `n == height.length`
- `1 <= n <= 2 * 10^4`
- `0 <= height[i] <= 10^5`

## Pattern note

Two pointers: maintain pointers at both ends, tracking the maximum heights seen so far from both sides. The water trapped at each index is determined by `min(max_left, max_right) - height[i]`.
