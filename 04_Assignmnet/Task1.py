# Task 1: Read a File and Handle Errors 
# Problem Statement:  Write a Python program that:
# 1.   Opens and reads a text file named sample.txt.
# 2.   Prints its content line by line.
# 3.   Handles errors gracefully if the file does not exist.

# Output:
# Reading file content:
# Line 1: This is a sample text file.
# Line 2: It contains multiple lines.

try:
    with open('sample.txt', 'r') as sample_file:
        reading_sample_file_lines = sample_file.readlines()
        for idx, line in enumerate(reading_sample_file_lines, start=1):
            print(f'Line {idx}: {line.strip()}')
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")