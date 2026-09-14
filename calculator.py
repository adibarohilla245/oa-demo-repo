def add(a: float, b: float) -> float:
    """
    Adds two numbers and returns the result.
    
    Parameters:
    a (float): The first number.
    b (float): The second number.
    
    Returns:
    float: The sum of a and b.
    """
    return a + b


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError('Input should be a non-negative integer')
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


def subtract(a: float, b: float) -> float:
    """
    Subtracts the second number from the first and returns the result.
    
    Parameters:
    a (float): The number from which to subtract.
    b (float): The number to subtract.
    
    Returns:
    float: The result of a - b.
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """
    Multiplies two numbers and returns the result.
    
    Parameters:
    a (float): The first number.
    b (float): The second number.
    
    Returns:
    float: The product of a and b.
    """
    return a * b


def divide(a: float, b: float) -> float:
    """
    Divides the first number by the second and returns the result.
    Raises an error if the second number is zero.
    
    Parameters:
    a (float): The numerator.
    b (float): The denominator.
    
    Returns:
    float: The result of a / b.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def modulo(a: float, b: float) -> float:
    """
    Returns the remainder of the division of the first number by the second.
    
    Parameters:
    a (float): The numerator.
    b (float): The denominator.
    
    Returns:
    float: The result of a % b.
    """
    return a % b


def power(base: float, exponent: float) -> float:
    """
    Raises the base to the power of the exponent and returns the result.
    
    Parameters:
    base (float): The base number.
    exponent (float): The exponent number.
    
    Returns:
    float: The result of base raised to the given exponent.
    """
    return base ** exponent