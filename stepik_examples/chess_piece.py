from abc import ABC, abstractmethod


class ChessPiece(ABC):
    def __init__(self, horizontal: str, vertical: int):
        self.horizontal = horizontal
        self.vertical = vertical
        self.horizontal_position = 96 - ord(horizontal)
        

    @abstractmethod
    def can_move(self):
        return NotImplemented
    

class King(ChessPiece):
    def can_move(self, hor: str, ver: int):
        hor_coord = 96 - ord(hor)
        ver_coord = ver
        if self.horizontal_position == hor_coord and self.vertical == ver_coord:
            return False
        else:
            return (-1 <= self.horizontal_position - hor_coord <= 1) and (-1 <= self.vertical - ver_coord <= 1)
    

class Knight(ChessPiece):
    def can_move(self, hor: str, ver: int):
        hor_coord = 96 - ord(hor)
        ver_coord = ver
        if self.horizontal_position == hor_coord and self.vertical == ver_coord:
            return False
        else:
            return (self.horizontal_position - hor_coord)**2 + (self.vertical - ver_coord)**2 == 5
    

# tests

# print('TEST_1:')
# king = King('b', 2)
# 
# print(king.can_move('c', 3))
# print(king.can_move('a', 1))
# print(king.can_move('f', 7))
# 
# print('TEST_2:')
# knight = Knight('c', 3)
# 
# print(knight.can_move('e', 5))
# print(knight.can_move('e', 4))
# 
# print('TEST_3:')
# king = King('e', 3)
# 
# print(king.can_move('e', 3))
# print(king.can_move('e', 4))
# print(king.can_move('b', 1))
# 
# print('TEST_4:')
# knight = Knight('h', 8)
# 
# print(knight.can_move('h', 8))
# print(knight.can_move('a', 6))
# print(knight.can_move('a', 1))
# print(knight.can_move('g', 6))
# 
# print('TEST_5:')
# knight = Knight('a', 1)
# 
# for horizontal in 'abcdefg':
    # for vertical in range(1, 9):
        # print(f'{horizontal}{vertical}', knight.can_move(horizontal, vertical))
# 
print('TEST_6:')
king = King('a', 1)

for horizontal in 'abcdefg':
    for vertical in range(1, 9):
        print(f'{horizontal}{vertical}', king.can_move(horizontal, vertical))

print('TEST_7:')
kings = [King(h, v) for h in 'abcdefgh' for v in range(1, 9)]

for king in kings:
    print('*' * 20)
    for horizontal in 'abcdefgh':
        for vertical in range(1, 9):
            if king.can_move(horizontal, vertical):
                print(f'King({king.horizontal}{king.vertical})', f'{horizontal}{vertical}',
                      king.can_move(horizontal, vertical))

print('TEST_8:')
knights = [Knight(h, v) for h in 'abcdefgh' for v in range(1, 9)]

for knight in knights:
    print('*' * 20)
    for horizontal in 'abcdefgh':
        for vertical in range(1, 9):
            if knight.can_move(horizontal, vertical):
                print(f'Knight({knight.horizontal}{knight.vertical})', f'{horizontal}{vertical}',
                      knight.can_move(horizontal, vertical))