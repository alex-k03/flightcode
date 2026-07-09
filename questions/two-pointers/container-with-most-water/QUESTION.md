# Container With Most Water

**Difficulty:** medium

## Problem

You are given an array `height` where `height[i]` is the height of a vertical
line at position `i`. Choose two lines to form a container with the x-axis.

Return the maximum amount of water the container can hold.

The amount of water between positions `left` and `right` is:

```
min(height[left], height[right]) * (right - left)
```

## Examples

Example 1:
```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
```

Example 2:
```
Input: height = [1,1]
Output: 1
```

## Constraints

- `2 <= len(height) <= 10^5`
- `0 <= height[i] <= 10^4`

## Pattern note

Two pointers: start with the widest container. Moving the taller wall inward
cannot improve the limiting height, so move the shorter wall and keep the best
area seen.
