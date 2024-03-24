#Create a class hierarchy to represent different types of electronics (Phone, Laptop) with their attributes

class Electronics:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}"

class Phone(Electronics):
    def __init__(self, brand, model, year, screen_size):
        super().__init__(brand, model, year)
        self.screen_size = screen_size
    
    def display_info(self):
        return f"Phone - {super().display_info()}, Screen size: {self.screen_size} inches"

class Laptop(Electronics):
    def __init__(self, brand, model, year, processor):
        super().__init__(brand, model, year)
        self.processor = processor
    
    def display_info(self):
        return f"Laptop - {super().display_info()}, Processor: {self.processor}"

# Example usage:
phone = Phone("Apple", "iPhone 12", 2020, 6.1)
laptop = Laptop("Dell", "XPS 15", 2021, "Intel Core i7")

print(phone.display_info())
print(laptop.display_info())
