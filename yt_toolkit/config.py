import json
import os
from pathlib import Path
from yt_toolkit.constants import CONFIG_FILENAME, DEFAULT_AUDIO_QUALITY
from yt_toolkit.utils import logger

def get_config_path() -> Path:
    """Returns the path to the config file in the user's home directory."""
    return Path.home() / f".{CONFIG_FILENAME}"

def load_config() -> dict:
    """Loads the user configuration, or returns defaults if none exists."""
    config_path = get_config_path()
    
    default_config = {
        "download_folder": os.path.join(Path.home(), "Downloads"),
        "quality": DEFAULT_AUDIO_QUALITY,
        "cookies_path": ""
    }

    if not config_path.exists():
        return default_config

    try:
        with open(config_path, "r") as f:
            user_config = json.load(f)
            # Merge user config with defaults in case of missing keys
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