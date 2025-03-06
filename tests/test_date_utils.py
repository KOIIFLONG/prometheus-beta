import pytest
from datetime import datetime, timedelta
from src.date_utils import add_days_to_date

def test_add_days_to_date_string_input():
    """Test adding days to a date using string input"""
    result = add_days_to_date('2023-01-01', 5)
    assert result == datetime(2023, 1, 6)

def test_add_days_to_date_datetime_input():
    """Test adding days to a date using datetime input"""
    input_date = datetime(2023, 1, 1)
    result = add_days_to_date(input_date, 5)
    assert result == datetime(2023, 1, 6)

def test_add_zero_days():
    """Test adding zero days"""
    result = add_days_to_date('2023-01-01', 0)
    assert result == datetime(2023, 1, 1)

def test_add_negative_days():
    """Test adding negative days"""
    result = add_days_to_date('2023-01-10', -5)
    assert result == datetime(2023, 1, 5)

def test_add_large_number_of_days():
    """Test adding a large number of days"""
    result = add_days_to_date('2023-01-01', 365)
    assert result == datetime(2024, 1, 1)

def test_invalid_date_string():
    """Test invalid date string format"""
    with pytest.raises(ValueError):
        add_days_to_date('2023/01/01', 5)

def test_invalid_days_type():
    """Test invalid type for days_to_add"""
    with pytest.raises(TypeError):
        add_days_to_date('2023-01-01', '5')

def test_invalid_date_type():
    """Test invalid input date type"""
    with pytest.raises(TypeError):
        add_days_to_date(12345, 5)