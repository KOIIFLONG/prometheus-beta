"""
LZ78 Compression Algorithm Implementation

This module provides functions for LZ78 compression and decompression.
LZ78 is a dictionary-based lossless compression algorithm that builds 
a dictionary of previously seen sequences during compression.
"""

class LZ78Compressor:
    """
    LZ78 compression and decompression utility.
    
    The algorithm works by building a dynamic dictionary of previously 
    seen sequences during compression and decompression.
    """
    
    @staticmethod
    def compress(input_data):
        """
        Compress the input data using LZ78 compression algorithm.
        
        Args:
            input_data (str): The input string to be compressed.
        
        Returns:
            list: A list of tuples (index, character) representing compressed data.
        
        Raises:
            TypeError: If input is not a string.
            ValueError: If input is an empty string.
        """
        # Validate input
        if not isinstance(input_data, str):
            raise TypeError("Input must be a string")
        
        if not input_data:
            raise ValueError("Input cannot be an empty string")
        
        # Initialize dictionary and compression output
        dictionary = {0: ''}  # 0 represents the root/empty string
        dict_index = 1
        output = []
        current_sequence = ''
        
        # Compress the input
        for char in input_data:
            # Try to extend the current sequence
            extended_sequence = current_sequence + char
            
            # Check if extended sequence is in dictionary
            found = False
            for index, seq in dictionary.items():
                if seq == extended_sequence:
                    current_sequence = extended_sequence
                    found = True
                    break
            
            # If not found, add to output and update dictionary
            if not found:
                # Find the index of the current sequence
                prev_index = 0
                for idx, seq in dictionary.items():
                    if seq == current_sequence:
                        prev_index = idx
                        break
                
                # Add to output and dictionary
                output.append((prev_index, char))
                dictionary[dict_index] = extended_sequence
                dict_index += 1
                
                # Reset current sequence
                current_sequence = ''
        
        # Handle the last sequence if any
        if current_sequence:
            prev_index = 0
            for idx, seq in dictionary.items():
                if seq == current_sequence:
                    prev_index = idx
                    break
            output.append((prev_index, ''))
        
        return output
    
    @staticmethod
    def decompress(compressed_data):
        """
        Decompress data compressed with LZ78 algorithm.
        
        Args:
            compressed_data (list): List of tuples (index, character) 
                                    representing compressed data.
        
        Returns:
            str: The decompressed original string.
        
        Raises:
            TypeError: If input is not a list.
            ValueError: If input contains invalid compressed data.
        """
        # Validate input
        if not isinstance(compressed_data, list):
            raise TypeError("Input must be a list of tuples")
        
        # Initialize dictionary and output
        dictionary = {0: ''}
        dict_index = 1
        output = []
        
        # Decompress
        for index, char in compressed_data:
            # Validate input tuple
            if not isinstance(index, int) or not isinstance(char, str):
                raise ValueError(f"Invalid compressed data: {(index, char)}")
            
            # Retrieve the sequence for the given index
            if index not in dictionary:
                raise ValueError(f"Invalid dictionary index: {index}")
            
            # Get the sequence from dictionary
            sequence = dictionary[index]
            
            # Construct the new output sequence
            new_sequence = sequence + char if char else sequence
            output.append(new_sequence)
            
            # Add to dictionary if not empty
            if new_sequence:
                dictionary[dict_index] = new_sequence
                dict_index += 1
        
        # Join and return the decompressed string
        return ''.join(output)