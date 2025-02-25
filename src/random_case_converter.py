import random

def convert_to_random_case(input_string: str) -> str:
    """
    Convert a string to random case, where each character 
    is randomly either uppercase or lowercase.

    Args:
        input_string (str): The input string to be converted.

    Returns:
        str: A new string with characters randomly cased.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If input is empty, return empty string
    if not input_string:
        return ""
    
    # Convert each character to random case
    return ''.join(
        char.upper() if random.choice([True, False]) else char.lower() 
        for char in input_string
    )