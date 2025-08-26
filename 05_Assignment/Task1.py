# Task 1: Create a Dictionary of Student Marks

# Problem Statement: Write a Python program that:
# 1.  Creates a dictionary where student names are keys and their marks are values.
# 2.  Asks the user to input a student's name.
# 3.  Retrieves and displays the corresponding marks.
# 4.  If the student’s name is not found, display an appropriate message.

# outPut:
# Enter the student's name: Alice
# Alice's marks: 85

# Enter the student's name: John
# Student not found.

dic_of_stds_and_marks = {
    "Alice": 85,
    "Johnny": 55
}

userinput_of_std_name = input("Enter the student's name: ")

# Make the lookup case-insensitive
found = False
for name, marks in dic_of_stds_and_marks.items():
    if name.lower() == userinput_of_std_name.strip().lower():
        print(f"{name}'s marks: {marks}")
        found = True
        break

if not found:
    print("Student not found.")