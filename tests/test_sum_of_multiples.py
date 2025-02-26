import pytest
from src.sum_of_multiples import sum_of_multiples

def test_basic_range():
    """Test a basic range of numbers."""
    assert sum_of_multiples(1, 10) == 33  # 2+3+4+6+8+9+10 = 33

def test_single_number_multiple():
    """Test when only one number is a multiple."""
    assert sum_of_multiples(7, 7) == 0  # 7 is not multiple of 2 or 3

def test_single_number_multiple_of_two():
    """Test when single number is multiple of 2."""
    assert sum_of_multiples(8, 8) == 8

def test_single_number_multiple_of_three():
    """Test when single number is multiple of 3."""
    assert sum_of_multiples(9, 9) == 9

def test_large_range():
    """Test a larger range of numbers."""
    assert sum_of_multiples(1, 1000) > 0

def test_same_min_max():
    """Test when min and max are the same number."""
    assert sum_of_multiples(6, 6) == 6

def test_negative_min():
    """Test range with negative numbers."""
    assert sum_of_multiples(-10, 10) > 0

def test_invalid_range():
    """Test that an error is raised when min > max."""
    with pytest.raises(ValueError):
        sum_of_multiples(10, 1)

def test_zero_range():
    """Test range starting and ending at zero."""
    assert sum_of_multiples(0, 0) == 0