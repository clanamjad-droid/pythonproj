import random

def fibonacci(n):
    """Return the nth fibonacci number."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# Generate random number between 1 and 10
random_num = random.randint(1, 10)

# Get fibonacci number and print result
fib_result = fibonacci(random_num)
print("Hello World")
print(f"Fibonacci({random_num}) = {fib_result}")
