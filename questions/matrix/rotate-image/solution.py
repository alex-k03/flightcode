def rotate_image(matrix):
    n = len(matrix)
    rotated = [[0] * n for _ in range(n)]

    for row in range(n):
        for col in range(n):
            rotated[col][n - 1 - row] = matrix[row][col]

    return rotated
