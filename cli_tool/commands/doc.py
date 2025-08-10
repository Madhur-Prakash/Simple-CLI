import os
from rich.console import Console
from InquirerPy import inquirer

console = Console()

def start_auth_containers():
    try:
        console.print("Starting authentication... Please be patient.")
        os.system("docker start bc601") # -> for mailhog
        os.system("docker start b4683") # -> for redis
        os.system("docker start 77d33") # -> for kafka 
        os.system("docker start 6e4e8") # -> for zookeper

        inp = inquirer.confirm("Do you want to start the containers for logging? (y/n): ").execute()
        if inp:
            os.system("docker start 9ffd9") # -> for logging
        else:
            console.print("Skipping logging container startup.")
        console.print("[yellow]All containers started successfully![/yellow]")
    except Exception as e:
        console.print(f"[red]An error occurred: {e}[/red]")
        console.print("[red]Please check your Docker setup and try again.[/red]")

    finally:
        console.print("\n")
        console.print("Exiting...")
        console.print("Happy coding!")
        exit(0)

def stop_auth_containers():
    try:
        console.print("[yellow]Stopping authentication... Please be patient.[/yellow]")
        os.system("docker stop bc601") # -> for mailhog
        os.system("docker stop b4683") # -> for redis
        os.system("docker stop 77d33") # -> for kafka 
        os.system("docker stop 6e4e8") # -> for zookeper
        os.system("docker stop 9ffd9") # -> for logging
        print("All containers stopped successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please check your Docker setup and try again.")
    
    finally:
        print("\n")
        print("Exiting...")
        print("Happy coding!")
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