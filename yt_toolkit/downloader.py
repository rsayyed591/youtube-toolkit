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

def get_auth_opts() -> dict:
    """Helper to safely load cookies and explicitly enable the Node.js runtime."""
    config = load_config()
    opts = {
        # Explicitly map Node.js for the EJS challenge solver
        "js_runtimes": {"node": {}},
    }
    
    cookies_path = config.get("cookies_path", "")
    if cookies_path and os.path.exists(cookies_path):
        logger.info("[dim]Authenticating using configured cookies.txt...[/dim]")
        opts["cookiefile"] = cookies_path
        
    return opts

def download_video(url: str):
    folder = get_download_path()
    ydl_opts = {
        "format": "bestvideo+bestaudio/best",
        "outtmpl": os.path.join(folder, "%(title)s.%(ext)s"),
        "merge_output_format": "mp4",
        # Spoofing mobile clients bypasses strict web blockades
        "extractor_args": {"youtube": {"player_client": ["android", "web"]}},
        **get_auth_opts()
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
        "extractor_args": {"youtube": {"player_client": ["android", "web"]}},
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": quality,
        }],
        **get_auth_opts()
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def download_playlist_mp3(url: str):
    folder = get_download_path()
    config = load_config()
    quality = config.get("quality", "320")

    ydl_opts = {
        "format": "bestaudio/best",
        "extractor_args": {"youtube": {"player_client": ["android", "web"]}},
        "outtmpl": os.path.join(folder, "%(playlist)s", "%(playlist_index)04d - %(title)s.%(ext)s"),
        "ignoreerrors": True,
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": quality,
        }],
        **get_auth_opts()
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])