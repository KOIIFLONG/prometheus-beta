def find_second_largest(arr):
    """
    Find the second largest element in an array of integers.
    
    Args:
        arr (list): A list of integers
    
    Returns:
        int: The second largest element in the array
    
    Raises:
        ValueError: If the input array has fewer than 2 unique elements
    """
    # Check if input is valid
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    # Remove duplicates and sort in descending order
    unique_elements = sorted(set(arr), reverse=True)
    
    # Check if there are at least 2 unique elements
    if len(unique_elements) < 2:
        raise ValueError("Array must contain at least 2 unique elements")
    
    # Return the second element (which is the second largest)
    return unique_elements[1]