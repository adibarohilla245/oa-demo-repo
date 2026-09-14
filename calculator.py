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
