from random import shuffle


class Card:
    def __init__(self, suit, rank):
        if suit in ['♣', '♢', '♡', '♠']:
            self.suit = suit
        if rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
            self.rank = rank

    def __str__(self):
        return f'{self.suit}{self.rank}'
    

class Deck:
    suits = ['♣', '♢', '♡', '♠']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    def __init__(self):
        self.deck = []
        for i in self.suits:
            for j in self.ranks:
                self.deck.append(Card(i, j))

    def shuffle(self):
        if len(self.deck) < 52:
            raise ValueError('Перемешивать можно только полную колоду')
        shuffle(self.deck)
    
    def deal(self):
        if len(self.deck) == 0:
            raise ValueError('Все карты разыграны')
        current_card = self.deck.pop(-1)
        return current_card
    
    def __str__(self):
        return f'Карт в колоде: {len(self.deck)}'


# tests

print('TEST_1:')
print(Card('♣', '4'))
print(Card('♡', 'A'))
print(Card('♢', '10'))

print('TEST_2:')
deck = Deck()

print(deck)
print(deck.deal())
print(deck.deal())
print(deck.deal())
print(type(deck.deal()))
print(deck)

print('TEST_3:')
deck = Deck()

for _ in range(52):
    deck.deal()
    
try:
    deck.deal()
except ValueError as error:
    print(error)

print('TEST_4:')
deck = Deck()

deck.deal()
    
try:
    deck.shuffle()
except ValueError as error:
    print(error)

print('TEST_5:')
deck = Deck()

for _ in range(52):
    print(deck.deal())

print('TEST_6:')
deck = Deck()

deck.shuffle()

for _ in range(52):
    print(deck.deal())