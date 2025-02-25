import os
import zipfile
from typing import List, Union


def create_zip_archive(files: List[str], output_path: str) -> bool:
    """
    Create a zip archive containing specified files.

    Args:
        files (List[str]): List of file paths to be added to the zip archive.
        output_path (str): Path where the zip archive will be created.

    Returns:
        bool: True if the zip archive was created successfully, False otherwise.

    Raises:
        ValueError: If the input list is empty or contains invalid file paths.
        IOError: If there are issues creating the zip archive.
    """
    # Validate input
    if not files:
        raise ValueError("No files provided for zip archive")

    # Validate that all files exist
    non_existent_files = [f for f in files if not os.path.isfile(f)]
    if non_existent_files:
        raise ValueError(f"The following files do not exist: {non_existent_files}")

    try:
        # Ensure the directory for the output path exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # Create the zip file
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file_path in files:
                # Add file to the zip, preserving the original filename
                zipf.write(file_path, os.path.basename(file_path))

        return True

    except (IOError, PermissionError) as e:
        raise IOError(f"Failed to create zip archive: {str(e)}")