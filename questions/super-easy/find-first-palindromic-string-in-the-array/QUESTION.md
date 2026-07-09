# Find First Palindromic String in the Array

**Difficulty:** easy

## Problem

Given a list of strings `words`, return the first string that reads the same
forward and backward. If no such string exists, return an empty string.

## Examples

```
Input: words = ["abc", "car", "ada", "racecar", "cool"]
Output: "ada"
```

```
Input: words = ["notapalindrome", "racecar"]
Output: "racecar"
```

## Constraints

- 1 <= len(words) <= 100
- 1 <= len(words[i]) <= 100
- `words[i]` contains only lowercase English letters

## Pattern note

String reversal: scan from left to right and return as soon as a word equals
its reverse.
