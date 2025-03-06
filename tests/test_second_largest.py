import pytest
from src.second_largest import find_second_largest

def test_normal_array():
    """Test finding second largest in a normal array."""
    assert find_second_largest([1, 2, 3, 4, 5]) == 4
    assert find_second_largest([5, 2, 8, 1, 9]) == 8

def test_array_with_duplicates():
    """Test finding second largest with duplicate values."""
    assert find_second_largest([1, 1, 2, 2, 3, 3]) == 2
    assert find_second_largest([5, 5, 5, 3, 3, 4]) == 4

def test_negative_numbers():
    """Test finding second largest with negative numbers."""
    assert find_second_largest([-1, -2, -3, -4, -5]) == -2

def test_mixed_numbers():
    """Test finding second largest with mixed positive and negative numbers."""
    assert find_second_largest([-10, 5, 0, 3, 3]) == 3

def test_error_cases():
    """Test error cases."""
    # Empty array
    with pytest.raises(ValueError, match="Array must contain at least 2 unique elements"):
        find_second_largest([])
    
    # Single element array
    with pytest.raises(ValueError, match="Array must contain at least 2 unique elements"):
        find_second_largest([1])
    
    # Array with all same elements
    with pytest.raises(ValueError, match="Array must contain at least 2 unique elements"):
        find_second_largest([2, 2, 2, 2])