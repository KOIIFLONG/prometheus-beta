import pytest
import random
from src.random_case_converter import convert_to_random_case

def test_convert_to_random_case_basic():
    """Test that the function works with a basic string."""
    input_str = "hello"
    result = convert_to_random_case(input_str)
    
    # Verify the result is the same length
    assert len(result) == len(input_str)
    
    # Verify the result contains the same characters (just differently cased)
    assert set(result.lower()) == set(input_str.lower())

def test_convert_to_random_case_empty_string():
    """Test that an empty string returns an empty string."""
    assert convert_to_random_case("") == ""

def test_convert_to_random_case_error_handling():
    """Test that non-string inputs raise a TypeError."""
    with pytest.raises(TypeError):
        convert_to_random_case(123)
    with pytest.raises(TypeError):
        convert_to_random_case(None)

def test_convert_to_random_case_randomness():
    """
    Test that the function provides some level of randomness.
    This test checks if multiple calls can produce different results.
    Due to randomness, we use a probabilistic approach.
    """
    input_str = "abcdefg"
    
    # Set a seed for reproducibility in randomness test
    random.seed(42)
    
    # Generate multiple results
    results = [convert_to_random_case(input_str) for _ in range(10)]
    
    # Check that not all results are the same
    assert len(set(results)) > 1