# Number of Changing Keys

**Difficulty:** easy

## Problem

Given a string `s` typed on a keyboard, count how many times the pressed key
changes from one character to the next.

Comparison is case-insensitive, so `"a"` and `"A"` are the same key.

## Examples

```
Input: s = "aAbBcC"
Output: 2
```

```
Input: s = "AaAaAaaA"
Output: 0
```

## Constraints

- 1 <= len(s) <= 100
- `s` contains only English letters

## Pattern note

Adjacent comparison: normalize case and compare each character with the
previous one.
