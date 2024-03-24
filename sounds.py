#Create a base class Animal with a method sound() and create derived classes Dog and Cat with their own sound().

class Animal:
    def sound(self):
        pass  # This method will be overridden by subclasses

class Dog(Animal):
    def sound(self):
        return "Woof"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Example usage:
dog = Dog()
cat = Cat()

print("Dog says:", dog.sound())
print("Cat says:", cat.sound())
