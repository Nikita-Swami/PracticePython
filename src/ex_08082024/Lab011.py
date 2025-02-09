#Find max between 3 numbers
num1 = int(input("Enter the number1\n"))
num2 = int(input("Enter the number2\n"))
num3 = int(input("Enter the number3\n"))

if num1>num2 and num1>num3:
    print(f"max is {num1}")
elif num2>num3 and num2>num1:
     print(f"max is {num2}")
else:
    print(f"max is {num3}")