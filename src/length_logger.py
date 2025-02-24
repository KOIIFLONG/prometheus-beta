import logging
from typing import Union, Sequence

def log_length(item: Union[str, Sequence]) -> int:
    """
    Log the length of a given string or array/sequence.

    Args:
        item (str or Sequence): The input to measure the length of.
    
    Returns:
        int: The length of the input.
    
    Raises:
        TypeError: If the input is not a string or sequence.
    """
    # Validate input type
    if not isinstance(item, (str, Sequence)):
        raise TypeError("Input must be a string or a sequence (list, tuple, etc.)")
    
    # Get the length
    length = len(item)
    
    # Log the length using the default logger
    logging.info(f"Length of input: {length}")
    
    return length