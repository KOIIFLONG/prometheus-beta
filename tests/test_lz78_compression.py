"""
Test suite for LZ78 Compression Algorithm
"""

import pytest
from src.lz78_compression import LZ78Compressor

def test_basic_compression():
    """Test basic string compression and decompression"""
    input_str = "TOBEORNOTTOBEORTOBEORNOT"
    compressed = LZ78Compressor.compress(input_str)
    decompressed = LZ78Compressor.decompress(compressed)
    assert decompressed == input_str

def test_empty_string_raises_error():
    """Test that empty string raises ValueError"""
    with pytest.raises(ValueError, match="Input cannot be an empty string"):
        LZ78Compressor.compress("")

def test_non_string_input_raises_error():
    """Test that non-string input raises TypeError"""
    with pytest.raises(TypeError, match="Input must be a string"):
        LZ78Compressor.compress(123)

def test_simple_repetitive_string():
    """Test compression of a simple repetitive string"""
    input_str = "AAAAAAAA"
    compressed = LZ78Compressor.compress(input_str)
    decompressed = LZ78Compressor.decompress(compressed)
    assert decompressed == input_str

def test_mixed_characters():
    """Test compression of a string with mixed characters"""
    input_str = "Hello, World! Hello, World!"
    compressed = LZ78Compressor.compress(input_str)
    decompressed = LZ78Compressor.decompress(compressed)
    assert decompressed == input_str

def test_compression_invalid_input():
    """Test compression with invalid compressed data"""
    with pytest.raises(TypeError, match="Input must be a list of tuples"):
        LZ78Compressor.decompress("not a list")
    
    with pytest.raises(ValueError, match="Invalid compressed data"):
        LZ78Compressor.decompress([(1, 2)])  # Invalid tuple types

def test_compression_invalid_dictionary_index():
    """Test decompression with invalid dictionary index"""
    with pytest.raises(ValueError, match="Invalid dictionary index"):
        LZ78Compressor.decompress([(999, 'a')])

def test_single_character_string():
    """Test compression of a single character string"""
    input_str = "A"
    compressed = LZ78Compressor.compress(input_str)
    decompressed = LZ78Compressor.decompress(compressed)
    assert decompressed == input_str

def test_unicode_characters():
    """Test compression with unicode characters"""
    input_str = "こんにちは世界"
    compressed = LZ78Compressor.compress(input_str)
    decompressed = LZ78Compressor.decompress(compressed)
    assert decompressed == input_str