# samples/python/utils.py
# Utility functions for the Python sample app.


def greet(name):
    return f'Hello, {name}! This is the Python sample app.'


def fibonacci(n):
    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]
