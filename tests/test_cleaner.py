import os
import pytest
from yt_toolkit.cleaner import clean_filenames

# This is a Pytest fixture. It creates a temporary directory for testing,
# puts some dummy files in it, and cleans it up after the test is done.
@pytest.fixture
def temp_music_folder(tmp_path):
    # Create dummy files
    files = [
        "01 - Bohemian Rhapsody.mp3",
        "02-Hotel California.mp3",
        "Just A Normal Song.mp3",
        "100 - Valid Song.mp3"
    ]
    
    for file in files:
        (tmp_path / file).touch()
        
    return str(tmp_path)

def test_clean_filenames_removes_numbers(temp_music_folder):
    """Test that the cleaner correctly strips leading numbers and hyphens."""
    
    # Run the cleaner on our temporary folder
    clean_filenames(temp_music_folder)
    
    # Get the new list of files
    resulting_files = set(os.listdir(temp_music_folder))
    
    # Assert that the files were renamed correctly
    expected_files = {
        "Bohemian Rhapsody.mp3",
        "Hotel California.mp3",
        "Just A Normal Song.mp3",
        "Valid Song.mp3"
    }
    
    assert resulting_files == expected_files