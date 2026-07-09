def maximal_rectangle(matrix):
    if not matrix:
        return 0

    cols = len(matrix[0])
    heights = [0] * cols
    best = 0

    for row in matrix:
        for col, value in enumerate(row):
            heights[col] = heights[col] + 1 if value == "1" else 0
        best = max(best, _largest_histogram_area(heights))

    return best


def _largest_histogram_area(heights):
    stack = []
    best = 0

    for i, height in enumerate(heights + [0]):
        while stack and heights[stack[-1]] > height:
            top = stack.pop()
            left_boundary = stack[-1] if stack else -1
            best = max(best, heights[top] * (i - left_boundary - 1))
        stack.append(i)

    return best
