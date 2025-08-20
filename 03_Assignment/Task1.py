# Method 1st get factorial using Recursion
def factorial(num):
    if num < 2:
        return 1
    else:
        return num * (factorial(num-1))
    
userInputNum = int(input("Enter a number : "))

result = factorial(num=userInputNum)

print(f"Factorial of {userInputNum} is : {result}")

# ==============================================================
# Method 1st get factorial using for loop

factorial_Result = 1
for fact in range(1, userInputNum + 1):
    factorial_Result *= fact

print(f"Factorial of {userInputNum} is : {factorial_Result}")
