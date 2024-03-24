#Create a class Person with private attributes and define methods to get and set the values of those attributes.

class Person:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute
    
    # Getter methods to retrieve values of private attributes
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    # Setter methods to set values of private attributes
    def set_name(self, name):
        self.__name = name
    
    def set_age(self, age):
        self.__age = age

# Example usage:
person = Person("Alice", 30)

# Accessing private attributes using getter methods
print("Name:", person.get_name())
print("Age:", person.get_age())

# Modifying private attributes using setter methods
person.set_name("Bob")
person.set_age(25)

print("\nModified values:")
print("Name:", person.get_name())
print("Age:", person.get_age())
