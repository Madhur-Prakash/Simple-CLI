import os
import subprocess
from rich.console import Console
from InquirerPy import inquirer

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


def start_auth_containers():
    try:
        console.print("Starting authentication... Please be patient.")
        run_cmd("docker start bc601", "Started mailhog container.")
        run_cmd("docker start b4683", "Started redis container.")
        run_cmd("docker start 77d33", "Started kafka container.")
        run_cmd("docker start 6e4e8", "Started zookeper container.")
        inp = inquirer.confirm("Do you want to start the containers for logging? (y/n): ").execute()
        if inp:
            run_cmd("docker start 9ffd9", "Started logging container.")
        else:
            console.print("Skipping logging container startup.")
        console.print("[yellow]All containers started successfully![/yellow]")
    except Exception as e:
        console.print(f"[red]An error occurred: {e}[/red]")
        console.print("[red]Please check your Docker setup and try again.[/red]")

    finally:
        console.print("[yellow]Exiting...[/yellow]")
        console.print("[yellow]Happy coding![/yellow]")
        exit(0)

def stop_auth_containers():
    try:
        console.print("[yellow]Stopping authentication... Please be patient.[/yellow]")
        run_cmd("docker stop bc601", "Stopped mailhog container.")
        run_cmd("docker stop b4683", "Stopped redis container.")
        run_cmd("docker stop 77d33", "Stopped kafka container.")
        run_cmd("docker stop 6e4e8", "Stopped zookeper container.")
        run_cmd("docker stop 9ffd9", "Stopped logging container.")
        console.print("[yellow]All containers stopped successfully![/yellow]")
    except Exception as e:
        console.print(f"[red]An error occurred: {e}[/red]")
        console.print("[red]Please check your Docker setup and try again.[/red]")

    finally:
        console.print("[yellow]Exiting...[/yellow]")
        console.print("[yellow]Happy coding![/yellow]")
        exit(0)

COMMANDS = {
    "start": start_auth_containers,
    "stop": stop_auth_containers
}

def main():
    commands = COMMANDS
    if not commands:
        console.print("[red]No command scripts found.[/red]")
        return
    console.print("Welcome to the Docker container startup script!")
    console.print("This script will help you start your Docker container.")

    choice = inquirer.select(
        message="Please select a command:",
        choices=list(commands.keys()) + ["Exit"],
        default=None,
    ).execute()
    if choice == "Exit":
        console.print("[bold yellow]Exiting...[/bold yellow]")
        return
    
    command_to_execute = commands.get(choice) 
    if command_to_execute:
        command_to_execute()
    else:
        console.print("[red]Invalid choice.[/red]")
        exit(1)
    
    


if __name__ == "__main__":
    main()