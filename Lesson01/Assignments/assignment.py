# 1. Simple Calculator
# Write a simple calculator that takes two numbers and an operator (+, -, *, /) as input and returns the result of the operation.

# Psedo Code:
# 1. Take two numbers and an operator as input.
# 2. Perform the operation based on the operator.
# 3. Print the result.

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")

select = int(input("Select operations form 1, 2, 3, 4 :"))

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

if select == 1:
    print(number_1, "+", number_2, "=",
                    add(number_1, number_2))

elif select == 2:
    print(number_1, "-", number_2, "=",
                    subtract(number_1, number_2))

elif select == 3:
    print(number_1, "*", number_2, "=",
                    multiply(number_1, number_2))

elif select == 4:
    print(number_1, "/", number_2, "=",
                    divide(number_1, number_2))
else:
    print("Invalid input")


  
# 2. Area of a Rectangle
# Write a program that takes the length and width of a rectangle as input and calculates the area of the rectangle.

# Psedo Code:
# 1. Take the length and width of the rectangle as input.
# 2. Calculate the area of the rectangle.
# 3. Print the area.

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
print("The area of the rectangle is:", area)

