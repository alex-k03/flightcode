# Longest Substring Without Repeating Characters

**Difficulty:** medium

## Problem

Given a string `s`, return the length of the longest substring that contains no
repeated characters.

A substring is a contiguous sequence of characters.

## Examples

Example 1:
```
Input: s = "abcabcbb"
Output: 3
Explanation: "abc" has length 3.
```

Example 2:
```
Input: s = "bbbbb"
Output: 1
```

## Constraints

- `0 <= len(s) <= 5 * 10^4`
- `s` may contain letters, digits, symbols, and spaces

## Pattern note

Sliding window: keep a left boundary for the current no-repeat window. When a
character repeats inside the window, move the left boundary past its previous
position.
