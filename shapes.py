#Write a Python program that uses inheritance to represent a hierarchy of shapes (Triangle, Rectangle, etc.)

import math

class Shape:
    def area(self):
        pass  # Abstract method to be implemented by subclasses
    
    def perimeter(self):
        pass  # Abstract method to be implemented by subclasses

class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def area(self):
        return 0.5 * self.base * self.height
    
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

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius**2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

# Example usage:
triangle = Triangle(5, 8, 5, 6, 7)
rectangle = Rectangle(4, 6)
circle = Circle(3)

print("Triangle Area:", triangle.area())
print("Triangle Perimeter:", triangle.perimeter())
print("Rectangle Area:", rectangle.area())
print("Rectangle Perimeter:", rectangle.perimeter())
print("Circle Area:", circle.area())
print("Circle Perimeter:", circle.perimeter())
