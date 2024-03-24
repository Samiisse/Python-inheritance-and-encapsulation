#Implement a class hierarchy to represent different types of vehicles (Car, Bike) with their own attributes and methods.

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def drive(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors
    
    def drive(self):
        return f"{self.make} {self.model} (Car) is driving"

class Bike(Vehicle):
    def __init__(self, make, model, year, bike_type):
        super().__init__(make, model, year)
        self.bike_type = bike_type
    
    def drive(self):
        return f"{self.make} {self.model} ({self.bike_type} Bike) is cycling"

# Example usage:
car = Car("Toyota", "Camry", 2020, 4)
bike = Bike("Giant", "Defy", 2019, "Road")

print(car.drive())
print(bike.drive())

