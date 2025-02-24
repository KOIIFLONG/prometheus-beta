import logging
import emoji

def log_emoji_message(message, level='info', emoji_symbol=None):
    """
    Log a message with an optional emoji symbol.

    Args:
        message (str): The message to log
        level (str, optional): Logging level. Defaults to 'info'.
            Supported levels: 'debug', 'info', 'warning', 'error', 'critical'
        emoji_symbol (str, optional): Emoji to prepend to the message.
            If None, no emoji is added.

    Returns:
        None

    Raises:
        ValueError: If an invalid logging level is provided
        TypeError: If message is not a string
    """
    # Validate input types
    if not isinstance(message, str):
        raise TypeError("Message must be a string")

    # Configure logging if not already configured
    logging.basicConfig(
        level=logging.INFO, 
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    # Validate and map logging level
    level_map = {
        'debug': logging.debug,
        'info': logging.info,
        'warning': logging.warning,
        'error': logging.error,
        'critical': logging.critical
    }

    if level not in level_map:
        raise ValueError(f"Invalid logging level. Choose from {list(level_map.keys())}")

    # Prepare the message with emoji if provided
    if emoji_symbol:
        # Validate emoji
        try:
            formatted_emoji = emoji.emojize(emoji_symbol, language='alias')
            log_message = f"{formatted_emoji} {message}"
        except TypeError:
            # If emoji conversion fails, log without emoji
            log_message = message
    else:
        log_message = message

    # Log the message at the specified level
    level_map[level](log_message)