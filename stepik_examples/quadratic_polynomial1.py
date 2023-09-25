class QuadraticPolynomial:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def from_iterable(cls, iterable):
        return cls(iterable[0], iterable[1], iterable[2])
    
    @classmethod
    def from_str(cls, text):
        a, b, c = text.split()
        return cls(float(a), float(b), float(c))
    

polynom = QuadraticPolynomial.from_str('-1.5 4 14.8')

print(polynom.a)
print(polynom.b)
print(polynom.c)
print(polynom.a + polynom.b + polynom.c)

