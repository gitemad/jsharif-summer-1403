# class Point:

#     def __init__(self, x, y):
#         self._x = x
#         self._y = y
    
#     def get_x(self):
#         return self._x
    
#     def set_x(self, x):
#         self._x = x
    
#     def get_y(self):
#         return self._y

#     def set_y(self, y):
#         self._y = y

# p = Point(3, 4)

# print(p.get_x())
# p.set_y(10)
# print(p.get_y())

# print(p._x)
# p._x = 20
# print(p._x)


# class Circle:

#     def __init__(self, radius):
#         self._radius = radius
    
#     def _get_radius(self):
#         return self._radius
    
#     def _set_radius(self, value):
#         if value > 0:
#             self._radius = value
    
#     def _del_radius(self):
#         del self._radius
    
#     radius = property(
#         fget=_get_radius,
#         fset=_set_radius,
#         fdel=_del_radius,
#         doc='The radius property'
#     )

# c = Circle(5)

# print(c.radius)
# c.radius = 10

# del c.radius

# class Circle:
#     def __init__(self, radius):
#         self._radius = radius

#     @property
#     def radius(self):
#         print('get radius')
#         return self._radius
    
#     @radius.setter
#     def radius(self, value):
#         print('set radius')
#         self._radius = value
    
#     @radius.deleter
#     def radius(self):
#         print('delete radius')
#         del self._radius

# c = Circle(5)

# print(c.radius)
# c.radius = 10
# print(c.radius)
# del c.radius

# class Point:
#     def __init__(self, x, y):
#         self._x = x
#         self._y = y
    
#     @property
#     def x(self):
#         return self._x
    
#     @property
#     def y(self):
#         return self._y

# p = Point(2, 6)

# print(p.x)
# p._x = 5
# print(p.x)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    @property
    def area(self):
        return self.width * self.height

r = Rectangle(2, 8)
print(r.area)