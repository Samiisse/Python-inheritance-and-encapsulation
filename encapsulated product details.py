#Given a JSON file with product details (name, price, quantity), create a Product class with encapsulated attributes

import json

class Product:
    def __init__(self, name, price, quantity):
        self._name = name
        self._price = price
        self._quantity = quantity
    
    @property
    def name(self):
        return self._name
    
    @property
    def price(self):
        return self._price
    
    @property
    def quantity(self):
        return self._quantity

    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"

# Function to read product data from JSON file
def read_product_data(json_file):
    products = []
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
            for entry in data['products']:
                product = Product(entry['name'], entry['price'], entry['quantity'])
                products.append(product)
    except FileNotFoundError:
        print("File not found.")
    except KeyError:
        print("Invalid JSON format. Missing required fields.")

    return products

# Example usage:
json_file = input("Enter the path of the JSON file: ")
product_data = read_product_data(json_file)
for product in product_data:
    print(product)
