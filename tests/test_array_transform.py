import pytest
from src.array_transform import transform_array

def test_basic_transform():
    """Test basic transformation of non-zero elements."""
    assert transform_array([0, 1, 2, 3]) == [0, 2, 5, 10]

def test_empty_array():
    """Test transformation of an empty array."""
    assert transform_array([]) == []

def test_zero_array():
    """Test array with only zeros."""
    assert transform_array([0, 0, 0]) == [0, 0, 0]

def test_invalid_input_type():
    """Test that non-list input raises TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        transform_array("not a list")

def test_negative_number():
    """Test that negative numbers raise ValueError."""
    with pytest.raises(ValueError, match="All elements must be non-negative integers"):
        transform_array([-1, 2, 3])

def test_mixed_inputs():
    """Test array with mixed non-zero elements."""
    assert transform_array([1, 0, 4, 5]) == [2, 0, 17, 26]

def test_float_input():
    """Test that non-integer inputs raise ValueError."""
    with pytest.raises(ValueError, match="All elements must be non-negative integers"):
        transform_array([1.5, 2, 3])

def test_large_numbers():
    """Test large non-zero inputs."""
    assert transform_array([10, 20]) == [101, 401]