class Shape:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

class Triange(Shape):
    def square(self):
        return 0.5 * self.a * self.b

class Rectangle(Shape):
    def square(self):
        return self.a * self.b
    
rec = Rectangle(10, 20)
tr = Triange(10, 20)

print(rec.square())
print(tr.square())