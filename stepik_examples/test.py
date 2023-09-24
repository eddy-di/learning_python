class Knight:
    def __init__(self, horizontal: str, vertical: int, color):
        self.horizontal = horizontal
        self.vertical = vertical
        self.color = color

    def get_char(self):
        self.knight_char = 'N'
        return self.knight_char
    
    def can_move(self, horizontal_can_move: str, vertical_can_move: int):
        self.horizontal_can_move = horizontal_can_move
        self.vertical_can_move = vertical_can_move
        self.x1, self.y1 = ord(self.horizontal) - 96, self.vertical
        self.x2, self.y2 = ord(self.horizontal_can_move) - 96, self.vertical_can_move
        if abs(self.x1 - self.x2) == 1 and abs(self.y1 - self.y2) == 2:
            return True
        elif abs(self.x1 - self.x2) == 2 and abs(self.y1 - self.y2) == 1:
            return True
        else:
            return False
        
    def move_to(self, hor_move: str, ver_move: int):
        self.horizontal_move = hor_move
        self.vertical_move = ver_move
        if self.can_move(self.horizontal_move, self.vertical_move):
            self.horizontal = self.horizontal_move
            self. vertical = self.vertical_move
        else:
            pass

    def draw_board(self):
        board = [['.'] * 8 for _ in range(8)]
        x = ord(self.horizontal) - 97
        y = 8 - self.vertical
        board[y][x] = self.get_char()

        for i in range(8):
            for j in range(8):
                if abs(y - i) * abs(x - j) == 2:
                    board[i][j] = '*'

        for r in board:
            print(''.join(r))


knight = Knight('h', 1, 'black')
knight.draw_board()