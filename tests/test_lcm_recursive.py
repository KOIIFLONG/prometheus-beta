import pytest
from src.lcm_recursive import lcm_recursive, gcd_recursive

def test_gcd_recursive_basic():
    """Test basic GCD calculations"""
    assert gcd_recursive(48, 18) == 6
    assert gcd_recursive(54, 24) == 6
    assert gcd_recursive(0, 5) == 5
    assert gcd_recursive(5, 0) == 5

def test_gcd_recursive_edge_cases():
    """Test edge cases for GCD"""
    assert gcd_recursive(0, 0) == 0
    assert gcd_recursive(1, 1) == 1

def test_gcd_recursive_negative_input():
    """Test that negative inputs raise ValueError"""
    with pytest.raises(ValueError):
        gcd_recursive(-1, 5)
    with pytest.raises(ValueError):
        gcd_recursive(5, -1)

def test_lcm_recursive_basic():
    """Test basic LCM calculations"""
    assert lcm_recursive(4, 6) == 12
    assert lcm_recursive(21, 6) == 42
    assert lcm_recursive(3, 5) == 15
    assert lcm_recursive(2, 3) == 6

def test_lcm_recursive_zero_input():
    """Test LCM with zero inputs"""
    assert lcm_recursive(0, 5) == 0
    assert lcm_recursive(5, 0) == 0
    assert lcm_recursive(0, 0) == 0

def test_lcm_recursive_one_input():
    """Test LCM with one input being 1"""
    assert lcm_recursive(1, 5) == 5
    assert lcm_recursive(5, 1) == 5
    assert lcm_recursive(1, 1) == 1

def test_lcm_recursive_negative_input():
    """Test that negative inputs raise ValueError"""
    with pytest.raises(ValueError):
        lcm_recursive(-1, 5)
    with pytest.raises(ValueError):
        lcm_recursive(5, -1)
    with pytest.raises(ValueError):
        lcm_recursive(-1, -1)