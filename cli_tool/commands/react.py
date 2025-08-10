import os
from rich.console import Console

console = Console()

def react_app():
    os.system("npm create vite@latest . -- --template react")

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