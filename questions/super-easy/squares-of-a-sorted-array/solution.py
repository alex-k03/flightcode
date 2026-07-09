def squares_of_a_sorted_array(nums):
    left = 0
    right = len(nums) - 1
    answer = [0] * len(nums)

    for pos in range(len(nums) - 1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            answer[pos] = nums[left] * nums[left]
            left += 1
        else:
            answer[pos] = nums[right] * nums[right]
            right -= 1
    return answer
