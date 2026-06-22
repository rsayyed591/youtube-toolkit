import json
import os
from pathlib import Path
from yt_toolkit.constants import CONFIG_FILENAME, DEFAULT_AUDIO_QUALITY
from yt_toolkit.utils import logger

# 1. This magically finds exactly where your 'youtube-toolkit' folder is located
PROJECT_ROOT = Path(__file__).resolve().parent.parent

def get_config_path() -> Path:
    """Returns the path to the config file directly inside the project folder."""
    # This will save it as Youtube Video Downloader/config.json
    return PROJECT_ROOT / CONFIG_FILENAME

def load_config() -> dict:
    """Loads the user configuration, or returns defaults if none exists."""
    config_path = get_config_path()
    
    # 2. We now set the defaults to stay inside your project folder too!
    default_config = {
        "download_folder": str(PROJECT_ROOT / "Downloads"),
        "quality": DEFAULT_AUDIO_QUALITY,
        "cookies_path": str(PROJECT_ROOT / "cookies.txt")
    }

    if not config_path.exists():
        return default_config

    try:
        with open(config_path, "r") as f:
            user_config = json.load(f)
            return {**default_config, **user_config}
    except Exception as e:
        logger.error(f"Failed to load config: {e}. Using defaults.")
        return default_config

def save_config(new_config: dict):
    """Saves the configuration dictionary to disk."""
    config_path = get_config_path()
    try:
        with open(config_path, "w") as f:
            json.dump(new_config, f, indent=4)
        logger.info(f"Configuration saved to [cyan]{config_path}[/cyan]")
    except Exception as e:
        logger.error(f"Failed to save config: {e}")