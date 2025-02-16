#take 3number from user and display sum by using functions
num1 = int(input("Enter the number1"))
num2 = int(input("Enter the number2"))
num3 = int(input("Enter the number3"))

def sum_of_num(n1,n2,n3):
    return n1+n2+n3

result = sum_of_num(n1=num1,n2=num2,n3=num3)
print(result)
