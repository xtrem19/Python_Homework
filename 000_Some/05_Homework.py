# Homework 5
# 5 exercises with functions

#A function to calculate the area of a circle:
print('------------------------------------------')
import math

def calculate_area(radius):
    area = math.pi * radius ** 2
    return area

radius = float(input("Enter the radius of the circle: "))
area = calculate_area(radius)
print("The area of the circle is:", area)

print('------------------------------------------')
#A function to calculate the factorial of a number:
def calculate_factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial

num = int(input("Enter a number: "))
factorial = calculate_factorial(num)
print("The factorial of", num, "is:", factorial)

print('------------------------------------------')
#A function to check if a number is prime:
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")

print('------------------------------------------')
#A function to concatenate two strings:

def concatenate_strings(str1, str2):
    return str1 + str2

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
concatenated_str = concatenate_strings(str1, str2)
print("The concatenated string is:", concatenated_str)

print('------------------------------------------')
#A function to calculate the sum of two numbers:

def calculate_sum(num1, num2):
    return num1 + num2

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sum = calculate_sum(num1, num2)
print("The sum of", num1, "and", num2, "is:", sum)

#In each of these examples, a function is defined to perform a specific task, and then called with appropriate arguments to obtain the desired result.
