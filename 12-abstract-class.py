from abc import ABC, abstractmethod

class Shape(ABC):

    def __init__(self, color='black'):
        self.color = color
    
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    
    def area(self):
        return 5

# shape = Shape()
rectangle = Rectangle()