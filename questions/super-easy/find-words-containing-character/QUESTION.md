# Find Words Containing Character

**Difficulty:** easy

## Problem

Given a list of strings `words` and a character `x`, return the indices of
all words that contain `x`.

Return the indices in increasing order.

## Examples

```
Input: words = ["leet", "code"], x = "e"
Output: [0, 1]
```

```
Input: words = ["abc", "bcd", "aaaa", "cbc"], x = "a"
Output: [0, 2]
```

## Constraints

- 1 <= len(words) <= 50
- 1 <= len(words[i]) <= 50
- `x` and every `words[i]` contain only lowercase English letters

## Pattern note

Linear scan: check membership for each word and collect matching indices.
