def is_valid_parentheses(s: str) -> bool:
    """
    Determine if parentheses in a string are correctly nested.
    
    Args:
        s (str): Input string to check for correct parentheses nesting
    
    Returns:
        bool: True if parentheses are correctly nested, False otherwise
    
    Examples:
        >>> is_valid_parentheses("()")  # Valid nesting
        True
        >>> is_valid_parentheses("((()))")  # Valid nesting
        True
        >>> is_valid_parentheses("(())")  # Valid nesting
        True
        >>> is_valid_parentheses(")(")  # Invalid nesting
        False
        >>> is_valid_parentheses("(()")  # Unbalanced
        False
        >>> is_valid_parentheses("")  # Empty string is valid
        True
    """
    # Stack to keep track of opening parentheses
    stack = []
    
    # Iterate through each character in the string
    for char in s:
        # If opening parenthesis, push to stack
        if char == '(':
            stack.append(char)
        # If closing parenthesis
        elif char == ')':
            # If no opening parenthesis to match, return False
            if not stack:
                return False
            # Pop the last opening parenthesis
            stack.pop()
    
    # Return True if stack is empty (all parentheses matched)
    return len(stack) == 0