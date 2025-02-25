def max_subarray_sum(arr, k):
    """
    Find the maximum sum of a subarray with length k in the given array.
    
    Args:
        arr (list): Input list of integers
        k (int): Length of the subarray
    
    Returns:
        int: Maximum sum of a subarray of length k
             Returns None if k is larger than the array length or k <= 0
    
    Raises:
        TypeError: If input is not a list or k is not an integer
    """
    # Validate input types
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    if not isinstance(k, int):
        raise TypeError("k must be an integer")
    
    # Check for invalid k values
    if k <= 0 or k > len(arr):
        return None
    
    # Initial window sum
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide the window and update max sum
    for i in range(k, len(arr)):
        # Remove first element of previous window and add new element
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum