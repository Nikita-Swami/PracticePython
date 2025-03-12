
# program to check the number is prime or not
#Method1
num1 = int(input("Enter any one number: "))
# prime number is greater than 1

# check the following factors
for x in range (2,num1):
      if (num1 % x) == 0:
        print(num1,"is not a prime number")
        print(x,"times",num1//x,"is",num1)

      else:
        print(num1,"is a prime number")
# if input number is smaller than
# or equal to the value 1, then it is not prime number

