import pytest
from src.lcm import find_lcm

def test_lcm_basic_cases():
    """Test basic LCM calculations."""
    assert find_lcm(4, 6) == 12
    assert find_lcm(21, 6) == 42
    assert find_lcm(17, 5) == 85

def test_lcm_same_number():
    """Test LCM when both numbers are the same."""
    assert find_lcm(7, 7) == 7

def test_lcm_one_number_multiple():
    """Test LCM when one number is a multiple of the other."""
    assert find_lcm(8, 16) == 16
    assert find_lcm(16, 8) == 16

def test_lcm_coprime_numbers():
    """Test LCM of coprime numbers."""
    assert find_lcm(17, 23) == 391

def test_invalid_inputs():
    """Test error handling for invalid inputs."""
    # Test non-integer inputs
    with pytest.raises(TypeError):
        find_lcm(4.5, 6)
    with pytest.raises(TypeError):
        find_lcm("4", 6)
    
    # Test non-positive inputs
    with pytest.raises(ValueError):
        find_lcm(0, 5)
    with pytest.raises(ValueError):
        find_lcm(4, -6)
    with pytest.raises(ValueError):
        find_lcm(-4, -6)