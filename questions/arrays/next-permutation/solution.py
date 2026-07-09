def next_permutation(nums):
    nums = nums[:]
    pivot = len(nums) - 2

    while pivot >= 0 and nums[pivot] >= nums[pivot + 1]:
        pivot -= 1

    if pivot >= 0:
        swap = len(nums) - 1
        while nums[swap] <= nums[pivot]:
            swap -= 1
        nums[pivot], nums[swap] = nums[swap], nums[pivot]

    nums[pivot + 1:] = reversed(nums[pivot + 1:])
    return nums
