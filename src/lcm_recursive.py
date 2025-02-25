def gcd_recursive(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) using the Euclidean algorithm recursively.
    
    Args:
        a (int): First non-negative integer
        b (int): Second non-negative integer
    
    Returns:
        int: Greatest Common Divisor of a and b
    
    Raises:
        ValueError: If either input is negative
    """
    # Validate inputs
    if a < 0 or b < 0:
        raise ValueError("Inputs must be non-negative integers")
    
    # Base case: if b is 0, return a
    if b == 0:
        return a
    
    # Recursive case: GCD(a, b) = GCD(b, a % b)
    return gcd_recursive(b, a % b)

def lcm_recursive(a: int, b: int) -> int:
    """
    Calculate the Least Common Multiple (LCM) using recursion.
    
    LCM is calculated using the formula: LCM(a,b) = |a * b| / GCD(a,b)
    
    Args:
        a (int): First non-negative integer
        b (int): Second non-negative integer
    
    Returns:
        int: Least Common Multiple of a and b
    
    Raises:
        ValueError: If either input is negative
        ZeroDivisionError: If both inputs are 0
    """
    # Validate inputs
    if a < 0 or b < 0:
        raise ValueError("Inputs must be non-negative integers")
    
    # Special case: if either number is 0, LCM is 0
    if a == 0 or b == 0:
        return 0
    
    # Calculate LCM using GCD
    return abs(a * b) // gcd_recursive(a, b)