import os
import pytest
from yt_toolkit.duplicates import delete_duplicates, find_duplicates

@pytest.fixture
def mock_audio_folder(tmp_path):
    """Creates a temporary directory with unique and duplicate mock MP3s."""
    
    # 1. Create a completely unique file
    file_unique = tmp_path / "01 - Unique Song.mp3"
    file_unique.write_bytes(b"Unique audio data A")

    # 2. Create the original of a song
    file_dup1 = tmp_path / "02 - Awesome Song.mp3"
    file_dup1.write_bytes(b"Identical audio data B")

    # 3. Create a duplicate of the previous song (exact same bytes)
    file_dup2 = tmp_path / "Awesome Song (Copy).mp3"
    file_dup2.write_bytes(b"Identical audio data B")

    # 4. Create a non-mp3 file (even with same bytes, it should be ignored)
    file_txt = tmp_path / "notes.txt"
    file_txt.write_bytes(b"Identical audio data B")

    return str(tmp_path)

def test_delete_duplicates(mock_audio_folder):
    """Test that identical mp3 files are deleted, keeping only one copy."""
    
    # Run the deletion command on the mock folder
    delete_duplicates(mock_audio_folder)
    
    # Check what files survived
    remaining_files = set(os.listdir(mock_audio_folder))
    
    # The unique song and the txt file MUST remain
    assert "01 - Unique Song.mp3" in remaining_files
    assert "notes.txt" in remaining_files
    
    # For the duplicates, exactly ONE should survive.
    # (os.listdir order dictates which gets kept, so we check using XOR)
    dup1_exists = "02 - Awesome Song.mp3" in remaining_files
    dup2_exists = "Awesome Song (Copy).mp3" in remaining_files
    
    assert dup1_exists != dup2_exists  # One must be True, the other False
    
    # Total files remaining should be exactly 3
    assert len(remaining_files) == 3