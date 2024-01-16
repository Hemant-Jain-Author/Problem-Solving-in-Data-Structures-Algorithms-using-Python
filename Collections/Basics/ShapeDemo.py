from Circle import Circle
from Rectangle import Rectangle

width = 2
length = 3
rectangle = Rectangle(width, length)
print(("Rectangle width:" , width , "and length:" , length , "Area:" , rectangle.area() , "Perimeter:" , rectangle.perimeter()))

radius = 10
circle = Circle(radius)
print(("Circle radius:" , radius, "Area:" , circle.area(), "Perimeter:" , circle.perimeter()))

