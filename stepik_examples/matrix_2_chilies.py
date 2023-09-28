class Matrix:
    def __init__(self, rows, cols, value=0):
        self.rows = rows
        self.cols = cols
        self.value = value
        self.matrix = [[self.value for _ in range(self.cols)] for _ in range(self.rows)]
        
    
    def get_value(self, row, col):
        return self.matrix[row][col]
    
    def set_value(self, row, col, value):
        self.matrix[row][col] = value

    def __repr__(self):
        return f'{self.__class__.__name__}({self.rows}, {self.cols})'
    
    def __str__(self) -> str:
        if not self.__invert__():
            tot = []
            for row in self.matrix:
                tot.append(" ".join(map(str, row)))
            return "\n".join(tot)
        else:
            tot = []
            for row in self.trans:
                tot.append(" ".join(map(str, row)))
            return "\n".join(tot)
    
    def __pos__(self):
        return self.__class__(self.rows, self.cols, self.value)
    
    def __neg__(self):
        return self.__class__(self.rows, self.cols, -self.value)
    
    def __invert__(self): # doesn't return as expected 
        self.trans = [[self.value for _ in range(self.rows)] for _ in range(self.cols)]
        for i in range(self.cols):
            for j in range(self.rows):
                self.trans[i][j]
        return Matrix(self.cols, self.rows)




matrix = Matrix(4, 2)

counter = 1
for row in range(4):
    for col in range(2):
        matrix.set_value(row, col, counter)
        counter += 1

print(matrix)
print()
print(~matrix)