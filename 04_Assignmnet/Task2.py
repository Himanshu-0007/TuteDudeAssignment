# Task 2: Write and Append Data to a File
 
# Problem Statement: Write a Python program that:
# 1.   Takes user input and writes it to a file named output.txt.
# 2.   Appends additional data to the same file.
# 3.   Reads and displays the final content of the file.

# Output
# Enter text to write to the file: Hello, Python!
# Data successfully written to output.txt.

# Enter additional text to append: Learning file handling in Python.
# Data successfully appended.

# Final content of output.txt:
# Hello, Python!
# Learning file handling in Python.

try:
    user_input_text = input("Enter text to write to the file: ")
    with open('output.txt', 'w') as output_file:
        output_file.write(user_input_text)
        print('Data successfully written to output.txt.\n')

    user_append_text = input("Enter additional text to append: ")
    with open('output.txt', 'a') as output_file:
        output_file.write(f'\n{user_append_text}')
        print('Data successfully appended.\n')

    print("Final content of output.txt:")
    with open('output.txt', 'r') as output_file:
        for line in output_file:
            print(line.strip())

except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
    
