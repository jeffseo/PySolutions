import random
"""
8.1
Write a method to generate the nth Fibonacci number.
"""

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

def fibonacci_iterative(n):
    if n == 0:
        return 0
    else:
        a = 1
        b = 1
        for i in range(3,n + 1):
            c = a + b
            a = b
            b = c
        return b

print fibonacci(10)
print fibonacci_iterative(10)
for i in range(random.randint(1,20)):
    assert fibonacci(i) == fibonacci_iterative(i)