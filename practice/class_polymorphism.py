class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width
    def area(self):
        return self.height * self.width 

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius

shapes = [Rectangle(2, 4), Circle(10)]

for shape in shapes:
    print(shape.area())