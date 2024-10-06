class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __pos__(self):
        return Point(self.x, self.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __neg__(self):
        return Point(-self.x, -self.y)
    
    def __str__(self):
        return f'({self.x}, {self.y})'
    
    def __repr__(self):
        return f'({self.x}, {self.y})'
    
    def __add__(self, other: 'Point'):
        return Point(self.x + other.x, self.y + other.y)
    
    def __iadd__(self, other: 'Point'):
        self.x += other.x
        self.y += other.y
        return self

p1 = Point(3, 4)
# p2 = +p1

# print(id(p1))
# print(id(p2))

# print(p1 is p2)
# print(p1 == p2)

# p3 = -p1
# print([p3])

p4 = Point(1, 2)

print(id(p4))
p4 += p1
print(id(p4))

print(p4)

# abs(x)
# __abs__


# round(x)
# __round__

# x + y
# __add__

# x - y
# __sub__

# x * y
# __mul__

# x // y
# __floordiv__

# x / y
# __truediv__

# x % y
# __mod__

# x ** y
# __pow__

# x < y
# __lt__

# x <= y
# __le__

# x > y
# __gt__

# x >= y
# __ge__

# x == y
# __eq__

# x != y
# __ne__

# __int__
# __float__
# __bool__
# __complex__

# __len__

# __del__