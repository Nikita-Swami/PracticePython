#Write a program for factorial of number in python

def factorial(n):
    # If the number is 0 or 1, the factorial is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursively calculate factorial
        return n * factorial(n - 1)

# Take input from the user
num = int(input("Enter a number: "))

# Ensure the number is non-negative
if num < 0:
    print("Factorial is not defined for negative numbers")
else:
    print(f"The factorial of {num} is {factorial(num)}")
