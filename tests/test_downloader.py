from unittest.mock import patch
from yt_toolkit.downloader import download_mp3

@patch("yt_toolkit.downloader.yt_dlp.YoutubeDL")
def test_download_mp3_calls_ydl(mock_ydl_class):
    """Tests that our code correctly configures and calls yt-dlp."""
    
    # Setup our mock instance
    mock_instance = mock_ydl_class.return_value.__enter__.return_value
    
    # Run the function
    test_url = "https://youtube.com/watch?v=dummy"
    download_mp3(test_url)
    
    # Verify YoutubeDL was instantiated
    mock_ydl_class.assert_called_once()
    
    # Verify the download method was called with our URL
    mock_instance.download.assert_called_once_with([test_url])