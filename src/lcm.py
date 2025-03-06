def find_lcm(a: int, b: int) -> int:
    """
    Calculate the Least Common Multiple (LCM) of two integers.

    Args:
        a (int): First integer
        b (int): Second integer

    Returns:
        int: Least Common Multiple of a and b

    Raises:
        ValueError: If either input is not a positive integer
    """
    # Validate inputs
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Inputs must be integers")
    
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers")
    
    # Use the formula: LCM(a,b) = |a * b| / GCD(a,b)
    def gcd(x: int, y: int) -> int:
        """Calculate Greatest Common Divisor using Euclidean algorithm."""
        while y:
            x, y = y, x % y
        return x
    
    return abs(a * b) // gcd(a, b)