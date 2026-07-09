def difference_between_element_sum_and_digit_sum_of_an_array(nums):
    element_sum = sum(nums)
    digit_sum = 0
    for num in nums:
        for digit in str(num):
            digit_sum += int(digit)
    return abs(element_sum - digit_sum)
