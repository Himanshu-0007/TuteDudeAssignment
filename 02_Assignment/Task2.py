# Task 2: Sum of Integers from 1 to 50 Using a Loop 
# Problem Statement: Write a Python program that:
# 1.   Uses a for loop to iterate over numbers from 1 to 50.
# 2.   Calculates the sum of all integers in this range.
# 3.   Displays the final sum.

def SumOfRangeNumbers():
    f_num = int(input("Enter first number :"))
    l_num = int(input("Enter last number :"))
    rng_num = f_num
    sum =0
    while True:
        if rng_num > l_num:
            print(f"The Sum of numbers from {f_num} to {l_num} is: {sum}")
            break
        elif rng_num <= l_num:
            sum+= rng_num
            rng_num += 1
            

SumOfRangeNumbers()