import os
import shutil
import urllib.request
from yt_toolkit.utils import console
from yt_toolkit.config import load_config

def run_diagnostics():
    """Runs system checks and prints a beautiful Rich report."""
    console.print("\n[bold cyan]Running System Diagnostics...[/bold cyan]\n")
    
    issues = 0

    # 1. Check FFmpeg
    if shutil.which("ffmpeg"):
        console.print("[green]✓[/green] FFmpeg installed")
    else:
        console.print("[red]✗[/red] FFmpeg not found! Audio extraction will fail.")
        issues += 1

    # 2. Check Node.js (Anti-Bot Bypass)
    if shutil.which("node"):
        console.print("[green]✓[/green] Node.js installed (Anti-bot bypass active)")
    else:
        console.print("[yellow]![/yellow] Node.js missing! (YouTube may block your downloads. Install from nodejs.org)")

    # 3. Check Internet
    try:
        # Pinging a standard domain to avoid Python IP/SSL mismatch errors
        urllib.request.urlopen("https://www.google.com", timeout=3)
        console.print("[green]✓[/green] Internet connection active")
    except Exception as e:
        console.print(f"[red]✗[/red] No internet connection detected")
        issues += 1

    # 4. Check Config & Permissions
    config = load_config()
    folder = config.get("download_folder", "")
    
    if os.path.exists(folder):
        if os.access(folder, os.W_OK):
            console.print(f"[green]✓[/green] Download folder ready ({folder})")
        else:
            console.print(f"[red]✗[/red] No write permission in download folder ({folder})")
            issues += 1
    else:
        console.print(f"[yellow]![/yellow] Download folder does not exist yet (will be created): {folder}")

    console.print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", style="cyan")
    if issues == 0:
        console.print("[bold green]System is healthy! You are ready to download.[/bold green]")
    else:
        console.print(f"[bold red]Found {issues} issue(s) that need your attention.[/bold red]")

    