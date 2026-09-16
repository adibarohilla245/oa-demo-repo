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

def is_even(n: int) -> bool:
    return n % 2 == 0

def square(n: float) -> float:
    """
    Returns the square of the number.
    
    Parameters:
    n (float): The number to be squared.
    
    Returns:
    float: The square of n.
    """
    return n * n


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

def is_leap_year(year: int) -> bool:
    """
    Determines if the given year is a leap year.
    
    A year is a leap year if it is divisible by 4, but not divisible by 100,
    unless it is also divisible by 400.
    
    Parameters:
    year (int): The year to check.
    
    Returns:
    bool: True if the year is a leap year, False otherwise.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)