
#Write a program in Python to produce a Star triangle?

def star_triangle(n):
    for i in range(1, n + 1):
        # Print spaces for alignment
        print(" " * (n - i), end="")
        # Print stars
        print("*" * (2 * i - 1))

# Example usage:
n = int(input("Enter the number of rows: "))
star_triangle(n)
