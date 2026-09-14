def add(a, b):
    return a + b

def average(numbers):
    if not numbers:
        raise ValueError('The list cannot be empty')
    return sum(numbers) / len(numbers)

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