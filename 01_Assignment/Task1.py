# Task 1: Perform Basic Mathematical Operations
# Problem Statement: Write a Python program that does the following:
    # 1.  Takes two numbers as input from the user.
    # 2.  Performs the basic mathematical operations on these two numbers:
        # Addition
        # Subtraction
        # Multiplication
        # Division
    # 3.  Displays the results of each operation on the screen.

print("Perform Basic Mathematical Operations,Please Input Two Numbers");

first_num = int(input("Please Enter First Number :"));
second_num = int(input("Please Enter Second Number :"));

print(f"\nYour First Number Is : {first_num}");
print(f"Your Second Number Is : {second_num}");

print("\nPerforms the basic mathematical operations on these two numbers\n")

print(f"Addition : {first_num + second_num}")
print(f"Subtraction : {first_num - second_num}")
print(f"Multiplication: {first_num * second_num}")
print(f"Division: {first_num / second_num}")


