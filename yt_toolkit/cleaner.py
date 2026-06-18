import os
import re
from yt_toolkit.utils import logger, console

def clean_filenames(folder: str):
    """Removes leading numbers from mp3 files in a directory."""
    if not os.path.exists(folder):
        logger.error(f"The folder [cyan]{folder}[/cyan] does not exist.")
        return

    logger.info(f"Cleaning filenames in [cyan]{folder}[/cyan]...")
    renamed_count = 0

    for filename in os.listdir(folder):
        if not filename.lower().endswith(".mp3"):
            continue
        
        # Regex: matches leading numbers, followed by optional spaces and a hyphen
        new_filename = re.sub(r"^\d+\s*-\s*", "", filename)
        
        if new_filename == filename:
            continue
            
        old_path = os.path.join(folder, filename)
        new_path = os.path.join(folder, new_filename)

        try:
            if os.path.exists(new_path):
                logger.warning(f"Skipped: [bold]{new_filename}[/bold] already exists.")
            else:
                os.rename(old_path, new_path)
                logger.info(f"Renamed: [dim]{filename}[/dim] -> [green]{new_filename}[/green]")
                renamed_count += 1
        except Exception as e:
            logger.error(f"Error renaming {filename}: {e}")

    console.print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", style="cyan")
    logger.info(f"Clean complete. ✓ {renamed_count} files renamed.")