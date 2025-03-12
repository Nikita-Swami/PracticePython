# Displaying Fibonacci sequence
n = 10
# first two terms
n0 = 0
n1 = 1
#Count
x = 0
# check if the number of terms is valid
if n <= 0:
   print("Enter positive integer")
elif n == 1:
   print("Numbers in Fibonacci sequence upto",n,":")
   print(n0)
else:
   print("Numbers in Fibonacci sequence upto",n,":")
   while x < n:
       print(n0,end=', ')
       nth = n0 + n1
       n0 = n1
       n1 = nth
       x += 1
