def divisible_and_non_divisible_sums_difference(n, m):
    total = 0
    for value in range(1, n + 1):
        if value % m == 0:
            total -= value
        else:
            total += value
    return total
