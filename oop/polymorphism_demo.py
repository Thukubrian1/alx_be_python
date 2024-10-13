import math
class Shape:
    def __init__(self,area):
        self.area = area

        raise NotImplementedError("derived classes need to override this metho")
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return f"{self.length * self.width}"

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return f"{math.pi * self.radius ** 2}"