# Baseball Game

**Difficulty:** easy

## Problem

You are given a list of operations for a simplified baseball scoring system.
Maintain a list of valid round scores:

- An integer string records a new score.
- `"+"` records the sum of the previous two valid scores.
- `"D"` records double the previous valid score.
- `"C"` removes the previous valid score.

Return the sum of all valid scores after processing every operation.

## Examples

```
Input: operations = ["5", "2", "C", "D", "+"]
Output: 30
```

```
Input: operations = ["5", "-2", "4", "C", "D", "9", "+", "+"]
Output: 27
```

## Constraints

- 1 <= len(operations) <= 1000
- Operations are valid when processed from left to right

## Pattern note

Stack: valid scores form a history where each operation reads or mutates the
end of the list.
