import string

def find_longest_word(sentence):
    """
    Find the longest word in a given sentence.

    Args:
        sentence (str): The input sentence to search for the longest word.

    Returns:
        str: The longest word in the sentence. If multiple words have the same 
             maximum length, returns the first occurrence.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If the input string is empty or contains only whitespace.
    """
    # Check for invalid input
    if not isinstance(sentence, str):
        raise TypeError("Input must be a string")
    
    # Remove leading/trailing whitespace and check for empty string
    sentence = sentence.strip()
    if not sentence:
        raise ValueError("Input sentence cannot be empty")
    
    # Remove punctuation and split the sentence into words
    # Translate removes punctuation, keeping only alphanumeric characters
    translator = str.maketrans('', '', string.punctuation)
    words = [word.translate(translator) for word in sentence.split()]
    
    # Find the longest word
    return max(words, key=len)