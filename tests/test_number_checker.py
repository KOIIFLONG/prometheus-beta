import pytest
from src.number_checker import is_even_or_odd

def test_positive_even_numbers():
    """Test that positive even numbers return 'even'."""
    assert is_even_or_odd(0) == 'even'
    assert is_even_or_odd(2) == 'even'
    assert is_even_or_odd(4) == 'even'
    assert is_even_or_odd(100) == 'even'

def test_positive_odd_numbers():
    """Test that positive odd numbers return 'odd'."""
    assert is_even_or_odd(1) == 'odd'
    assert is_even_or_odd(3) == 'odd'
    assert is_even_or_odd(5) == 'odd'
    assert is_even_or_odd(99) == 'odd'

def test_negative_even_numbers():
    """Test that negative even numbers return 'even'."""
    assert is_even_or_odd(-2) == 'even'
    assert is_even_or_odd(-4) == 'even'
    assert is_even_or_odd(-100) == 'even'

def test_negative_odd_numbers():
    """Test that negative odd numbers return 'odd'."""
    assert is_even_or_odd(-1) == 'odd'
    assert is_even_or_odd(-3) == 'odd'
    assert is_even_or_odd(-99) == 'odd'

def test_invalid_input():
    """Test that non-integer inputs raise a TypeError."""
    with pytest.raises(TypeError):
        is_even_or_odd(3.14)
    
    with pytest.raises(TypeError):
        is_even_or_odd("2")
    
    with pytest.raises(TypeError):
        is_even_or_odd([2])
    
    with pytest.raises(TypeError):
        is_even_or_odd(None)