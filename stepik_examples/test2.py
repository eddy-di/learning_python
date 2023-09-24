for i in range(8):
    for j in range(8):
        board[row][col] = 'N'
        if (row - 2 < row and col - 1 < col) and (row - 2 > -1 and col - 1 > -1):
            board[row-2][col-1] = '*'
        if (row + 2 > row and col - 1 < col) and (row + 2 < 8 and col - 1 > -1):
            board[row+2][col-1] = '*'
        if (row - 1 < row and col - 2 < col) and (col - 2 > -1 and row - 1 > -1):
            board[row-1][col-2] = '*'
        if (row + 1 > row and col - 2 < col) and (col - 2 > -1 and row + 1 < 8):
            board[row+1][col-2] = '*'
        if (row - 2 < row and col + 1 > col) and (row - 2 > -1 and col + 1 < 8):
            board[row-2][col+1] = '*'
        if (row + 2 > row and col + 1 > col) and (row + 2 < 8 and col + 1 < 8):
            board[row+2][col+1] = '*'
        if (row - 1 < row and col + 2 > col) and (row - 1 > -1 and col + 2 < 8):
            board[row-1][col+2] = '*'
        if (row + 1 > row and col + 2 > col) and (row + 1 < 8 and col + 2 < 8):
            board[row+1][col+2] = '*'
            

for r in board:
    print(*r)