import pytest
from src.remove_char_length import remove_char_length

def test_remove_char_basic():
    """Test basic character removal and length calculation"""
    assert remove_char_length("hello", "l") == 3

def test_remove_char_multiple_occurrences():
    """Test removal of multiple occurrences of a character"""
    assert remove_char_length("mississippi", "s") == 7

def test_remove_char_no_occurrences():
    """Test when the character is not in the string"""
    assert remove_char_length("hello", "x") == 5

def test_remove_char_empty_string():
    """Test with an empty string"""
    assert remove_char_length("", "a") == 0

def test_remove_char_whole_string_removed():
    """Test when all characters are removed"""
    assert remove_char_length("aaaa", "a") == 0

def test_invalid_input_non_string():
    """Test error handling for non-string input"""
    with pytest.raises(TypeError, match="Input string must be a string"):
        remove_char_length(123, "a")

def test_invalid_input_non_string_char():
    """Test error handling for non-string character"""
    with pytest.raises(TypeError, match="Character to remove must be a string"):
        remove_char_length("hello", 1)

def test_invalid_input_multi_char():
    """Test error handling for multi-character input"""
    with pytest.raises(ValueError, match="Character to remove must be a single character"):
        remove_char_length("hello", "ab")