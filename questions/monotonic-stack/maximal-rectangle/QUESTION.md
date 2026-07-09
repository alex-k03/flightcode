# Maximal Rectangle

**Difficulty:** hard

## Problem

Given a binary matrix represented as a list of equal-length strings, return the
area of the largest rectangle containing only `1`s.

Each string contains only the characters `"0"` and `"1"`.

## Examples

Example 1:
```
Input: matrix = ["10100","10111","11111","10010"]
Output: 6
Explanation: The largest all-1 rectangle has area 6.
```

Example 2:
```
Input: matrix = ["1"]
Output: 1
```

## Constraints

- `0 <= len(matrix) <= 200`
- If `matrix` is non-empty, `1 <= len(matrix[i]) <= 200`
- Every row has the same length
- `matrix[i][j]` is `"0"` or `"1"`

## Pattern note

Monotonic stack plus row compression: treat each row as the bottom of a
histogram. Consecutive `1`s above that row become bar heights, then solve the
largest-rectangle-in-histogram problem for each row.
