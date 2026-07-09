def subtract_product_and_sum(n):
    product = 1
    total = 0
    for digit in str(n):
        value = int(digit)
        product *= value
        total += value
    return product - total
