import pytest
from src.counting_sort import counting_sort

def test_basic_sorting():
    """Test basic sorting functionality"""
    input_list = [4, 2, 2, 8, 3, 3, 1]
    assert counting_sort(input_list) == [1, 2, 2, 3, 3, 4, 8]

def test_empty_list():
    """Test sorting an empty list"""
    assert counting_sort([]) == []

def test_single_element_list():
    """Test sorting a list with a single element"""
    assert counting_sort([5]) == [5]

def test_already_sorted_list():
    """Test sorting an already sorted list"""
    input_list = [1, 2, 3, 4, 5]
    assert counting_sort(input_list) == [1, 2, 3, 4, 5]

def test_list_with_zeros():
    """Test sorting a list that includes zero"""
    input_list = [0, 3, 2, 1, 0]
    assert counting_sort(input_list) == [0, 0, 1, 2, 3]

def test_list_with_repeated_elements():
    """Test sorting a list with multiple repeated elements"""
    input_list = [3, 3, 3, 1, 1, 2, 2]
    assert counting_sort(input_list) == [1, 1, 2, 2, 3, 3, 3]

def test_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        counting_sort("not a list")

def test_negative_elements():
    """Test that ValueError is raised for negative numbers"""
    with pytest.raises(ValueError, match="All elements must be non-negative integers"):
        counting_sort([-1, 2, 3])

def test_non_integer_elements():
    """Test that ValueError is raised for non-integer elements"""
    with pytest.raises(ValueError, match="All elements must be non-negative integers"):
        counting_sort([1.5, 2, 3])

def test_large_range_sorting():
    """Test sorting with a larger range of numbers"""
    input_list = [100, 3, 200, 1, 50, 25]
    assert counting_sort(input_list) == [1, 3, 25, 50, 100, 200]