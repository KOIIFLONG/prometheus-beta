import os
import pytest
from datetime import datetime, timedelta
import time

from src.file_modified_date import get_file_last_modified_date


def test_get_file_last_modified_date_existing_file(tmp_path):
    """Test getting last modified date for an existing file."""
    # Create a temporary file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Test content")
    
    # Wait a moment to ensure timestamp is different
    time.sleep(0.1)
    
    # Get the last modified date
    modified_date = get_file_last_modified_date(str(test_file))
    
    # Assert it's a datetime object
    assert isinstance(modified_date, datetime)
    
    # Check if the modified date is very recent (within the last 5 seconds)
    assert datetime.now() - modified_date < timedelta(seconds=5)


def test_get_file_last_modified_date_nonexistent_file():
    """Test that FileNotFoundError is raised for non-existent file."""
    with pytest.raises(FileNotFoundError):
        get_file_last_modified_date("non_existent_file_123456.txt")


def test_get_file_last_modified_date_recent_modification(tmp_path):
    """Test that the function reflects recent file modifications."""
    # Create a temporary file
    test_file = tmp_path / "modification_test.txt"
    test_file.write_text("Initial content")
    
    # Get initial modified date
    initial_date = get_file_last_modified_date(str(test_file))
    
    # Wait a moment
    time.sleep(0.1)
    
    # Modify the file
    test_file.write_text("Updated content")
    
    # Get new modified date
    new_date = get_file_last_modified_date(str(test_file))
    
    # Assert that the dates are different
    assert new_date > initial_date