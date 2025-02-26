def remove_duplicates_and_sort(arr):
    """
    Remove duplicate elements from an array of integers and sort in ascending order 
    without using built-in sorting or set methods.
    
    Args:
        arr (list): Input list of integers
    
    Returns:
        list: A new list with duplicates removed and sorted in ascending order
    
    Raises:
        TypeError: If input is not a list or contains non-integer elements
    """
    # Type checking
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are integers
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements must be integers")
    
    # If input is empty, return empty list
    if not arr:
        return []
    
    # Remove duplicates using manual method
    unique_elements = []
    for num in arr:
        # Only add if not already in unique_elements
        if num not in unique_elements:
            unique_elements.append(num)
    
    # Bubble sort in ascending order
    for i in range(len(unique_elements)):
        for j in range(0, len(unique_elements) - i - 1):
            if unique_elements[j] > unique_elements[j + 1]:
                # Swap elements
                unique_elements[j], unique_elements[j + 1] = unique_elements[j + 1], unique_elements[j]
    
    return unique_elements