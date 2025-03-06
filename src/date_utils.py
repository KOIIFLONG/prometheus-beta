from datetime import datetime, timedelta

def add_days_to_date(input_date, days_to_add):
    """
    Add a specified number of days to a given date.

    Args:
        input_date (str or datetime): The starting date in 'YYYY-MM-DD' format or datetime object
        days_to_add (int): Number of days to add to the input date

    Returns:
        datetime: A new datetime object representing the date after adding specified days

    Raises:
        ValueError: If input_date is not a valid date or days_to_add is not an integer
        TypeError: If input types are incorrect
    """
    # Validate input types
    if not isinstance(days_to_add, int):
        raise TypeError("days_to_add must be an integer")

    # Convert input to datetime if it's a string
    if isinstance(input_date, str):
        try:
            input_date = datetime.strptime(input_date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("input_date must be in 'YYYY-MM-DD' format")
    
    # Validate input_date is a datetime object
    if not isinstance(input_date, datetime):
        raise TypeError("input_date must be a datetime object or a string in 'YYYY-MM-DD' format")

    # Add days and return the new date
    return input_date + timedelta(days=days_to_add)