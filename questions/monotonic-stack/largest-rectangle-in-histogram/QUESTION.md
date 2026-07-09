# Largest Rectangle in Histogram

**Difficulty:** hard

## Problem

Given an array of non-negative integers `heights`, where each value is the
height of a bar in a histogram and every bar has width `1`, return the area of
the largest rectangle that can be formed inside the histogram.

A rectangle must cover one or more consecutive bars. Its height is limited by
the shortest bar it covers.

## Examples

Example 1:
```
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The rectangle covering heights 5 and 6 has height 5 and width 2.
```

Example 2:
```
Input: heights = [2,4]
Output: 4
```

## Constraints

- `1 <= len(heights) <= 10^5`
- `0 <= heights[i] <= 10^4`

## Pattern note

Monotonic stack: keep bars in increasing height order. When a shorter bar
appears, it tells you the right boundary for taller bars already on the stack.
The new top of the stack gives the left boundary.
