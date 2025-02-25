def transform_array(input_array):
    """
    Transform an array of non-negative integers based on specific rules.
    
    Args:
        input_array (list): A list of non-negative integers.
    
    Returns:
        list: A new list where:
            - 0 remains 0
            - Non-zero elements are transformed to their square plus 1
    
    Raises:
        TypeError: If input is not a list.
        ValueError: If any element is a negative number.
    
    Examples:
        >>> transform_array([0, 1, 2, 3])
        [0, 2, 5, 10]
        >>> transform_array([])
        []
    """
    # Validate input type
    if not isinstance(input_array, list):
        raise TypeError("Input must be a list")
    
    # Validate input elements
    if any(not isinstance(x, int) or x < 0 for x in input_array):
        raise ValueError("All elements must be non-negative integers")
    
    # Transform the array
    return [0 if x == 0 else x**2 + 1 for x in input_array]