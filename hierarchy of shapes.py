#mplement a program that uses inheritance to represent a hierarchy of shapes (Circle, Triangle, Rectangle, etc.).

import math

class Shape:
    def area(self):
        pass  # Abstract method to be implemented by subclasses
    
    def perimeter(self):
        pass  # Abstract method to be implemented by subclasses

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius**2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

# Example usage:
circle = Circle(5)
triangle = Triangle(3, 4, 5)
rectangle = Rectangle(4, 6)

print("Circle Area:", circle.area())
print("Circle Perimeter:", circle.perimeter())
print("Triangle Area:", triangle.area())
print("Triangle Perimeter:", triangle.perimeter())
print("Rectangle Area:", rectangle.area())
print("Rectangle Perimeter:", rectangle.perimeter())
