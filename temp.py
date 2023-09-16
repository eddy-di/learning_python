
def matrix(n=0, m=0, value=0):
    matrix = []
    if n == 0 and m == 0:
        matrix.append([])
    elif n > 0 and m == 0:
        for _ in range(n):
            temp1 = []
            for _ in range(n):
                temp1.append(value)
            matrix.append(temp1)
    elif n > 0 and m > 0:
        for _ in range(n):
            temp2 = []
            for _ in range(m):
                temp2.append(value)
            matrix.append(temp2)
    elif (n > 0 and m > 0) and value > 0:
        for i in range(n):
            temp3 = []
            for j in range(m):
                temp3.append(value)
            matrix.append(temp3)

    return matrix

print(matrix(3, 4, -1))