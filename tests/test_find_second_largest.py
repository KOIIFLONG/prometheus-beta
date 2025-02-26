import pytest
from src.find_second_largest import find_second_largest

def test_basic_unsorted_array():
    """Test finding second largest in an unsorted array"""
    assert find_second_largest([5, 2, 8, 1, 9]) == 8

def test_array_with_duplicates():
    """Test array with duplicate elements"""
    assert find_second_largest([5, 5, 8, 8, 9, 1]) == 8

def test_sorted_array():
    """Test finding second largest in a sorted array"""
    assert find_second_largest([1, 2, 3, 4, 5]) == 4

def test_reverse_sorted_array():
    """Test finding second largest in a reverse sorted array"""
    assert find_second_largest([5, 4, 3, 2, 1]) == 4

def test_empty_array():
    """Test that an empty array raises a ValueError"""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_second_largest([])

def test_single_element_array():
    """Test that an array with a single element raises a ValueError"""
    with pytest.raises(ValueError, match="Array must contain at least 2 unique elements"):
        find_second_largest([1])

def test_all_same_elements():
    """Test array with all same elements raises a ValueError"""
    with pytest.raises(ValueError, match="Array must contain at least 2 unique elements"):
        find_second_largest([2, 2, 2, 2])

def test_negative_numbers():
    """Test finding second largest with negative numbers"""
    assert find_second_largest([-1, -5, -2, -8, -3]) == -2