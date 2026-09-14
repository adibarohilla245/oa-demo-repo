def add(a, b):
    return a + b

def is_even(n):
    return n % 2 == 0

def modulo(a, b):
    return a % b

def power(base, exponent):
    return base ** exponent

def divide(a, b):
    if b == 0:
        raise ValueError('Cannot divide by zero')
    return a / b

def multiply(a, b):
    return a * b