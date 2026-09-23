def celsius_to_fahrenheit(c: float) -> float:
    """
    Converts Celsius to Fahrenheit.
    
    Parameters:
    c (float): Temperature in Celsius.
    
    Returns:
    float: Temperature in Fahrenheit.
    """
    return (c * 9/5) + 32


def fahrenheit_to_celsius(f: float) -> float:
    """
    Converts Fahrenheit to Celsius.
    
    Parameters:
    f (float): Temperature in Fahrenheit.
    
    Returns:
    float: Temperature in Celsius.
    """
    return (f - 32) * 5/9