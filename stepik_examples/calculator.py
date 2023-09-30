class Calculator:
    def __init__(self) -> None:
        pass 

    def __call__(self, a: int|float, b: int|float, operation: str):
        self.a = a
        self.b = b
        self.operation = operation
        if self.operation == '+':
            return self.a + self.b
        elif self.operation == '-':
            return self.a - self.b
        elif self.operation == '*':
            return self.a * self.b
        elif self.operation == '/':
            if self.b != 0:
                return self.a / self.b
            else:
                return 'Деление на ноль невозможно'
            

calculator = Calculator()

print(calculator(10, 0, '+'))
print(calculator(10, 0, '-'))
print(calculator(10, 0, '*'))