import zstandard as zstd

def compress_data(data):
    """
    Compress input data using Zstandard compression algorithm.

    Args:
        data (bytes or str): The data to be compressed. 
                              If str is provided, it will be encoded to bytes.

    Returns:
        bytes: Compressed data

    Raises:
        TypeError: If input is not bytes or str
        ValueError: If input is empty
    """
    # Validate input type
    if not isinstance(data, (bytes, str)):
        raise TypeError("Input must be bytes or str")
    
    # Convert str to bytes if necessary
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Check for empty input
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Create compressor
    cctx = zstd.ZstdCompressor()
    
    # Compress data
    return cctx.compress(data)

def decompress_data(compressed_data):
    """
    Decompress data that was compressed with Zstandard.

    Args:
        compressed_data (bytes): The compressed data to decompress

    Returns:
        bytes: Decompressed data

    Raises:
        TypeError: If input is not bytes
        ValueError: If input is empty or invalid
    """
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    # Check for empty input
    if not compressed_data:
        raise ValueError("Input data cannot be empty")
    
    # Create decompressor
    dctx = zstd.ZstdDecompressor()
    
    # Decompress data
    return dctx.decompress(compressed_data)