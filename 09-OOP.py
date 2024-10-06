class Rectangle:
    sides_count = 4
    
    # dunder init
    def __init__(self, width: int, length: int):
        self.width = width
        self.length = length

    def calculate_area(self):
        return self.width * self.length

    def calculate_perimeter(self):
        return 2 * (self.width + self.length)

rect1 = Rectangle(3, 4)
rect2 = Rectangle(5, 5)

print(rect1.calculate_area())
print(rect2.calculate_area())

print(Rectangle.sides_count)