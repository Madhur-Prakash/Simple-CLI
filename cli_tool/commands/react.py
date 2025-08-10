import os
from rich.console import Console

console = Console()

def react_app():
    os.system("npm create vite@latest . -- --template react")

def main():
    console.print("Welcome to the React app creation tool!")
    console.print("This script will help you create a new React app using Vite.")
    console.print("\n")

    try:
        react_app()
        console.print("\n")
        console.print("React app created successfully!")
        console.print("Installing dependencies... Please be patient.")
        console.print("This may take a while depending on your internet connection.")
        os.system("npm install")
        console.print("Dependencies installed successfully!")

        
    except Exception as e:
        console.print(f"[red]An error occurred: {e}[/red]")
        console.print("[red]Please check your setup and try again.[/red]")
    
    finally:
        console.print("\n")
        console.print("[bold yellow]Exiting...[/bold yellow]")
        console.print("[bold yellow]Happy coding![/bold yellow]")
    
if __name__ == "__main__":
    main()