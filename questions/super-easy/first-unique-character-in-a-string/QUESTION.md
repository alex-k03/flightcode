# First Unique Character in a String

**Difficulty:** easy

## Problem

Given a string `s`, return the index of the first character that appears
exactly once. If every character appears more than once, return `-1`.

## Examples

```
Input: s = "leetcode"
Output: 0
```

```
Input: s = "loveleetcode"
Output: 2
```

```
Input: s = "aabb"
Output: -1
```

## Constraints

- 1 <= len(s) <= 10^5
- `s` contains only lowercase English letters

## Pattern note

Character counting: count frequencies first, then scan from left to right to
find the earliest count of one.
