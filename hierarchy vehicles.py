#Implement a program that uses inheritance to represent a hierarchy of vehicles (Car, Bike, Truck, etc.)0

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}"

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors
    
    def display_info(self):
        return f"Car - {super().display_info()}, Number of doors: {self.num_doors}"

class Bike(Vehicle):
    def __init__(self, make, model, year, bike_type):
        super().__init__(make, model, year)
        self.bike_type = bike_type
    
    def display_info(self):
        return f"Bike - {super().display_info()}, Bike type: {self.bike_type}"

class Truck(Vehicle):
    def __init__(self, make, model, year, load_capacity):
        super().__init__(make, model, year)
        self.load_capacity = load_capacity
    
    def display_info(self):
        return f"Truck - {super().display_info()}, Load capacity: {self.load_capacity} tons"

# Example usage:
car = Car("Toyota", "Camry", 2020, 4)
bike = Bike("Honda", "CBR1000RR", 2021, "Sport")
truck = Truck("Ford", "F-150", 2019, 2)

print(car.display_info())
print(bike.display_info())
print(truck.display_info())
