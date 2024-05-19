def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# example usage:
num = 5
result = factorial(num)
print("Factorial of", num, "is", result)
