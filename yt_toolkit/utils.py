import hashlib
import logging
from rich.console import Console
from rich.logging import RichHandler

# Global Rich console for beautiful output
console = Console()

# Professional logging setup replacing standard print()
logging.basicConfig(
    level="INFO",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(console=console, rich_tracebacks=True, show_path=False)]
)

logger = logging.getLogger("yt_toolkit")

def get_file_hash(path: str) -> str:
    """Calculates SHA-256 hash of a file for duplicate detection."""
    sha = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            chunk = f.read(1024 * 1024)
            if not chunk:
                break
            sha.update(chunk)
    return sha.hexdigest()