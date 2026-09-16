def add(a: float, b: float) -> float:
    """
    Adds two numbers together and returns the result.

    Parameters:
    a (float): The first number.
    b (float): The second number.

    Returns:
    float: The sum of a and b.
    """
    return a + b

def cube(n: float) -> float:
    """
    Raises a number to the power of three and returns the result.
    
    Parameters:
    n (float): The number to be cubed.
    
    Returns:
    float: The result of n raised to the power of three.
    """
    return n ** 3

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

def is_even(n: int) -> bool:
    return n % 2 == 0

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