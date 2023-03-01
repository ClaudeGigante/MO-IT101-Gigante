# Import necessary libraries
import os

# Define username and password
username = "user"
password = "user"

# Clear console screen
os.system('cls' if os.name == 'nt' else 'clear')

# Ask for user input
input_username = input("Enter username: ")
input_password = input("Enter password: ")

# Check if username and password are correct
if input_username == username and input_password == password:
    print("Login successful!")
else:
    print("Incorrect username or password.")