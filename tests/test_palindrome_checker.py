import pytest
from src.palindrome_checker import is_palindrome

def test_classic_palindromes():
    """Test classic palindrome scenarios."""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False

def test_simple_palindromes():
    """Test simple palindrome cases."""
    assert is_palindrome("racecar") == True
    assert is_palindrome("Racecar") == True

def test_edge_cases():
    """Test edge cases including empty string and single character."""
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome(" ") == True

def test_numeric_palindromes():
    """Test palindromes with numbers."""
    assert is_palindrome("123321") == True
    assert is_palindrome("12321") == True
    assert is_palindrome("12345") == False

def test_mixed_palindromes():
    """Test palindromes with mixed characters and punctuation."""
    assert is_palindrome("Do geese see God?") == True
    assert is_palindrome("Was it a car or a cat I saw?") == True

def test_non_palindromes():
    """Test strings that are not palindromes."""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False
    assert is_palindrome("OpenAI") == False

def test_special_characters():
    """Test palindromes with various special characters."""
    assert is_palindrome("A! b@c#c b, a") == True
    assert is_palindrome("123-454-321") == True
    assert is_palindrome("No 'x' in Nixon?") == True