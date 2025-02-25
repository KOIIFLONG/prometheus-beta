def reverse_matrix_elements(matrix):
    """
    Reverse the digits of each element in the given N x N matrix.
    
    Args:
        matrix (List[List[int]]): A square matrix of integers
    
    Returns:
        List[List[int]]: A new matrix with each element's digits reversed
    
    Raises:
        ValueError: If the matrix is not square
    """
    # Validate input matrix
    if not matrix or not matrix[0]:
        return []
    
    # Check if matrix is square
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("Input must be a square matrix")
    
    # Create a new matrix with reversed elements
    reversed_matrix = []
    for row in matrix:
        reversed_row = []
        for num in row:
            # Reverse the number's digits as a string
            reversed_num = int(str(num)[::-1])
            reversed_row.append(reversed_num)
        reversed_matrix.append(reversed_row)
    
    return reversed_matrix