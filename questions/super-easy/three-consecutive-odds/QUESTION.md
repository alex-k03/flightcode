# Three Consecutive Odds

**Difficulty:** easy

## Problem

Given an integer array `arr`, return `True` if there are three consecutive
odd numbers anywhere in the array. Otherwise, return `False`.

## Examples

```
Input: arr = [2, 6, 4, 1]
Output: False
```

```
Input: arr = [1, 2, 34, 3, 4, 5, 7, 23, 12]
Output: True
```

## Constraints

- 1 <= len(arr) <= 1000
- 1 <= arr[i] <= 1000

## Pattern note

Running count: increment for odd values and reset to zero for even values.
