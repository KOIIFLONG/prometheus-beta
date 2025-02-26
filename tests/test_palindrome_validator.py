import pytest
from src.palindrome_validator import is_palindrome

def test_simple_palindrome():
    assert is_palindrome("racecar") == True

def test_palindrome_with_spaces():
    assert is_palindrome("race car") == True

def test_palindrome_mixed_case():
    assert is_palindrome("Able was I ere I saw Elba") == True

def test_palindrome_with_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama") == True

def test_non_palindrome():
    assert is_palindrome("hello") == False

def test_empty_string():
    assert is_palindrome("") == True

def test_single_character():
    assert is_palindrome("a") == True

def test_palindrome_with_numbers():
    assert is_palindrome("123321") == True

def test_palindrome_mixed_alphanumeric():
    assert is_palindrome("R2acec3aR2") == True

def test_non_palindrome_with_punctuation():
    assert is_palindrome("Was it a car or a dog I saw?") == False