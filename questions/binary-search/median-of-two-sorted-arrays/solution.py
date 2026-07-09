def median_of_two_sorted_arrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    total = len(nums1) + len(nums2)
    half = (total + 1) // 2
    lo, hi = 0, len(nums1)

    while lo <= hi:
        cut1 = (lo + hi) // 2
        cut2 = half - cut1

        left1 = nums1[cut1 - 1] if cut1 > 0 else float("-inf")
        right1 = nums1[cut1] if cut1 < len(nums1) else float("inf")
        left2 = nums2[cut2 - 1] if cut2 > 0 else float("-inf")
        right2 = nums2[cut2] if cut2 < len(nums2) else float("inf")

        if left1 <= right2 and left2 <= right1:
            if total % 2 == 1:
                return max(left1, left2)
            return (max(left1, left2) + min(right1, right2)) / 2

        if left1 > right2:
            hi = cut1 - 1
        else:
            lo = cut1 + 1
