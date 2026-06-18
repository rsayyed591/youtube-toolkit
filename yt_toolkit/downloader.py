import os
import yt_dlp
from yt_toolkit.config import load_config
from yt_toolkit.utils import logger

def get_download_path() -> str:
    """Helper to get the configured download folder and ensure it exists."""
    config = load_config()
    folder = config.get("download_folder", os.path.join(os.path.expanduser("~"), "Downloads"))
    os.makedirs(folder, exist_ok=True)
    return folder

def download_video(url: str):
    folder = get_download_path()
    ydl_opts = {
        "format": "bestvideo+bestaudio/best",
        "outtmpl": os.path.join(folder, "%(title)s.%(ext)s"),
        "merge_output_format": "mp4",
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def download_mp3(url: str):
    folder = get_download_path()
    config = load_config()
    quality = config.get("quality", "320")
    
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(folder, "%(title)s.%(ext)s"),
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": quality,
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def download_playlist_mp3(url: str):
    folder = get_download_path()
    config = load_config()
    quality = config.get("quality", "320")

    ydl_opts = {
        "format": "bestaudio/best",
        "extractor_args": {"youtube": {"player_client": ["android"]}},
        "outtmpl": os.path.join(folder, "%(playlist)s", "%(playlist_index)04d - %(title)s.%(ext)s"),
        "ignoreerrors": True,
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": quality,
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])