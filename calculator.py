def add(a, b):
    return a + b

def average(numbers):
    if not numbers:
        raise ValueError('The list cannot be empty')
    return sum(numbers) / len(numbers)