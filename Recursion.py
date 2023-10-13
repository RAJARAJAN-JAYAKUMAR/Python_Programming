def factorial(n):
    # Base case: if n is 0 or 1, the factorial is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: calculate factorial by multiplying n with factorial of (n-1)
    else:
        return n * factorial(n - 1)

# Example usage:
result = factorial(5)
print("Factorial of 5:", result)
