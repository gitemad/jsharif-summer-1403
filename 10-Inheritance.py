class Shape:

    def __init__(self, outline='black', fill='white'):
        self.outline = outline
        self.fill = fill

# Rectangle is a Shape
class Rectangle(Shape):
    
    def __init__(self, width, length, outline='black', fill='white'):
        super().__init__(outline, fill)

        self.width = width
        self.length = length


class Square(Rectangle):

    def __init__(self, width, outline='black', fill='white'):
        super().__init__(width, width, outline, fill)
    

class Circle(Shape):

    def __init__(self, radius, outline='black', fill='white'):
        super().__init__(outline, fill)

        self.radius = radius