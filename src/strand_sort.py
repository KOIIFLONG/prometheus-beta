def strand_sort(arr):
    """
    Implement the strand sort algorithm to sort a list.
    
    Strand sort works by repeatedly extracting sorted sublists and merging them.
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: A new sorted list
    
    Raises:
        TypeError: If input is not a list
        TypeError: If list contains elements that cannot be compared
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element list
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a mutable copy to work with
    working_list = arr.copy()
    result = []
    
    while working_list:
        # Create a new sublist starting with the first element
        sublist = [working_list.pop(0)]
        
        # Iterate through remaining elements
        i = 0
        while i < len(working_list):
            # If current element is greater than the last element in sublist, add it
            if working_list[i] > sublist[-1]:
                sublist.append(working_list.pop(i))
            else:
                i += 1
        
        # Merge the sublist with the result list
        result = merge(result, sublist)
    
    return result

def merge(list1, list2):
    """
    Merge two sorted lists.
    
    Args:
        list1 (list): First sorted list
        list2 (list): Second sorted list
    
    Returns:
        list: A merged sorted list
    """
    merged = []
    i, j = 0, 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    
    # Add remaining elements from list1, if any
    merged.extend(list1[i:])
    
    # Add remaining elements from list2, if any
    merged.extend(list2[j:])
    
    return merged