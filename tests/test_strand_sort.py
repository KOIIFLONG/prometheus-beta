import pytest
from src.strand_sort import strand_sort

def test_strand_sort_basic():
    """Test basic sorting of integers"""
    arr = [5, 2, 9, 1, 7, 6]
    assert strand_sort(arr) == sorted(arr)

def test_strand_sort_already_sorted():
    """Test sorting of an already sorted list"""
    arr = [1, 2, 3, 4, 5]
    assert strand_sort(arr) == arr

def test_strand_sort_reverse_sorted():
    """Test sorting of a reverse-sorted list"""
    arr = [5, 4, 3, 2, 1]
    assert strand_sort(arr) == sorted(arr)

def test_strand_sort_duplicates():
    """Test sorting of a list with duplicate elements"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    assert strand_sort(arr) == sorted(arr)

def test_strand_sort_empty_list():
    """Test sorting of an empty list"""
    arr = []
    assert strand_sort(arr) == []

def test_strand_sort_single_element():
    """Test sorting of a single-element list"""
    arr = [42]
    assert strand_sort(arr) == [42]

def test_strand_sort_floats():
    """Test sorting of floating-point numbers"""
    arr = [3.14, 2.71, 1.41, 0.58]
    assert strand_sort(arr) == sorted(arr)

def test_strand_sort_strings():
    """Test sorting of strings"""
    arr = ['banana', 'apple', 'cherry', 'date']
    assert strand_sort(arr) == sorted(arr)

def test_strand_sort_invalid_input():
    """Test handling of invalid input type"""
    with pytest.raises(TypeError):
        strand_sort("not a list")
    with pytest.raises(TypeError):
        strand_sort(None)

def test_strand_sort_unsortable_elements():
    """Test handling of unsortable elements"""
    class UnsortableClass:
        pass
    
    arr = [UnsortableClass(), UnsortableClass()]
    with pytest.raises(TypeError):
        strand_sort(arr)