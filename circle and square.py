#Create a base class Shape with methods to calculate area and perimeter, and derive classes Circle and Square

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

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length
    
    def area(self):
        return self.side_length**2
    
    def perimeter(self):
        return 4 * self.side_length

# Example usage:
circle = Circle(5)
square = Square(4)

print("Circle Area:", circle.area())
print("Circle Perimeter:", circle.perimeter())
print("Square Area:", square.area())
print("Square Perimeter:", square.perimeter())
