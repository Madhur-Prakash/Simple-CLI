import time
import importlib
from InquirerPy import inquirer
from rich.console import Console
from rich.live import Live
from rich.spinner import Spinner
from rich.style import Style

console = Console()
__package__ = "cli_tool"

ascii_art = r"""
  ____            _           _      
 |  _ \ ___  __ _| | ___  ___| | __  
 | |_) / _ \/ _` | |/ _ \/ __| |/ /  
 |  __/  __/ (_| | |  __/ (__|   <   
 |_|   \___|\__,_|_|\___|\___|_|\_\  
 
 Automate Your Repetitive Tasks
"""

def animate_ascii(ascii_str, delay=0.1):
    lines = ascii_str.strip("\n").split("\n")
    for i in range(len(lines)):
        console.print("\n".join(lines[:i+1]), style=Style(color="cyan", bold=True))
        time.sleep(delay)
        if i != len(lines) - 1:
            console.clear()
    # console.print("\n".join(lines), style=Style(color="cyan", bold=True))

def loading_animation(duration=1.25):
    spinner = Spinner("bouncingBall", text="Loading Simple-CLI...", style="bold magenta")
    with Live(spinner, refresh_per_second=12):
        time.sleep(duration)

COMMANDS = {
    "Setup New Python Project": "create",
    "Start Docker Container": "doc",
    "GitHub Automation": "github",
    "Install Dependencies": "inst",
    "Create a new Python Script": "new",
    "Install React": "react",
    "Generate Folder Structure": "structure",
    "Create File": "touch",
}

def main():
    console.clear()
    animate_ascii(ascii_art)
    loading_animation()

    commands = COMMANDS
    if not commands:
        console.print("[red]No command scripts found.[/red]")
        return

    choice = inquirer.select(
        message="Select a command to run:",
        choices=list(commands.keys()) + ["Exit"],
        default=None,
    ).execute()

    if choice == "Exit":
        console.print("[bold yellow]Goodbye! 👋[/bold yellow]")
        return
    
    module_name = f"cli_tool.commands.{commands[choice]}"
    mod = importlib.import_module(module_name, package=__package__)

    try:
        mod = importlib.import_module(module_name)
        if hasattr(mod, "main"):
            mod.main()
        else:
            console.print(f"[yellow]{choice}.py does not have a main() function.[/yellow]")
    except Exception as e:
        console.print(f"[red]Error running {choice}: {e}[/red]")

if __name__ == "__main__":
    main()
