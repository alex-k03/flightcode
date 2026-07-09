def difference_of_sums(n, m):
    total = 0
    for value in range(1, n + 1):
        if value % m == 0:
            total -= value
        else:
            total += value
    return total
