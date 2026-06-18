import os
from yt_toolkit.utils import get_file_hash, logger, console

def find_duplicates(folder: str):
    """Scans a directory for duplicate MP3 files based on SHA-256 hashes."""
    hashes = {}
    duplicates_found = 0

    logger.info(f"Scanning [bold cyan]{folder}[/bold cyan] for duplicates...")
    
    for filename in os.listdir(folder):
        if not filename.lower().endswith(".mp3"):
            continue

        path = os.path.join(folder, filename)
        file_hash = get_file_hash(path)

        if file_hash in hashes:
            logger.warning(f"Duplicate: [bold]{filename}[/bold] -> Same as: [dim]{hashes[file_hash]}[/dim]")
            duplicates_found += 1
        else:
            hashes[file_hash] = filename

    console.print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", style="cyan")
    if duplicates_found > 0:
        logger.error(f"Scan complete. Found {duplicates_found} duplicate(s).")
    else:
        logger.info("Scan complete. ✓ No duplicates found.")
    logger.info(f"Unique files: {len(hashes)}")


def delete_duplicates(folder: str):
    """Scans a directory and securely deletes duplicate MP3 files."""
    hashes = {}
    deleted = 0

    logger.info(f"Scanning [bold cyan]{folder}[/bold cyan] and removing duplicates...")

    for filename in os.listdir(folder):
        if not filename.lower().endswith(".mp3"):
            continue

        path = os.path.join(folder, filename)
        file_hash = get_file_hash(path)

        if file_hash in hashes:
            logger.warning(f"Deleting duplicate: [bold]{filename}[/bold] (Duplicate of: [dim]{hashes[file_hash]}[/dim])")
            try:
                os.remove(path)
                deleted += 1
            except Exception as e:
                logger.error(f"Failed to delete {filename}: {e}")
        else:
            hashes[file_hash] = filename

    console.print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", style="cyan")
    logger.info(f"Finished! ✓ Deleted {deleted} duplicate file(s).")
    logger.info(f"Remaining unique songs: {len(hashes)}")