def add(a, b):
    return a + b

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def power(base, exponent):
    return base ** exponent

def divide(a, b):
    if b == 0:
        raise ValueError('Cannot divide by zero')
    return a / b

def multiply(a, b):
    return a * b