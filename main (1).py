def factorial(n):
    # Base case: If n is 0 or 1, the factorial is 1.
    if n == 0 or n == 1:
        return 1
    # Recursive case: Multiply n by the factorial of (n-1).
    else:
        return n * factorial(n - 1)

# Test the function with an example:
n = 5
result = factorial(n)
print(f"The factorial of {n} is {result}")
