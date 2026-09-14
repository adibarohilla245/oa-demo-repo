def add(a, b):
    return a + b

def cube(n):
    return n ** 3

def power(base, exponent):
    return base ** exponent

def divide(a, b):
    if b == 0:
        raise ValueError('Cannot divide by zero')
    return a / b

def multiply(a, b):
    return a * b