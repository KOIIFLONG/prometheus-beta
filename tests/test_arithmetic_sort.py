import pytest
from src.arithmetic_sort import arithmetic_sort

def test_arithmetic_sort_empty_list():
    """Test sorting an empty list"""
    assert arithmetic_sort([]) == []

def test_arithmetic_sort_single_element():
    """Test sorting a list with a single element"""
    assert arithmetic_sort([5]) == [5]

def test_arithmetic_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    assert arithmetic_sort(input_list) == input_list

def test_arithmetic_sort_reverse_sorted():
    """Test sorting a list in reverse order"""
    input_list = [5, 4, 3, 2, 1]
    assert arithmetic_sort(input_list) == [1, 2, 3, 4, 5]

def test_arithmetic_sort_random_order():
    """Test sorting a list in random order"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert arithmetic_sort(input_list) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_arithmetic_sort_with_negatives():
    """Test sorting a list with negative numbers"""
    input_list = [-5, 3, 0, -2, 7, 1]
    assert arithmetic_sort(input_list) == [-5, -2, 0, 1, 3, 7]

def test_arithmetic_sort_preserves_original_list():
    """Test that the original list is not modified"""
    input_list = [3, 1, 4, 1, 5]
    _ = arithmetic_sort(input_list)
    assert input_list == [3, 1, 4, 1, 5]