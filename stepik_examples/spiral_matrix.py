def generate_spiral_matrix(n, m):
    matrix = [[0] * m for _ in range(n)]

    left, right, top, bottom = 0, m - 1, 0, n - 1
    num = 1

    while num <= n * m:
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1

        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1

    return matrix


n, m = (int(i) for i in input().split())
result = generate_spiral_matrix(n, m)
for row in result:
    print(row)
