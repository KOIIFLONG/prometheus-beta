import os
import zipfile
import pytest
import tempfile
import shutil

from src.zip_archiver import create_zip_archive


def test_create_zip_archive_single_file():
    """Test creating a zip archive with a single file."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a test file
        test_file_path = os.path.join(temp_dir, 'test_file.txt')
        with open(test_file_path, 'w') as f:
            f.write('Test content')

        # Define output zip path
        output_zip_path = os.path.join(temp_dir, 'output.zip')

        # Create zip archive
        result = create_zip_archive([test_file_path], output_zip_path)
        assert result is True

        # Verify the zip file was created
        assert os.path.exists(output_zip_path)

        # Verify contents of the zip file
        with zipfile.ZipFile(output_zip_path, 'r') as zipf:
            assert len(zipf.namelist()) == 1
            assert 'test_file.txt' in zipf.namelist()


def test_create_zip_archive_multiple_files():
    """Test creating a zip archive with multiple files."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create test files
        files = []
        for i in range(3):
            file_path = os.path.join(temp_dir, f'test_file_{i}.txt')
            with open(file_path, 'w') as f:
                f.write(f'Test content {i}')
            files.append(file_path)

        # Define output zip path
        output_zip_path = os.path.join(temp_dir, 'output.zip')

        # Create zip archive
        result = create_zip_archive(files, output_zip_path)
        assert result is True

        # Verify the zip file was created
        assert os.path.exists(output_zip_path)

        # Verify contents of the zip file
        with zipfile.ZipFile(output_zip_path, 'r') as zipf:
            assert len(zipf.namelist()) == 3
            for i in range(3):
                assert f'test_file_{i}.txt' in zipf.namelist()


def test_create_zip_archive_empty_file_list():
    """Test that an empty file list raises a ValueError."""
    with tempfile.TemporaryDirectory() as temp_dir:
        output_zip_path = os.path.join(temp_dir, 'output.zip')

        with pytest.raises(ValueError, match="No files provided for zip archive"):
            create_zip_archive([], output_zip_path)


def test_create_zip_archive_non_existent_file():
    """Test that non-existent files raise a ValueError."""
    with tempfile.TemporaryDirectory() as temp_dir:
        non_existent_file = os.path.join(temp_dir, 'non_existent.txt')
        output_zip_path = os.path.join(temp_dir, 'output.zip')

        with pytest.raises(ValueError, match="The following files do not exist"):
            create_zip_archive([non_existent_file], output_zip_path)


def test_create_zip_archive_preserves_filename():
    """Test that the original filename is preserved in the zip archive."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a test file
        test_file_path = os.path.join(temp_dir, 'unique_filename.txt')
        with open(test_file_path, 'w') as f:
            f.write('Test content')

        # Define output zip path
        output_zip_path = os.path.join(temp_dir, 'output.zip')

        # Create zip archive
        create_zip_archive([test_file_path], output_zip_path)

        # Verify contents of the zip file
        with zipfile.ZipFile(output_zip_path, 'r') as zipf:
            assert 'unique_filename.txt' in zipf.namelist()


def test_create_zip_archive_output_directory_creation():
    """Test that the function creates necessary directories for the output path."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a test file
        test_file_path = os.path.join(temp_dir, 'test_file.txt')
        with open(test_file_path, 'w') as f:
            f.write('Test content')

        # Define output zip path in a nested directory that doesn't exist
        nested_dir = os.path.join(temp_dir, 'nested', 'path')
        output_zip_path = os.path.join(nested_dir, 'output.zip')

        # Create zip archive
        create_zip_archive([test_file_path], output_zip_path)

        # Verify the zip file was created
        assert os.path.exists(output_zip_path)