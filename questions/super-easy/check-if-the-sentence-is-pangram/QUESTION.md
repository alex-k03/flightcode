# Check if the Sentence Is Pangram

**Difficulty:** easy

## Problem

Given a string `sentence`, return `True` if it contains every lowercase
English letter at least once. Otherwise, return `False`.

## Examples

```
Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: True
```

```
Input: sentence = "leetcode"
Output: False
```

## Constraints

- 1 <= len(sentence) <= 1000
- `sentence` contains only lowercase English letters

## Pattern note

Set membership: collect the letters seen and check whether there are 26.
