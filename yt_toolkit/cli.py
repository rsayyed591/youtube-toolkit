import platform
import typer
import yt_dlp
from rich.table import Table
from rich.prompt import Prompt

# Tool imports
from yt_toolkit.constants import VERSION, APP_NAME
from yt_toolkit.utils import console
from yt_toolkit.config import load_config, save_config
from yt_toolkit.doctor import run_diagnostics
from yt_toolkit.downloader import download_video, download_mp3, download_playlist_mp3
from yt_toolkit.cleaner import clean_filenames
from yt_toolkit.duplicates import find_duplicates, delete_duplicates

app = typer.Typer(help="🎵 Professional YouTube toolkit for downloading and managing music.")

def display_banner():
    """Prints a professional header for tool commands."""
    console.print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", style="cyan")
    console.print(f"🎵 [bold green]{APP_NAME.upper()}[/bold green] v{VERSION}")
    console.print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", style="cyan")

@app.command()
def version():
    """Display system and version info."""
    table = Table(show_header=False, border_style="cyan")
    table.add_column("Component", style="bold green")
    table.add_column("Version", style="white")
    
    table.add_row("YT Toolkit", VERSION)
    table.add_row("Python", platform.python_version())
    table.add_row("yt-dlp", yt_dlp.version.__version__)
    
    console.print(table)

@app.command()
def config():
    """Interactively configure the application."""
    display_banner()
    current_config = load_config()
    
    console.print("[cyan]Press Enter to keep current values.[/cyan]\n")
    
    new_folder = Prompt.ask(
        "Download folder", 
        default=current_config.get("download_folder")
    )
    new_quality = Prompt.ask(
        "Audio quality (kbps)", 
        default=current_config.get("quality", "320")
    )
    
    updated_config = {
        **current_config,
        "download_folder": new_folder,
        "quality": new_quality
    }
    
    save_config(updated_config)
    console.print("\n[bold green]✓ Configuration saved![/bold green]")

@app.command()
def doctor():
    """Check system health (FFmpeg, internet, folders)."""
    display_banner()
    run_diagnostics()

@app.command()
def video(url: str = typer.Argument(..., help="The URL of the YouTube video")):
    """[URL] Download a video in the highest quality."""
    display_banner()
    download_video(url)

@app.command()
def mp3(url: str = typer.Argument(..., help="The URL of the YouTube video")):
    """[URL] Download a video and convert it to MP3."""
    display_banner()
    download_mp3(url)

@app.command()
def playlist(url: str = typer.Argument(..., help="The URL of the YouTube playlist")):
    """[URL] Download an entire playlist as MP3s."""
    display_banner()
    download_playlist_mp3(url)

@app.command()
def clean(folder: str = typer.Argument(..., help="The path to the folder to clean")):
    """[FOLDER] Remove numbered prefixes from MP3 files."""
    display_banner()
    clean_filenames(folder)

@app.command(name="find-duplicates")
def scan(folder: str = typer.Argument(..., help="The path to the folder to scan")):
    """[FOLDER] Scan a directory for duplicate MP3 files."""
    display_banner()
    find_duplicates(folder)

@app.command(name="remove-duplicates")
def dedupe(folder: str = typer.Argument(..., help="The path to the folder to clean")):
    """[FOLDER] Safely delete duplicate MP3 files in a directory."""
    display_banner()
    delete_duplicates(folder)

if __name__ == "__main__":
    app()