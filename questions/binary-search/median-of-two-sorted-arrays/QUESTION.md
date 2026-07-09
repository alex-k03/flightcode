# Median of Two Sorted Arrays

**Difficulty:** hard

## Problem

Given two sorted arrays `nums1` and `nums2`, return the median of the two sorted
arrays combined.

The arrays may have different lengths. At least one array is non-empty.

Your solution should run in `O(log(min(m, n)))` time, where `m` and `n` are the
lengths of the two arrays.

## Examples

Example 1:
```
Input: nums1 = [1,3], nums2 = [2]
Output: 2
```

Example 2:
```
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.5
```

## Constraints

- `0 <= len(nums1), len(nums2) <= 1000`
- `1 <= len(nums1) + len(nums2) <= 2000`
- `-10^6 <= nums1[i], nums2[i] <= 10^6`
- `nums1` and `nums2` are sorted in non-decreasing order

## Pattern note

Binary search on a partition: choose how many values come from the smaller
array so the left half and right half have valid boundaries. The median is then
determined only by the boundary values around that partition.
