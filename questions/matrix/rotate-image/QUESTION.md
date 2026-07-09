# Rotate Image

**Difficulty:** medium

## Problem

Given an `n x n` matrix, return a new matrix representing the original matrix
rotated 90 degrees clockwise.

## Examples

Example 1:
```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
```

Example 2:
```
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
```

## Constraints

- `1 <= len(matrix) <= 100`
- `len(matrix) == len(matrix[i])`
- `-1000 <= matrix[i][j] <= 1000`

## Pattern note

Matrix coordinate reasoning: in a clockwise rotation, the value at old position
`(row, col)` moves to new position `(col, n - 1 - row)`.
