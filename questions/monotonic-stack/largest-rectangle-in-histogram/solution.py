def largest_rectangle_in_histogram(heights):
    stack = []
    best = 0

    for i, height in enumerate(heights + [0]):
        while stack and heights[stack[-1]] > height:
            top = stack.pop()
            left_boundary = stack[-1] if stack else -1
            width = i - left_boundary - 1
            best = max(best, heights[top] * width)
        stack.append(i)

    return best
