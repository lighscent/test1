# example.py
# A simple Python script that prints a greeting and computes factorial.

def greet(name):
    return f"Hello, {name}! Welcome to Python."


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


if __name__ == '__main__':
    print(greet('Developer'))
    print('5! =', factorial(5))
