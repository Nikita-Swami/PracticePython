#triangle identifier

#equiilateral,isosceles,scalene

a = float(input("Enter side a:\n"))
b = float(input("Enter side b:\n"))
c = float(input("Enter side c:\n"))

if a == b == c:
    print("Equilateral")
elif a == b or b == c or c == a:
    print("Isosceles")
else:
    print("Scalene")