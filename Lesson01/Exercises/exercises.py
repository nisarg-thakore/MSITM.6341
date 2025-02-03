# In-Class Exercises

# 1. Define and Print Variables
# Define two variables, string and num, and assign them proper values.
# Print a sentence containing the two variables.
# name = "Nisarg"
# age = 25
# print(f"My name is {name}, I am {age} years old")


# # 2. User Input and Data Conversion
# # Take two numbers as input from the user.
# # Convert the numbers to integers and print their sum.
# # Take two numbers as input from the user

# num1 = input("Enter the first number: ")
# num2 = input("Enter the second number: ")
# num1 = int(num1)
# num2 = int(num2)
# sum_result = num1 + num2
# print("The sum of the two numbers is:", sum_result)

# 3. Identify Data Types
# Define variables of different data types (int, float, string, boolean).
# Print the data types of the variables.

# int_var = 156        # Integer
# decimal_var = 2.16   # Float
# string_var = "hello world" # String
# bool_var = True # Boolean
# print(type(int_var))
# print(type(decimal_var))
# print(type(string_var))
# print(type(bool_var))


# 4. Perform Arithmetic Operations
# Take two numbers as input from the user.
# Perform addition, subtraction, multiplication, division, and modulus operations on the numbers.

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# addition = num1 + num2
# subtraction = num1 - num2
# multiplication = num1 * num2
# division = num1 / num2
# modulus = num1 % num2

# print("\nResults:")
# print(f"Addition: {addition}")
# print(f"Subtraction: {subtraction}")
# print(f"Multiplication: {multiplication}")
# print(f"Division: {division}")
# print(f"Modulus: {modulus}")



# 5. Conditional Logic
# Take a number as input from the user.
# If the number is positive, print "Positive".
# If the number is negative, print "Negative".
# If the number is zero, print "Zero".

# num = int(input("Enter a number: "))
# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")


# 6. Even or Odd
# Take a number as input from the user.
# If the number is even, print "Even".
# If the number is odd, print "Odd".
# Hint: Use the modulus operator (%).

# num = int(input("enter a number: "))
# if num % 2 == 0:
#          print("even")
# if num % 2 != 0:
#           print("odd")

# 7. For Loop with Range
# Print numbers from 1 to 5 using a for loop and the range function.

# for i in range(1, 6):
#     print(f"Iteration {i}")



# 8. Factorial with While Loop
# Take a number as input from the user.
# Calculate the factorial of the number using a while loop.
# Print the factorial.


# num = int(input("Enter a non-negative integer: "))

# factorial = 1
# i = 1

# while i <= num:
#     factorial *= i
#     i += 1

# print(f"The factorial of {num} is: {factorial}")


# 9. Function to Add Numbers
# Define a function that takes two numbers as input and returns their sum.
# Call the function with two numbers and print the result.

# def add_numbers(a, b):
#     return a + b

# result = add_numbers(5, 7)
# print("The sum is:", result)



# 10. Function with Default Arguments
# Define a function that takes a name as input and returns a greeting message.
# The function should have a default argument "Guest".
# Call the function with and without an argument and print the messages.

# def greet(name="Guest"):
#     return f"Hello, {name}! Welcome."


# message1 = greet("Alice")
# print(message1)


# message2 = greet()
# print(message2)
