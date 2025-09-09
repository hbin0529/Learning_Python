# Create a Program from calculator

# What we do in calc
# We take 2 input then we do required operations
"""
num1 = eval(input("Enter first number: "))
num2 = eval(input("Enter second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2


print("두 숫자의 합은 :", addition, "입니다!!")
print("두 숫자의 차는 :", subtraction, "입니다!!")
print("두 숫자의 곱은 :", multiplication, "입니다!!")
print("두 숫자의 나눗셈은 :", division, "입니다!!")
"""

##############################

num1 = eval(input("Enter first number: "))
num2 = eval(input("Enter second number: "))

def addition(num1, num2):
    print("두 숫자의 합은 :", num1 + num2, "입니다!!")


def subtraction(num1, num2):
    print("두 숫자의 차는 :", num1 - num2, "입니다!!")


def multiplication(num1, num2):
    print("두 숫자의 곱은 :", num1 * num2, "입니다!!")


def division(num1, num2):
    print("두 숫자의 나눗셈은 :", num1 / num2, "입니다!!")


addition(num1, num2)
subtraction(num1, num2)
multiplication(num1, num2)
division(num1, num2)



















