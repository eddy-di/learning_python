class Temperature:
    def __init__(self, temp_c):
        self.temperature = temp_c

    def to_fahrenheit(self):
        return round(self.temperature * (9/5) + 32, 2)
    
    @classmethod
    def from_fahrenheit(cls, temp_f):
        return cls((5/9)*(temp_f-32))
    
    def __str__(self):
        return f'{round(self.temperature, 2)}°C'
    
    def __bool__(self):
        return self.temperature > 0
    
    def __int__(self):
        return int(self.temperature)
    
    def __float__(self):
        return float(self.temperature)
    
t = Temperature.from_fahrenheit(41)

print(t)
print(int(t))
print(float(t))
print(t.to_fahrenheit())