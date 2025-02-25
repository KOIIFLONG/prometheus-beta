def bubble_merge_sort(arr):
    """
    Custom sorting algorithm that combines Bubble Sort and Merge Sort.
    
    This algorithm works in two stages:
    1. Partially sort the array using Bubble Sort to reduce inversions
    2. Perform a Merge Sort to complete the sorting
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: A new sorted list
    
    Raises:
        TypeError: If input is not a list
    """
    # Type checking
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Stage 1: Bubble Sort to reduce inversions
    def bubble_sort_pass(lst):
        """Perform a single pass of bubble sort."""
        n = len(lst)
        swapped = False
        for i in range(n - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = True
        return swapped
    
    # Create a copy to avoid modifying the original list
    working_arr = arr.copy()
    
    # Perform multiple bubble sort passes to reduce inversions
    for _ in range(len(working_arr) // 2):
        bubble_sort_pass(working_arr)
    
    # Stage 2: Merge Sort
    def merge(left, right):
        """Merge two sorted lists."""
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        # Append remaining elements
        result.extend(left[i:])
        result.extend(right[j:])
        
        return result
    
    def merge_sort(lst):
        """Recursive merge sort implementation."""
        # Base case
        if len(lst) <= 1:
            return lst
        
        # Divide
        mid = len(lst) // 2
        left = merge_sort(lst[:mid])
        right = merge_sort(lst[mid:])
        
        # Conquer (merge)
        return merge(left, right)
    
    # Final merge sort to complete the sorting
    return merge_sort(working_arr)