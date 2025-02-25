import pytest
from src.matrix_reverser import reverse_matrix_elements

def test_basic_matrix_reversal():
    """Test reversing elements in a basic matrix"""
    input_matrix = [
        [12, 34],
        [56, 78]
    ]
    expected_matrix = [
        [21, 43],
        [65, 87]
    ]
    assert reverse_matrix_elements(input_matrix) == expected_matrix

def test_single_digit_matrix():
    """Test matrix with single-digit elements"""
    input_matrix = [
        [1, 2],
        [3, 4]
    ]
    assert reverse_matrix_elements(input_matrix) == input_matrix

def test_zero_matrix():
    """Test matrix with zero elements"""
    input_matrix = [
        [0, 0],
        [0, 0]
    ]
    assert reverse_matrix_elements(input_matrix) == input_matrix

def test_empty_matrix():
    """Test empty matrix"""
    assert reverse_matrix_elements([]) == []

def test_non_square_matrix():
    """Test that non-square matrix raises ValueError"""
    with pytest.raises(ValueError, match="Input must be a square matrix"):
        reverse_matrix_elements([
            [1, 2, 3],
            [4, 5]
        ])

def test_large_matrix():
    """Test a larger matrix"""
    input_matrix = [
        [12, 34, 56],
        [78, 90, 12],
        [34, 56, 78]
    ]
    expected_matrix = [
        [21, 43, 65],
        [87, 9, 21],
        [43, 65, 87]
    ]
    assert reverse_matrix_elements(input_matrix) == expected_matrix