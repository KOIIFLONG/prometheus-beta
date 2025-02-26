import pytest
from src.remove_duplicates import remove_duplicates_and_sort

def test_basic_removal_and_sort():
    """Test basic functionality of removing duplicates and sorting"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    expected = [1, 2, 3, 4, 5, 6, 9]
    assert remove_duplicates_and_sort(input_list) == expected

def test_already_sorted_list():
    """Test list that is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    expected = [1, 2, 3, 4, 5]
    assert remove_duplicates_and_sort(input_list) == expected

def test_reverse_sorted_list():
    """Test list in reverse order"""
    input_list = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert remove_duplicates_and_sort(input_list) == expected

def test_list_with_all_duplicates():
    """Test list with all duplicate elements"""
    input_list = [2, 2, 2, 2, 2]
    expected = [2]
    assert remove_duplicates_and_sort(input_list) == expected

def test_empty_list():
    """Test empty list"""
    input_list = []
    expected = []
    assert remove_duplicates_and_sort(input_list) == expected

def test_single_element_list():
    """Test list with a single element"""
    input_list = [42]
    expected = [42]
    assert remove_duplicates_and_sort(input_list) == expected

def test_invalid_input_type():
    """Test with invalid input type"""
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates_and_sort("not a list")

def test_non_integer_elements():
    """Test list with non-integer elements"""
    with pytest.raises(TypeError, match="All elements must be integers"):
        remove_duplicates_and_sort([1, 2, "3", 4])

def test_negative_numbers():
    """Test list with negative numbers"""
    input_list = [-3, 1, -3, 0, 5, 1, -1]
    expected = [-3, -1, 0, 1, 5]
    assert remove_duplicates_and_sort(input_list) == expected