# In-Class Exercises

# 1. Define and Print Variables
name = "Alice"
age = 25
is_student = True
print(f"My name is {name}, I am {age} years old, and student status: {is_student}.")

# 2. User Input and Data Conversion
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(f"The product is {num1 * num2}.")

# 3. Identify Data Types
print(type(123))      # int
print(type("hello"))  # str
print(type(3.14))     # float
print(type(True))     # bool

# 4. Perform Arithmetic Operations
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
print(f"Area of the rectangle: {length * width}")

# 5. Conditional Logic
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# 6. Even or Odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 7. For Loop with Range
for i in range(1, 11):
    print(i)

# 8. Factorial with While Loop
num = int(input("Enter a number: "))
factorial = 1
while num > 1:
    factorial *= num
    num -= 1
print(f"Factorial: {factorial}")

# 9. Function to Add Numbers
def add_numbers(a, b):
    return a + b

print(add_numbers(5, 10))

# 10. Function with Default Arguments
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()         # Hello, Guest!
greet("Alice")  # Hello, Alice!