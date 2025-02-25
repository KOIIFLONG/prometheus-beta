import pytest
from src.max_subarray_sum import max_subarray_sum

def test_standard_case():
    """Test with a standard input array"""
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 4
    assert max_subarray_sum(arr, k) == 39

def test_single_element_array():
    """Test with a single element array"""
    arr = [5]
    assert max_subarray_sum(arr, 1) == 5

def test_all_same_elements():
    """Test array with all same elements"""
    arr = [2, 2, 2, 2, 2]
    assert max_subarray_sum(arr, 3) == 6

def test_negative_numbers():
    """Test array with negative numbers"""
    arr = [-1, -2, 3, 4, -5, 6, 7]
    assert max_subarray_sum(arr, 3) == 14

def test_k_larger_than_array():
    """Test when k is larger than array length"""
    arr = [1, 2, 3]
    assert max_subarray_sum(arr, 4) is None

def test_k_zero():
    """Test when k is zero"""
    arr = [1, 2, 3]
    assert max_subarray_sum(arr, 0) is None

def test_k_negative():
    """Test when k is negative"""
    arr = [1, 2, 3]
    assert max_subarray_sum(arr, -1) is None

def test_empty_array():
    """Test with an empty array"""
    arr = []
    assert max_subarray_sum(arr, 0) is None

def test_invalid_input_type():
    """Test with invalid input types"""
    with pytest.raises(TypeError):
        max_subarray_sum("not a list", 3)
    
    with pytest.raises(TypeError):
        max_subarray_sum([1, 2, 3], "not an int")

def test_full_array_subarray():
    """Test when k is equal to array length"""
    arr = [1, 2, 3, 4, 5]
    assert max_subarray_sum(arr, 5) == 15