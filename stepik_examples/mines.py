from random import randrange


class Game:
    def __init__(self, rows: int, cols: int, mines: int):
        self.rows = rows
        self.cols = cols
        self.mines = mines 
        self.board = [[Cell(i, j) for j in range(self.cols)] for i in range(self.rows)]
        self.mines_coord = self.random_mine_coordinates(self.rows, self.cols, mines)
        for r, c in self.mines_coord:
            self.board[r][c].mine = True
        for i in range(self.rows):
            for j in range(self.cols):
                self.check_for_mines(i, j, self.board, self.rows, self.cols)
        for r, c in self.mines_coord:
            self.board[r][c].neighbours = 0

    @staticmethod
    def random_mine_coordinates(rows, cols, num):
        coord = []
        counter = 0
        while counter != num:
            i = (randrange(0, rows), randrange(0, cols))
            if i not in coord:
                coord.append(i)
                counter += 1
        return coord
    
    @ staticmethod
    def check_for_mines(row, col, matrix, length_rows, length_cols):
        offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]        
        for offset_row, offset_col in offsets:
            new_row, new_col = row + offset_row, col + offset_col
            if 0 <= new_row < length_rows and 0 <= new_col < length_cols:
                if matrix[new_row][new_col].mine == True:
                    matrix[row][col].neighbours += 1

class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.mine = False
        self.open = False
        self.neighbours = 0

    def __repr__(self):
        if self.mine == True:
            red_color_code = "\033[91m"
            reset_color_code = "\033[0m"
            return f'{red_color_code}({self.neighbours}){reset_color_code}'
        else:
            return f'({self.neighbours})'

# tests

game = Game(14, 18, 40)
print(game.rows)
print(game.cols)
print(game.mines)

cell = game.board[0][0]

print(cell.row)
print(cell.col)
print(0 <= cell.neighbours <= 3)
