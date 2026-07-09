# Spiral Matrix

**Difficulty:** medium

## Problem

Given an `m x n` matrix, return all elements of the matrix in spiral order.

Start at the top-left corner, move right, then down, then left, then up, and
continue inward until every element has been visited.

## Examples

Example 1:
```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
```

Example 2:
```
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

## Constraints

- `1 <= len(matrix) <= 100`
- `1 <= len(matrix[i]) <= 100`
- Every row has the same length
- `-100 <= matrix[i][j] <= 100`

## Pattern note

Boundary simulation: maintain top, bottom, left, and right borders. After each
direction, shrink the border that was just consumed.
