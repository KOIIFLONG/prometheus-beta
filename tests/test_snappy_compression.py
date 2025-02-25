import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from snappy_compression import compress_data, decompress_data

def test_compress_decompress_bytes():
    """Test compression and decompression with bytes"""
    original_data = b'Hello, Snappy compression!'
    compressed = compress_data(original_data)
    assert compressed != original_data
    decompressed = decompress_data(compressed)
    assert decompressed == original_data

def test_compress_decompress_str():
    """Test compression and decompression with string"""
    original_data = 'Hello, Snappy compression!'
    compressed = compress_data(original_data)
    assert compressed != original_data.encode('utf-8')
    decompressed = decompress_data(compressed)
    assert decompressed == original_data.encode('utf-8')

def test_compress_empty_input_raises_error():
    """Test that empty input raises a ValueError"""
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        compress_data(b'')
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        compress_data('')

def test_decompress_empty_input_raises_error():
    """Test that empty input for decompression raises a ValueError"""
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        decompress_data(b'')

def test_invalid_input_type_raises_error():
    """Test that invalid input types raise TypeError"""
    with pytest.raises(TypeError, match="Input must be bytes or str"):
        compress_data(123)
    with pytest.raises(TypeError, match="Input must be bytes"):
        decompress_data('not bytes')

def test_large_data_compression():
    """Test compression and decompression of large data"""
    large_data = b'A' * 10000
    compressed = compress_data(large_data)
    assert len(compressed) < len(large_data)
    decompressed = decompress_data(compressed)
    assert decompressed == large_data

def test_repeated_data_compression():
    """Test compression of highly repetitive data"""
    repeated_data = b'ABCDEFG' * 1000
    compressed = compress_data(repeated_data)
    assert len(compressed) < len(repeated_data)
    decompressed = decompress_data(compressed)
    assert decompressed == repeated_data