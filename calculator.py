def add(a, b):
    return a + b

def reverse_string(s):
    return s[::-1]

def power(base, exponent):
    return base ** exponent

def divide(a, b):
    if b == 0:
        raise ValueError('Cannot divide by zero')
    return a / b

def multiply(a, b):
    return a * b