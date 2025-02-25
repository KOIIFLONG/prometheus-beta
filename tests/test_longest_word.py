import pytest
from src.longest_word import find_longest_word

def test_find_longest_word_basic():
    """Test finding the longest word in a simple sentence."""
    assert find_longest_word("The quick brown fox jumps") == "quick"

def test_find_longest_word_multiple_max_length():
    """Test when multiple words have the same maximum length."""
    assert find_longest_word("cat dog mouse house") == "house"

def test_find_longest_word_punctuation():
    """Test sentence with punctuation."""
    assert find_longest_word("Hello, world! How are you?") == "Hello"

def test_find_longest_word_single_word():
    """Test with a single word."""
    assert find_longest_word("python") == "python"

def test_find_longest_word_empty_string():
    """Test that empty string raises ValueError."""
    with pytest.raises(ValueError, match="Input sentence cannot be empty"):
        find_longest_word("")

def test_find_longest_word_whitespace_only():
    """Test that whitespace-only string raises ValueError."""
    with pytest.raises(ValueError, match="Input sentence cannot be empty"):
        find_longest_word("   \t\n")

def test_find_longest_word_invalid_input():
    """Test that non-string input raises TypeError."""
    with pytest.raises(TypeError, match="Input must be a string"):
        find_longest_word(123)

def test_find_longest_word_mixed_case():
    """Test finding longest word with mixed case."""
    assert find_longest_word("Python is AWESOME") == "AWESOME"