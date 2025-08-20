# Task 2: Using the Math Module for Calculations
 
# Problem Statement: Write a Python program that:
# 1.   Asks the user for a number as input.
# 2.   Uses the math module to calculate the:
# o   Square root of the number
# o   Natural logarithm (log base e) of the number
# o   Sine of the number (in radians)
# 3.   Displays the calculated results.


from math import *

user_input_num = int(input("Enter a number : "))
print(f'Square root : {sqrt(user_input_num)}')
print(f'Logarithm : {log(user_input_num)}')
print(f'Sine : {sin(user_input_num)}')
