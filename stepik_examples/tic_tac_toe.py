class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.turns = 9
        self.marked_squares = []

    def mark(self, row: int, column: int):
        coord = (row-1, column-1)
        if self.turns in range(5, 10):
            try:
                if coord not in self.marked_squares:
                    if self.turns % 2 != 0 and self.turns in range(1, 10): # X's turn
                        self.board[row-1][column-1] = 'X'
                        self.turns -= 1
                        self.marked_squares.append(coord)
                    elif self.turns % 2 == 0 and self.turns in range(1, 10): # O's turn
                        self.board[row-1][column-1] = 'O'
                        self.turns -= 1
                        self.marked_squares.append(coord)
                else:
                    raise ValueError('Недоступная клетка')
            except ValueError as e:
                print(e)
        else:
            try:
                if self.winner() == None:
                    try:
                        if coord not in self.marked_squares:
                            if self.turns % 2 != 0 and self.turns in range(1, 10): # X's turn
                                self.board[row-1][column-1] = 'X'
                                self.turns -= 1
                                self.marked_squares.append(coord)
                            elif self.turns % 2 == 0 and self.turns in range(1, 10): # O's turn
                                self.board[row-1][column-1] = 'O'
                                self.turns -= 1
                                self.marked_squares.append(coord)
                        else:
                            raise ValueError('Недоступная клетка')
                    except ValueError as e:
                        print(e)
                else:
                    raise ValueError('Игра окончена')
            except ValueError as e:
                print(e)

    def winner(self):
        board_state = self.board_state(self.board)
        if 88 in board_state:
            self.turns = -1
            return 'X'
        if 79 in board_state:
            self.turns = -1
            return 'O'
        if len(self.marked_squares) == 9 and self.turns not in range(1, 10):
            return 'Ничья'
        else:
            return None
        
    def show(self):
        temp_board = self.board[:]
        temp_board.insert(1, ['-'*5])
        temp_board.insert(3, ['-'*5])
        for r in temp_board:
            print(*r, sep="|")

    @ staticmethod
    def board_state(board):
        board_tic_tac = [[ord(board[i][j]) for j in range(3)] for i in range(3)]
        # getting all horizontal lines (up, mid, bot) sums divided by // 3
        horizontals = [sum(r) // 3 for r in board_tic_tac]
        # getting all vertical lines (left, mid, right) sums divided by // 3
        verticals = []
        for i in range(3):
            res = 0
            for j in range(3):
                res += board_tic_tac[j][i]
            verticals.append(res//3)
        # getting all diagonal main and side one's sums divided by // 3
        diagonals = []
        main_res = 0
        side_res = 0
        for i in range(3):
            main_res += board_tic_tac[i][i]
            side_res += board_tic_tac[i][3-i-1]
        diagonals.append(main_res//3)
        diagonals.append(side_res//3)
        # lines combined
        comdined_flat_results = horizontals + verticals + diagonals
        return comdined_flat_results
        

# tests

print()
print('TEST_1:')
tictactoe = TicTacToe()

tictactoe.mark(1, 1)
tictactoe.mark(3, 1)
tictactoe.mark(1, 1)

tictactoe.mark(1, 3)
tictactoe.mark(1, 2)
tictactoe.mark(3, 3)
tictactoe.mark(2, 2)
tictactoe.mark(2, 3)

print(tictactoe.winner())
tictactoe.mark(2, 1)
tictactoe.show()

print()
print('TEST_2:')
tictactoe = TicTacToe()

tictactoe.mark(1, 1)
tictactoe.mark(3, 2)
tictactoe.mark(1, 1)

tictactoe.mark(1, 3)
tictactoe.mark(1, 2)
tictactoe.mark(3, 3)
tictactoe.mark(2, 2)
tictactoe.mark(2, 3)

print(tictactoe.winner())
tictactoe.show()

print()
print('TEST_3:')
tictactoe = TicTacToe()

tictactoe.mark(1, 1)
tictactoe.mark(3, 2)
tictactoe.mark(1, 3)
tictactoe.mark(1, 2)
tictactoe.mark(3, 3)
tictactoe.mark(2, 3)
tictactoe.mark(3, 1)
tictactoe.mark(2, 1)
tictactoe.mark(2, 2)

print(tictactoe.winner())
tictactoe.show()
tictactoe.mark(2, 2)

print()
print('TEST_4:')
tictactoe = TicTacToe()

tictactoe.mark(1, 1)
tictactoe.mark(1, 3)
tictactoe.mark(3, 1)
tictactoe.mark(2, 1)

print(tictactoe.winner())

tictactoe.mark(3, 2)
tictactoe.mark(3, 3)
tictactoe.mark(1, 2)
tictactoe.mark(2, 2)
tictactoe.mark(2, 3)

print(tictactoe.winner())
tictactoe.show()
tictactoe.mark(2, 2)
print(tictactoe.winner())
