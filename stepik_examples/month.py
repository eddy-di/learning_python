from functools import total_ordering

@total_ordering
class Month:
    def __init__(self, year: int, month: int) -> None:
        self.year = year
        self.month = month
        self.data = (self.year, self.month)
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.year}, {self.month})'
    
    def __str__(self) -> str:
        return f'{self.year}-{self.month}'
    
    def __gt__(self, other) -> bool:
        if isinstance(other, Month):
            return self.data > other.data
        if isinstance(other, tuple):
            return self.data > other
        return NotImplemented
    
    def __lt__(self, other) -> bool:
        if isinstance(other, Month):
            return self.data < other.data
        if isinstance(other, tuple):
            return self.data < other
        return NotImplemented
    
    def __le__(self, other) -> bool:
        if isinstance(other, Month):
            return self.data <= other.data
        if isinstance(other, tuple):
            return self.data <= other
        return NotImplemented
    
    def __ge__(self, other) -> bool:
        if isinstance(other, Month):
            return self.data >= other.data
        if isinstance(other, tuple):
            return self.data >= other
        return NotImplemented

    def __eq__(self, other) -> bool:
        if isinstance(other, Month):
            return self.data == other.data
        if isinstance(other, tuple):
            return self.data == other
        return NotImplemented


month = Month(2023, 4)

print(month.__eq__(1))
print(month.__ne__(1.1))
print(month.__gt__(range(5)))
print(month.__lt__([1, 2, 3]))
print(month.__ge__({4, 5, 6}))
print(month.__le__({1: 'one'}))


