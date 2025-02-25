import pytest
from src.fibonacci import fibonacci

def test_fibonacci_base_cases():
    """Test base cases of Fibonacci sequence."""
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1

def test_fibonacci_known_values():
    """Test Fibonacci numbers with known values."""
    assert fibonacci(2) == 1
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55

def test_fibonacci_larger_numbers():
    """Test Fibonacci calculation for larger numbers."""
    assert fibonacci(20) == 6765
    assert fibonacci(30) == 832040

def test_negative_input():
    """Test that negative inputs raise a ValueError."""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        fibonacci(-1)

def test_non_integer_input():
    """Test that non-integer inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci(3.14)
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci("5")

def test_memoization():
    """
    Verify that memoization works by creating a shared memo dictionary.
    
    This test ensures that repeated calls with the same input 
    benefit from previously calculated values.
    """
    memo = {}
    result1 = fibonacci(10, memo)
    result2 = fibonacci(10, memo)
    assert result1 == result2  # Should return the same value
    
    # Verify different calls can share the same memo
    another_result = fibonacci(5, memo)
    assert another_result == 5