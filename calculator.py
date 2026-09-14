def add(a, b):
    return a + b

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)