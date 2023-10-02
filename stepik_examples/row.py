from typing import Any


class Row:
    def __init__(self, **kwargs):
        for arg, val in kwargs.items():
            object.__setattr__(self, arg, val)

    def __setattr__(self, attr: str, value) -> None:
        if attr in self.__dict__:
            raise AttributeError("Изменение значения атрибута невозможно")
        else:
            raise AttributeError("Установка нового атрибута невозможна")

    def __delattr__(self, attr) -> None:
        if attr in self.__dict__:
            raise AttributeError("Удаление атрибута невозможно")
        
    def __repr__(self) -> str:
        res = ", ".join([f'{k}={v!r}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({res})'
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return tuple(self.__dict__.items()) == tuple(other.__dict__.items())
        return NotImplemented
        
    def __hash__(self) -> int:
        return hash(tuple(self.__dict__.items()))



row1 = Row(a=1, b=2, c=3)
row2 = Row(a=1, b=2, c=3)
row3 = Row(b=2, c=3, a=1)

print(row1 == row2)
print(hash(row1) == hash(row2))
print(row1 == row3)
print(hash(row1) == hash(row3))
print()
print(id(row1))
print(id(row2))
