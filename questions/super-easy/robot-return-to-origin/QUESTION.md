# Robot Return to Origin

**Difficulty:** easy

## Problem

A robot starts at coordinate `(0, 0)`. Given a string `moves`, where each
character is one of `"U"`, `"D"`, `"L"`, or `"R"`, return `True` if the robot
ends at the origin after all moves. Otherwise, return `False`.

## Examples

```
Input: moves = "UD"
Output: True
```

```
Input: moves = "LL"
Output: False
```

## Constraints

- 1 <= len(moves) <= 2 * 10^4
- `moves` contains only `"U"`, `"D"`, `"L"`, and `"R"`

## Pattern note

Coordinate tracking: vertical and horizontal moves cancel independently.
