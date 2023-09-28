class ReversibleString:
    def __init__(self, text) -> None:
        self.string = text

    def __str__(self):
        return self.string
    
    def __neg__(self):
        return ReversibleString(self.string[::-1])


string = ReversibleString('beegeek')

print(-string)
print(type(-string))