from math import sqrt

class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def view(self):
        if self.b < 0:
            return f'{self.a}x^2 - {abs(self.b)}x + {self.c}'
        elif self.c < 0:
            return f'{self.a}x^2 + {abs(self.b)}x - {abs(self.c)}'
        else:
            return f'{self.a}x^2 + {self.b}x + {self.c}'
    
    @property
    def coefficients(self) -> tuple:
        return self.a, self.b, self.c
    
    @coefficients.setter
    def coefficients(self, coefs):
        self.a = coefs[0]
        self.b = coefs[1]
        self.c = coefs[2]

    @property
    def x1(self):
        if self.b**2 - (4 * self.a * self.c) < 0:
            return None
        else:
            return (-self.b - sqrt(self.b**2 - (4 * self.a * self.c))) / (2 * self.a)
        
    @property
    def x2(self):
        if self.b**2 -(4 * self.a * self.c) < 0:
            return None
        else:
            return (-self.b + sqrt(self.b**2 - (4 * self.a * self.c))) / (2 * self.a)
        

polynom = QuadraticPolynomial(500, -601, 101)

print(polynom.a, polynom.b, polynom.c)
print(polynom.x1)
print(polynom.x2)
print(polynom.coefficients)
print(polynom.view)

print()

polynom.coefficients = (-1000, 1202, -202)
print(polynom.a, polynom.b, polynom.c)
print(polynom.x1)
print(polynom.x2)
print(polynom.coefficients)
print(polynom.view)