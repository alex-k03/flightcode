def minimum_number_game(nums):
    nums = sorted(nums)
    answer = []
    for i in range(0, len(nums), 2):
        answer.append(nums[i + 1])
        answer.append(nums[i])
    return answer
