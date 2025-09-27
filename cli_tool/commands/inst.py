import os
from rich.console import Console

console = Console()

def install():
    try:
        console.print("[yellow]Installation started... Please be patient.[/yellow]")
        with open("requirements.txt", "w") as f:
            f.write("fastapi[standard]\n")
            f.write("motor\n")
            f.write("kafka-python\n")
            f.write("aioredis\n")
            f.write("concurrent_log_handler\n")
            f.close()
        os.system("pip install -r requirements.txt")
        console.print("[green]Installation completed successfully![/green]")
    except Exception as e:
        console.print(f"[red]An error occurred: {e}[/red]")
        console.print("[red]Please check your fastapi installation script and try again.[/red]")
    finally:
        console.print("[bold yellow]Exiting...[/bold yellow]")
        console.print("[bold yellow]Happy coding![/bold yellow]")
        exit(0)


def main():
    console.print("[bold yellow]Welcome to the FastAPI Installation Script![/bold yellow]")
    console.print("[bold yellow]This script will install FastAPI and some other basic dependencies.[/bold yellow]")
    install()



if __name__ == "__main__":
    main()

