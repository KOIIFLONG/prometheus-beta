import pytest
from src.min_steps_to_target_sum import min_steps_to_target_sum

def test_basic_cases():
    # Basic positive case
    assert min_steps_to_target_sum([1, 2, 3], 6) == 2  # e.g., 1+3 or 2+3
    
    # Target is zero
    assert min_steps_to_target_sum([1, -1, 2, -2], 0) == 1
    
    # Negative target
    assert min_steps_to_target_sum([1, 2, 3], -6) == 2
    
    # Target cannot be reached
    assert min_steps_to_target_sum([1, 2], 5) == -1

def test_edge_cases():
    # Empty list
    assert min_steps_to_target_sum([], 5) == -1
    
    # Single number cases
    assert min_steps_to_target_sum([5], 5) == 1
    assert min_steps_to_target_sum([5], 10) == -1
    
    # Large numbers
    assert min_steps_to_target_sum([100, 200, 300], 500) == 2

def test_complex_cases():
    # Multiple ways to reach the target
    result = min_steps_to_target_sum([1, 2, 3, 4], 7)
    assert result == 2  # e.g., 3+4 or 1+2+4
    
    # Mix of positive and negative numbers
    assert min_steps_to_target_sum([-1, 1, 2, 3], 4) == 2
    
    # Repeated number usage not allowed
    assert min_steps_to_target_sum([2, 2], 4) == 2  # both 2s used with +/-

def test_large_lists():
    # Test with larger list of numbers
    large_list = list(range(1, 11))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = min_steps_to_target_sum(large_list, 15)
    assert result > 0  # should be possible to reach 15