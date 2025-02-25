def remove_char_length(string: str, char: str) -> int:
    """
    Remove all instances of a specified character from a string and return its new length.

    Args:
        string (str): The input string to modify
        char (str): The character to remove from the string

    Returns:
        int: The length of the string after removing all instances of the specified character

    Raises:
        TypeError: If input string or character is not a string
        ValueError: If character is not a single character
    """
    # Validate input types
    if not isinstance(string, str):
        raise TypeError("Input string must be a string")
    
    if not isinstance(char, str):
        raise TypeError("Character to remove must be a string")
    
    # Validate character length
    if len(char) != 1:
        raise ValueError("Character to remove must be a single character")
    
    # Remove the specified character and return the new length
    modified_string = string.replace(char, '')
    return len(modified_string)