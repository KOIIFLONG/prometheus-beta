import pytest
from src.palindrome_checker import is_palindrome

def test_classic_palindromes():
    """Test classic palindrome strings"""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False
    assert is_palindrome("Was it a car or a cat I saw?") == True

def test_empty_and_single_char():
    """Test edge cases with empty string and single character"""
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome(" ") == True

def test_numeric_palindromes():
    """Test palindromes with numbers"""
    assert is_palindrome("12321") == True
    assert is_palindrome("123 321") == True
    assert is_palindrome("1234") == False

def test_mixed_case():
    """Test palindromes with mixed case"""
    assert is_palindrome("Able was I ere I saw Elba") == True
    assert is_palindrome("Hello") == False

def test_special_characters():
    """Test palindromes with various special characters"""
    assert is_palindrome("A!b@c#c$b%a") == True
    assert is_palindrome("A man, a plan, a canal: Panama!") == True
    assert is_palindrome("Not a palindrome!") == False

def test_whitespace():
    """Test palindromes with different whitespace configurations"""
    assert is_palindrome("  racecar  ") == True
    assert is_palindrome(" a b c b a ") == True