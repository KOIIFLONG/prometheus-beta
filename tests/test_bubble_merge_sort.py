import pytest
import random
from src.bubble_merge_sort import bubble_merge_sort

def test_basic_sorting():
    """Test basic sorting functionality"""
    assert bubble_merge_sort([4, 2, 7, 1, 5, 3]) == [1, 2, 3, 4, 5, 7]

def test_already_sorted():
    """Test sorting an already sorted list"""
    sorted_list = [1, 2, 3, 4, 5]
    assert bubble_merge_sort(sorted_list) == sorted_list

def test_reverse_sorted():
    """Test sorting a reverse-sorted list"""
    assert bubble_merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_empty_list():
    """Test sorting an empty list"""
    assert bubble_merge_sort([]) == []

def test_single_element_list():
    """Test sorting a list with a single element"""
    assert bubble_merge_sort([42]) == [42]

def test_duplicate_elements():
    """Test sorting a list with duplicate elements"""
    assert bubble_merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_large_random_list():
    """Test sorting a large random list"""
    # Generate a large random list
    large_list = [random.randint(-1000, 1000) for _ in range(1000)]
    
    # Compare with Python's built-in sort
    expected = sorted(large_list)
    assert bubble_merge_sort(large_list) == expected

def test_negative_numbers():
    """Test sorting a list with negative numbers"""
    assert bubble_merge_sort([-4, -2, -7, -1, -5, -3]) == [-7, -5, -4, -3, -2, -1]

def test_mixed_numbers():
    """Test sorting a list with mixed positive and negative numbers"""
    assert bubble_merge_sort([-4, 2, 0, -1, 5, -3]) == [-4, -3, -1, 0, 2, 5]

def test_error_handling():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        bubble_merge_sort("not a list")
    
    with pytest.raises(TypeError):
        bubble_merge_sort(123)
    
    with pytest.raises(TypeError):
        bubble_merge_sort(None)