# Valid Palindrome

**Difficulty:** easy

## Problem

Given a string `s`, return `true` if it is a palindrome after converting all
uppercase letters into lowercase letters and removing all non-alphanumeric
characters.

Alphanumeric characters include letters and numbers.

## Examples

```
Input: s = "A man, a plan, a canal: Panama"
Output: true
```

```
Input: s = "race a car"
Output: false
```

## Constraints

- 1 <= len(s) <= 2 * 10^5
- `s` consists only of printable ASCII characters

## Pattern note

Two pointers: move inward from both ends, skipping non-alphanumeric characters.
