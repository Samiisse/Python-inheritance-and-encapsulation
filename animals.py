#Create a class hierarchy to represent different types of animals (Bird, Fish) with their own attributes and methods

class Animal:
    def __init__(self, species, habitat):
        self.species = species
        self.habitat = habitat
    
def eat(self):
        pass  # Abstract method to be implemented by subclasses
    
def move(self):
        pass  # Abstract method to be implemented by subclasses

class Bird(Animal):
    def __init__(self, species, habitat, wingspan):
        super().__init__(species, habitat)
        self.wingspan = wingspan
    
    def eat(self):
        return "Bird is eating insects"
    
    def move(self):
        return "Bird is flying"

class Fish(Animal):
    def __init__(self, species, habitat, water_type):
        super().__init__(species, habitat)
        self.water_type = water_type
    
    def eat(self):
        return "Fish is feeding on plankton"
    
    def move(self):
        return "Fish is swimming"

# Example usage:
bird = Bird("Sparrow", "Forest", 20)
fish = Fish("Salmon", "River", "Freshwater")

print("Bird species:", bird.species)
print("Bird habitat:", bird.habitat)
print("Bird wingspan:", bird.wingspan)
print("Bird action:", bird.move())
print("Bird eating:", bird.eat())

print("\nFish species:", fish.species)
print("Fish habitat:", fish.habitat)
print("Fish water type:", fish.water_type)
print("Fish action:", fish.move())
print("Fish eating:", fish.eat())
