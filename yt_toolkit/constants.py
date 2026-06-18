from importlib.metadata import version, PackageNotFoundError

APP_NAME = "yt-toolkit"

try:
    # Pulls version dynamically from pyproject.toml / installed package
    VERSION = version(APP_NAME)
except PackageNotFoundError:
    # Fallback for local development before running 'pip install -e .'
    VERSION = "2.0.0"

DEFAULT_AUDIO_QUALITY = "320"
DEFAULT_AUDIO_FORMAT = "mp3"
CONFIG_FILENAME = "config.json"