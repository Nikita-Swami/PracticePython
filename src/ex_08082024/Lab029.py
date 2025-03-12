# Function to display Fibonacci sequence
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

# Input from the user
num_terms = int(input("Enter the number of terms you want in the Fibonacci sequence: "))

# Call the function to display the sequence
fibonacci(num_terms)




