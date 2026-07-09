def xor_operation_in_an_array(n, start):
    result = 0
    for i in range(n):
        result ^= start + 2 * i
    return result
