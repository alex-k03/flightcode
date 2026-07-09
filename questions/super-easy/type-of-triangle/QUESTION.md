# Type of Triangle

**Difficulty:** easy

## Problem

Given a list `nums` containing three positive integers, decide what kind of
triangle they can form:

- Return `"equilateral"` if all three sides are equal.
- Return `"isosceles"` if exactly two sides are equal.
- Return `"scalene"` if all sides are different.
- Return `"none"` if the three lengths cannot form a triangle.

## Examples

```
Input: nums = [3, 3, 3]
Output: "equilateral"
```

```
Input: nums = [3, 4, 5]
Output: "scalene"
```

## Constraints

- len(nums) == 3
- 1 <= nums[i] <= 100

## Pattern note

Sorting: after sorting the side lengths, the triangle inequality only needs to
be checked against the two smaller sides and the largest side.
