import cx_Oracle
import os


# Iterative approach
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Recursive approach
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Get input from the user
num = int(input("Enter a number: "))

# Calculate factorial using both approaches
iterative_result = factorial_iterative(num)
recursive_result = factorial_recursive(num)

# Print the results
print(f"Factorial of {num} (Iterative): {iterative_result}")
print(f"Factorial of {num} (Recursive): {recursive_result}")


















