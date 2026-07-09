def subtract_the_product_and_sum_of_digits_of_an_integer(n):
    product = 1
    total = 0
    for digit in str(n):
        value = int(digit)
        product *= value
        total += value
    return product - total
