# Task 1: Check if a Number is Even or Odd
# Problem Statement:  Write a Python program that:
# 1. 	Takes an integer input from the user.
# 2. 	Checks whether the number is even or odd using an if-else statement.
# 3. 	Displays the result accordingly.

def checkNumber():
    print("Check if a Number is Even or Odd")
    action = input(f'Enter "Y" for "Yes", "Q" for "Quit" from program :')
    while True:
        if action == "q" or action == "Q":
            break
        elif action == "y" or action == "Y":
            num = input(f"Enter a number :")
            try:
                num = int(num)
                if (num%2 == 0):
                    print(f"{num} is an even number.\n")
                else:
                    print(f"{num} is an Odd number.\n")                
            except Exception as e:
                print("Please enter a valid integer no.\n")    
                action = input(f'Enter "Y" for "Yes", "Q" for "Quit" from program :')        
        else:
            print("Choose valid option for action.\n")      
            action = input(f'Enter "Y" for "Yes", "Q" for "Quit" from program :')      
             
        

checkNumber()