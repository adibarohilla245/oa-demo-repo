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

def is_prime(n: int) -> bool:
    """
    Determines if the provided number is a prime number.
    
    Parameters:
    n (int): The number to check.
    
    Returns:
    bool: True if n is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

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