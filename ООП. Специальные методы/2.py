class Vector:

    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return str((self.x, self.y, self.z))
    
    def __add__(self, c):
        return Vector(self.x + c.x, self.y + c.y, self.z + c.z)
    
    def __sub__(self, c):
        return Vector(self.x - c.x, self.y - c.y, self.z - c.z)
    
    def __mul__(self, c):
        if type(c) == Vector:
            return self.x * c.x + self.y * c.y + self.z * c.z
        else:
            return Vector(c * self.x, c * self.y, c * self.z)

    def __matmul__(self, c):
        return Vector(self.y * c.z - self.z * c.y, self.z * c.x - self.x * c.z, self.x * c.y - self.y * c.x)
    
    def __abs__(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
    

L = [
    (1.2, 2.4, 3.6),
    (-0.5, 2.0, 4.8),
    (3.0, 1.5, -2.7),
    (-2.3, 0.7, 5.2),
    (2.1, -3.0, 1.8),
    (0.0, 2.5, -1.0),
    (-1.8, 1.2, 2.9),
    (3.3, -2.6, 0.5),
    (0.8, 0.2, -4.0),
    (-2.4, -1.1, -0.9)
]

d = 0
p = None
for point in L:
    a = Vector(point[0], point[1], point[2])
    if abs(a) >= d:
        d = abs(a)
        p = point
print(point, d)


m1 = 10
m2 = 20
m3 = 30

a = Vector(1, 2, 3)
b = Vector(2, 3, 6)
c = Vector(3, 2, 1)

print((a*m1 + b*m2 + c*m3) * (1 / (m1 + m2 +m3)))

print(abs(a @ b))
print(a * (b @ c))

m = 0
for i in L:
    for j in L:
        for k in L:
            a = Vector(i[0], i[1], i[2])
            b = Vector(j[0], j[1], j[2])
            c = Vector(k[0], k[1], k[2])
            per = abs(b - a) + abs(c - b) + abs(a - c)
            if per >= m:
                m = per
print(m)

m = 0
for i in L:
    for j in L:
        for k in L:
            a = Vector(i[0], i[1], i[2])
            b = Vector(j[0], j[1], j[2])
            c = Vector(k[0], k[1], k[2])
            s = 0.5 * abs((b - a) @ (c - a))
            if s >= m:
                m = s
print(m)

