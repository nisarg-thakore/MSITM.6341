# ----------------------------
# 1. Basic Syntax and Variables
# ----------------------------

# Defining Variables
name = "Alice"  # String
age = 30        # Integer

# Printing
print(f"Hello, my name is {name} and I am {age} years old.")

# User Input
name = input("Enter your name: ")
print(f"Hello, {name}!")

age = int(input("Enter your age: "))
print(f"You are {age} years old.")

x, y = input("Enter two numbers separated by space: ").split()
x, y = int(x), int(y)
print(f"The sum of {x} and {y} is {x + y}.")

# ----------------------------
# 2. Data Types
# ----------------------------

# Common Data Types
int_var = 5                     # int: Integer
float_var = 3.14                # float: Floating-point number
str_var = "Hello"               # str: String
bool_var = True                 # bool: Boolean
list_var = [1, 2, 3]            # list: List
tuple_var = (1, 2, 3)           # tuple: Tuple
dict_var = {"name": "Alice", "age": 30}  # dict: Dictionary

# ----------------------------
# 3. Operators
# ----------------------------

# Arithmetic Operators
a = 10
b = 3
sum_result = a + b      # Addition
diff_result = a - b     # Subtraction
prod_result = a * b     # Multiplication
quot_result = a / b     # Division
mod_result = a % b      # Modulus
exp_result = a ** b     # Exponentiation
floor_div_result = a // b  # Floor division

# Comparison Operators
is_equal = (a == b)   # Equal to
is_not_equal = (a != b)  # Not equal to
is_greater = (a > b)  # Greater than
is_less = (a < b)     # Less than
is_greater_equal = (a >= b)  # Greater than or equal to
is_less_equal = (a <= b)  # Less than or equal to

# Logical Operators
and_result = (a > 0 and b > 0)  # Logical AND
or_result = (a > 0 or b > 0)    # Logical OR
not_result = not(a > 0)         # Logical NOT

# ----------------------------
# 4. Control Structures
# ----------------------------

# If-Else Statements
number = -10
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# For Loops
for i in range(1, 11):
    print(i)

# While Loops
count = 1
while count <= 5:
    print(count)
    count += 1

# ----------------------------
# 5. Functions
# ----------------------------

# Defining Functions
def add_numbers(a, b):
    return a + b

# Calling Functions
result = add_numbers(5, 7)
print(f"The sum is {result}.")

# ----------------------------
# 6. Modules
# ----------------------------

# Creating a Module (e.g., math_utils.py)
# Save this content in a file named math_utils.py

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Importing and Using a Module
# This code goes in your main script file

from math_utils import factorial
result = factorial(5)
print(f"Factorial of 5 is {result}.")

# ----------------------------
# 7. File Handling
# ----------------------------

# Writing to a File
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a test file.\n")

# Reading from a File
with open("output.txt", "r") as file:
    content = file.read()
print("File contents:")
print(content)

# Appending to a File
with open("output.txt", "a") as file:
    file.write("Appending some more text.\n")

# ----------------------------
# 8. Classes and Objects (Basic Object-Oriented Programming)
# ----------------------------

# Defining a Class
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_stock(self, amount):
        self.quantity += amount

    def remove_stock(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
        else:
            print("Not enough stock!")

    def total_value(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.name}: ${self.price} x {self.quantity} = ${self.total_value()}"

# Creating and Using an Object
laptop = Product("Laptop", 1200.00, 5)
print(laptop)
laptop.add_stock(3)
laptop.remove_stock(2)
print(laptop)

# ----------------------------
# 9. Error Handling
# ----------------------------

# Try-Except Block
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# ----------------------------
# 10. Common Built-in Functions
# ----------------------------

# Commonly Used Functions
print(len([1, 2, 3]))        # Length of a list
print(str(123))              # Convert integer to string
print(int("123"))            # Convert string to integer
print(float("123.45"))       # Convert string to float
print(list("hello"))         # Convert string to list of characters
print(type(123))             # Get the type of an object
print(range(1, 5))           # Generate a range of numbers
print("Hello, World!")       # Print output to console

# ----------------------------
# 11. Useful Standard Library Modules
# ----------------------------

# math Module
import math
print(math.sqrt(16))  # Output: 4.0

# datetime Module
import datetime
now = datetime.datetime.now()
print(now)

# random Module
import random
print(random.randint(1, 10))  # Random integer between 1 and 10
