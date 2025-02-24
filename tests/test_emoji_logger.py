import logging
import pytest
import io
import sys
from src.emoji_logger import log_emoji_message

def test_log_message_without_emoji(caplog):
    """Test logging a message without an emoji"""
    caplog.set_level(logging.INFO)
    log_emoji_message("Test message")
    assert "Test message" in caplog.text

def test_log_message_with_emoji(caplog):
    """Test logging a message with an emoji"""
    caplog.set_level(logging.INFO)
    log_emoji_message("Hello", emoji_symbol=":smile:")
    assert "😄 Hello" in caplog.text

def test_different_log_levels(caplog):
    """Test logging at different levels"""
    levels = ['debug', 'info', 'warning', 'error', 'critical']
    for level in levels:
        caplog.clear()
        caplog.set_level(logging.DEBUG)
        log_emoji_message(f"Test {level} message", level=level, emoji_symbol=":rocket:")
        assert f"🚀 Test {level} message" in caplog.text

def test_invalid_log_level():
    """Test that an invalid log level raises a ValueError"""
    with pytest.raises(ValueError, match="Invalid logging level"):
        log_emoji_message("Test", level="invalid")

def test_invalid_message_type():
    """Test that non-string message raises a TypeError"""
    with pytest.raises(TypeError, match="Message must be a string"):
        log_emoji_message(123)

def test_invalid_emoji_symbol(caplog):
    """Test behavior with invalid emoji symbol"""
    caplog.set_level(logging.INFO)
    log_emoji_message("Test", emoji_symbol="invalid_emoji")
    assert "Test" in caplog.text  # Should log without emoji