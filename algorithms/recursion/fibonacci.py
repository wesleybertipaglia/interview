def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = fibonacci_recursive(n - 1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

# example usage:
n_terms = 10
fib_sequence = fibonacci_recursive(n_terms)
print("Fibonacci sequence up to", n_terms, "terms:", fib_sequence)
