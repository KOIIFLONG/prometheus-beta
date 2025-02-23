def arithmetic_sort(arr):
    """
    Sort a list of integers using only basic arithmetic operations.
    Uses selection sort algorithm with no built-in sorting functions.
    
    Args:
        arr (list): List of integers to be sorted
    
    Returns:
        list: Sorted list of integers
    """
    # If list is empty or has only one element, return as is
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a copy of the input list to avoid modifying the original
    sorted_arr = arr.copy()
    
    # Outer loop for selection sort
    for i in range(len(sorted_arr)):
        # Assume the current index has the minimum value
        min_idx = i
        
        # Inner loop to find the minimum element in unsorted portion
        for j in range(i + 1, len(sorted_arr)):
            # Compare elements using only arithmetic operations
            # If the element at j is less than the current minimum, update min_idx
            if sorted_arr[j] - sorted_arr[min_idx] < 0:
                min_idx = j
        
        # Swap elements using only arithmetic operations
        if min_idx != i:
            sorted_arr[i], sorted_arr[min_idx] = sorted_arr[min_idx], sorted_arr[i]
    
    return sorted_arr