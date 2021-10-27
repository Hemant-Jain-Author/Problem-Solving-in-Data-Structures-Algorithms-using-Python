from Shape import Shape
class Rectangle(Shape):
    def __init__(self, w=1, l=1):
        self.width = w
        self.length = l

    def setWidth(self, w):
        self.width = w

    def setLength(self, l):
        self.length = l

    def area(self):
        return self.width * self.length  #  Area = width * length

    def perimeter(self):
        return 2 * (self.width + self.length)  #  Perimeter = 2(width + length)

