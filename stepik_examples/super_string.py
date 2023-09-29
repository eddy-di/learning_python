class SuperString:
    def __init__(self, string: str) -> None:
        self.string = string

    def __str__(self):
        return f'{self.string}'
    
    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.string + other.string)
        return NotImplemented
        
    def __mul__(self, n):
        if isinstance(n, int):
            return self.__class__(self.string * n)
        return NotImplemented
    
    def __rmul__(self, n):
        return self.__mul__(n)
    
    def __truediv__(self, n):
        if isinstance(n, int):
            m = len(self.string) // n
            return self.__class__(self.string[:m])
        return NotImplemented
        
    def __lshift__(self, n):
        if isinstance(n, int) and len(self.string) > n:
            return self.__class__(self.string[:(len(self.string) - n)])
        elif isinstance(n, int) and len(self.string) <= n:
            return self.__class__(self.string[0:0])
        return NotImplemented
    
    def __rshift__(self, n):
        if isinstance(n, int) and len(self.string) > n:
            return self.__class__(self.string[n:])
        elif isinstance(n, int) and len(self.string) <= n:
            return self.__class__(self.string[0:0])
        return NotImplemented
    
superstring = SuperString('bee')
print(superstring.__add__([]))
print(superstring.__mul__(()))
print(superstring.__truediv__({}))
print(superstring.__lshift__(set()))
print(superstring.__rshift__('geek'))
