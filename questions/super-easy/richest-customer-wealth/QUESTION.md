# Richest Customer Wealth

**Difficulty:** easy

## Problem

Given a 2D list `accounts`, where `accounts[i][j]` is the money customer `i`
has in bank `j`, return the largest total wealth held by any customer.

## Examples

```
Input: accounts = [[1, 2, 3], [3, 2, 1]]
Output: 6
```

```
Input: accounts = [[1, 5], [7, 3], [3, 5]]
Output: 10
```

## Constraints

- 1 <= len(accounts) <= 50
- 1 <= len(accounts[i]) <= 50
- 1 <= accounts[i][j] <= 100

## Pattern note

Row sums: each customer is one row, so sum each row and keep the maximum.
