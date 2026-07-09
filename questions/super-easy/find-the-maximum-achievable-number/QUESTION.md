# Find the Maximum Achievable Number

**Difficulty:** easy

## Problem

Given integers `num` and `t`, you may perform exactly `t` operations.

In each operation, you can increase `num` by `1` while decreasing another
number by `1`. Return the largest value that can be made equal to `num` after
exactly `t` operations.

## Examples

```
Input: num = 4, t = 1
Output: 6
```

```
Input: num = 3, t = 2
Output: 7
```

## Constraints

- 1 <= num, t <= 50

## Pattern note

Arithmetic: each operation can close the gap by two, so add `2 * t`.
