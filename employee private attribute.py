#Given a CSV file with employee details (name, position, salary), create an Employee class with private attributes

import csv

class Employee:
    def __init__(self, name, position, salary):
        self._name = name  # Private attribute
        self._position = position  # Private attribute
        self._salary = salary  # Private attribute
    
    # Getter methods to retrieve values of private attributes
    def get_name(self):
        return self._name
    
    def get_position(self):
        return self._position
    
    def get_salary(self):
        return self._salary

# Function to read employee data from CSV file
def read_employee_data(csv_file):
    employees = []
    try:
        with open(csv_file, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                name, position, salary = row
                employee = Employee(name, position, float(salary))
                employees.append(employee)
    except FileNotFoundError:
        print("File not found.")
    except ValueError:
        print("Error: Invalid data format.")

    return employees

# Example usage:
csv_file = input("Enter the path of the CSV file: ")
employee_data = read_employee_data(csv_file)
for employee in employee_data:
    print("Name:", employee.get_name())
    print("Position:", employee.get_position())
    print("Salary:", employee.get_salary())
    print()  # Print empty line for separation
