import pytest
from src.parentheses_validator import is_valid_parentheses

def test_valid_parentheses():
    """Test various valid parentheses combinations."""
    assert is_valid_parentheses("()") == True
    assert is_valid_parentheses("((()))") == True
    assert is_valid_parentheses("()()") == True
    assert is_valid_parentheses("(())()") == True
    assert is_valid_parentheses("") == True

def test_invalid_parentheses():
    """Test various invalid parentheses combinations."""
    assert is_valid_parentheses(")(") == False
    assert is_valid_parentheses("(()") == False
    assert is_valid_parentheses("())") == False
    assert is_valid_parentheses("((()") == False

def test_complex_parentheses():
    """Test more complex parentheses scenarios."""
    assert is_valid_parentheses("((()()))") == True
    assert is_valid_parentheses("(()())(()())") == True
    assert is_valid_parentheses("((()))()") == True

def test_only_parentheses():
    """Ensure function works with strings containing only parentheses."""
    assert is_valid_parentheses("(") == False
    assert is_valid_parentheses(")") == False
    assert is_valid_parentheses("()()()") == True

def test_mixed_content():
    """Test parentheses in strings with other characters."""
    assert is_valid_parentheses("a(b)c") == True
    assert is_valid_parentheses("(a(b)c)") == True
    assert is_valid_parentheses("a(b(c)d)e") == True
    assert is_valid_parentheses("a)(b") == False