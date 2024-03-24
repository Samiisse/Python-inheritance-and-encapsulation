#Implement a class hierarchy to represent different types of employees (Manager, Engineer) with their attributes

class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

class Manager(Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)
        self.department = department

class Engineer(Employee):
    def __init__(self, name, employee_id, specialization):
        super().__init__(name, employee_id)
        self.specialization = specialization

# Example usage:
manager = Manager("John Doe", 1001, "Marketing")
engineer = Engineer("Alice Smith", 1002, "Software Development")

print("Manager:", manager.name, "-", manager.department)
print("Engineer:", engineer.name, "-", engineer.specialization)
