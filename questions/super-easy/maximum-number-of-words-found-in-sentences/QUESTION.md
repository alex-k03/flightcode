# Maximum Number of Words Found in Sentences

**Difficulty:** easy

## Problem

Given a list of strings `sentences`, return the largest number of words in
any single sentence.

Words are separated by exactly one space, and each sentence has no leading or
trailing spaces.

## Examples

```
Input: sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
Output: 6
```

```
Input: sentences = ["please wait", "continue to fight", "continue to win"]
Output: 3
```

## Constraints

- 1 <= len(sentences) <= 100
- 1 <= len(sentences[i]) <= 100
- Each sentence contains lowercase English letters and spaces

## Pattern note

String splitting: split each sentence on spaces and take the maximum length.
