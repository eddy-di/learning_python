n = int(input())

matrix = [[0*n for _ in range(n)] for _ in range(n)]

if n % 2 == 0:
    for i in range(n):
        for j in range(n):
            if i<j and i < n-1-j:
                matrix[i][j] = i % n + 1
            elif i>j and i > n-1-j:
                matrix[i][j] = n % i
            elif i>j and i < n-1-j:
                matrix[i][j] = j % n + 1
            elif i<j and i > n-1-j:
                matrix[i][j] = n % j
            elif i == j and  i < n//2:
                matrix[i][j] = i % n + 1
            elif i == j and  i >= n//2:
                matrix[i][j] = n-i
            elif j == n - 1 - i and  i < n//2:
                matrix[i][j] = n-j
            elif j == n - 1 - i and  i >= n//2:
                matrix[i][j] = j % n + 1
else:
    for i in range(n):
        for j in range(n):
            if i<j and i < n-1-j:
                matrix[i][j] = i % n + 1
            elif i>j and i > n-1-j:
                matrix[i][j] = n % i
            elif i>j and i < n-1-j:
                matrix[i][j] = j % n + 1
            elif i<j and i > n-1-j:
                matrix[i][j] = n % j
            elif i == j and i < n//2:
                matrix[i][j] = i % n + 1
            elif i == j and i > n//2:
                matrix[i][j] = n-i
            elif j == n - 1 - i and i < j:
                matrix[i][j] = n-j
            elif j == n - 1 - i and i > j:
                matrix[i][j] = n-i
            else:
                matrix[i][j] = n//2+1


for row in matrix:
    print(*row)