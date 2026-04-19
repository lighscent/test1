# samples/python/app.py
# A simple Python app that uses helper functions from utils.py.

from utils import greet, fibonacci


def main():
    print(greet('Developer'))
    print('Fibonacci sequence for n=10:')
    print(fibonacci(10))


if __name__ == '__main__':
    main()
