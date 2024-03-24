#Write a Python program that uses encapsulation to protect sensitive information in a User class.

class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password  # Private attribute
    
    def set_password(self, new_password):
        self.__password = new_password
    
    def authenticate(self, username, password):
        return self.username == username and self.__password == password

# Example usage:
user = User("john_doe", "password123")

# Attempt to access password directly (will raise an AttributeError)
try:
    print("Password:", user.__password)
except AttributeError:
    print("Cannot access password directly")

# Set new password using setter method
user.set_password("new_password123")

# Authenticate user
if user.authenticate("john_doe", "new_password123"):
    print("Authentication successful")
else:
    print("Authentication failed")
