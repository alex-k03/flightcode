def count_the_digits_that_divide_a_number(num):
    original = num
    count = 0
    while num:
        digit = num % 10
        if original % digit == 0:
            count += 1
        num //= 10
    return count
