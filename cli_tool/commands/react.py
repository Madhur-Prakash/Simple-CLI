import os
import subprocess
from rich.console import Console

console = Console()

def run_cmd(command, success_msg):
    try:
        # Capture both stdout and stderr
        result = subprocess.run(
            command, 
            check=True, 
            shell=True, 
            text=True,
            capture_output=True
        )
        if result.stdout.strip():
            console.print(f"[cyan]{result.stdout.strip()}[/cyan]")  # Git messages
        console.print(f"[green]{success_msg}[/green]")
    except subprocess.CalledProcessError as e:
        # Show both stdout and stderr from Git
        if e.stdout and e.stdout.strip():
            console.print(f"[cyan]{e.stdout.strip()}[/cyan]")
        if e.stderr and e.stderr.strip():
            console.print(f"[red]{e.stderr.strip()}[/red]")
        console.print(f"[red]Command failed: {command}[/red]")
        exit(1)


def react_app():
    run_cmd("npm create vite@latest . -- --template react", "React app created successfully.")

def main():
    console.print("[yellow]Welcome to the React app creation tool![/yellow]")
    console.print("[yellow]This script will help you create a new React app using Vite.[/yellow]")

    try:
        react_app()
        console.print("\n")
        console.print("[green]React app created successfully![/green]")
        console.print("[yellow]Installing dependencies... Please be patient.[/yellow]")
        console.print("[yellow]This may take a while depending on your internet connection.[/yellow]")
        os.system("npm install")
        console.print("[green]Dependencies installed successfully![/green]")

        
    except Exception as e:
        console.print(f"[red]An error occurred: {e}[/red]")
        console.print("[red]Please check your setup and try again.[/red]")
    
    finally:
        console.print("\n")
        console.print("[bold yellow]Exiting...[/bold yellow]")
        console.print("[bold yellow]Happy coding![/bold yellow]")
    
if __name__ == "__main__":
    main()