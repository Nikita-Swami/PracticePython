# program to check the number is prime or not
#Method2

def is_prime(n):
    # Check if the number is less than 2
    if n <= 1:
        return False

    # Check divisibility from 2 to the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example usage:
num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
