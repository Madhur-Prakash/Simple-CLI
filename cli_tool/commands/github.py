import os
import subprocess
from InquirerPy import inquirer
from rich.console import Console
from rich.prompt import Prompt

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


def push_to_personal():
    try:
        run_cmd("git add .", "Added all changes to staging area.")
        commit_message = Prompt.ask("Enter commit message", default="update").strip()
        run_cmd(f'git commit -m "{commit_message}"', "Committed changes.")
        run_cmd("git push", "Pushed changes to personal repository.")
    except Exception as e:
        console.print(f"[red]An error occurred: {e}[/red]")
        console.print("[red]Please check your Github and try again.[/red]")

    finally:
        console.print("[yellow]Exiting...[/yellow]")
        console.print("[yellow]Happy coding![/yellow]")
        exit(0)


def clone_repo():
    try:
        repo_url = Prompt.ask("Enter the repository URL").strip()
        run_cmd(f"git clone {repo_url}", "Cloned repository successfully.")
        repo_name = repo_url.split("/")[-1].replace(".git", "")
        console.print(f"[green]Repository name: {repo_name}[/green]")
        os.chdir(repo_name)
        console.print(f"[green]Changed directory to {repo_name}.[/green]")

        open_in_vscode = Prompt.ask("Do you want to open the repository in VS Code? (yes/no)", default="no").strip().lower()
        if open_in_vscode == "yes" or open_in_vscode == "y":
            os.system("code .")
            console.print("[green]Opened the repository in VS Code.[/green]")
        else:
            console.print("[yellow]Exiting...[/yellow]")
            console.print("[yellow]Happy coding![/yellow]")
            exit(0)

    except Exception as e:
        console.print(f"[red]An error occurred: {e}[/red]")
        console.print("[red]Please check your Github and try again.[/red]")

    finally:
        console.print("\n")
        console.print("[yellow]Exiting...[/yellow]")
        console.print("[yellow]Happy coding![/yellow]")
        exit(0)


def setup_new_repo():
    try:
        run_cmd("git init", "Initialized git repository.")
        run_cmd("git add .", "Added changes to staging area.")
        commit_message = Prompt.ask("Enter commit message", default="initial commit").strip()
        run_cmd(f'git commit -m "{commit_message}"', "Committed changes.")
        remote_origin_link = Prompt.ask("Enter the remote origin link").strip()
        run_cmd(f'git remote add origin "{remote_origin_link}"', "Added remote origin.")
        run_cmd("git branch -M main", "Renamed branch to main.")
        run_cmd("git push -u origin main", "Pushed changes to main branch.")
        console.print("[green]Repository setup successfully.[/green]")

    except Exception as e:
        console.print(f"[red]An error occurred: {e}[/red]")
        console.print("[red]Please check your Github and try again.[/red]")

    finally:
        console.print("[yellow]Exiting...[/yellow]")
        console.print("[yellow]Happy coding![/yellow]")
        exit(0)

COMMANDS = {
    "Push to Personal Repository": push_to_personal,
    "Clone Repository": clone_repo,
    "Setup New Repository": setup_new_repo,
}


def main():
    console.print("[yellow]Welcome to the GitHub Automation Script![/yellow]")

    commands = COMMANDS
    if not commands:
        console.print("[red]No command scripts found.[/red]")
        return


    choice = inquirer.select(
        message="Please select a command:",
        choices=list(commands.keys()) + ["Exit"],
        default=None
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


