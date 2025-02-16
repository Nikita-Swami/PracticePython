#FizzBuzz from 1 to 100
#Multiply by 3 print Fizz
#Multiply by 5 print Buzz
#Multiply by 3 and 5 print FizzBuzz

for i in range(1,101,1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)