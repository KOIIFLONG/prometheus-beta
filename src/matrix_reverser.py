def reverse_matrix_elements(matrix):
    """
    Reverse the digits of each element in the given N x N matrix.
    
    Args:
        matrix (List[List[int]]): A square matrix of integers in range [0, 9]
    
    Returns:
        List[List[int]]: A new matrix with each element's digits reversed
    
    Raises:
        ValueError: If the matrix is not square or contains invalid elements
    """
    # Validate input matrix
    if not matrix or not matrix[0]:
        return []
    
    # Check if matrix is square
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("Input must be a square matrix")
    
    # Validate matrix elements
    for row in matrix:
        if any(not (0 <= num <= 9) for num in row):
            raise ValueError("Matrix elements must be integers in range [0, 9]")
    
    # Create a new matrix with reversed elements
    reversed_matrix = []
    for row in matrix:
        reversed_row = []
        for num in row:
            # Reverse the digit
            reversed_num = int(str(num)[::-1]) if num > 9 else num
            reversed_row.append(reversed_num)
        reversed_matrix.append(reversed_row)
    
    return reversed_matrix