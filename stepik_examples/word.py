from functools import total_ordering

@total_ordering
class Word:
    def __init__(self, string: str) -> None:
        self.word = string

    def __eq__(self, other) -> bool:
        if isinstance(other, Word):
            return len(self.word) == len(other.word)
        return NotImplemented
    
    def __lt__(self, other) -> bool:
        if isinstance(other, Word):
            return len(self.word) < len(other.word)
        return NotImplemented
    
    def __str__(self):
        return f'{self.word.title()}'
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.word!r})'
    

words = [Word('python'), Word('bee'), Word('geek')]

print(sorted(words))
print(min(words))
print(max(words))