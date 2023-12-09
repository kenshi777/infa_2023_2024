class Complex:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b
    
    def __str__(self) -> str:
        if self.b > 0:
            return f'{self.a}' + '+' +f'{self.b}' + 'i'
        if self.b == 0:
            return f'{self.a}'
        else:
            return f'{self.a}' + f'{self.b}' + 'i'
        

    def __add__(self, c):
        return Complex(self.a + c.a, self.b + c.b)
    
    def __sub__(self, c):
        return Complex(self.a - c.a, self.b - c.b)
    
    def __mul__(self, c):
        return Complex((self.a * c.a - self.b * c.b), (self.a * c.b + self.b * c.a))
    
    def __truediv__(self, c):
        return Complex((self.a * c.a + self.b * c.b) / (c.a ** 2 + c.b **2), (self.b * c.a - self.a * c.b) / (c.a ** 2 + c.b **2))

    def __abs__(self):
        return (self.a ** 2 + self.b ** 2) ** 0.5

a = Complex(3, 4)
b = Complex(2, -1)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(abs(a))