import os
from InquirerPy import inquirer
from rich.console import Console
from rich.prompt import Prompt

console = Console()

def push_to_personal():
    try:
        os.system("git add .")
        console.print("[green]Added all changes to staging area.[/green]")
        commit_message = Prompt.ask("Enter commit message", default="update").strip()
        os.system(f'git commit -m "{commit_message}"')
        console.print("[green]Committed changes.[/green]")
        os.system("git push")
        console.print("[green]Pushed changes to personal repository.[/green]")

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
        os.system(f"git clone {repo_url}")
        console.print("[green]Cloned the repository successfully.[/green]")
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
        os.system("git init")
        os.system("git add .")
        console.print("[green]Added all changes to staging area.[/green]")
        commit_message = Prompt.ask("Enter commit message", default="initial commit").strip()
        os.system(f'git commit -m "{commit_message}"')
        console.print("[green]Committed changes.[/green]")
        remote_origin_link = Prompt.ask("Enter the remote origin link").strip()
        os.system(f'git remote add origin "{remote_origin_link}"')
        console.print("[green]Added remote origin.[/green]")
        os.system("git branch -M main")
        console.print("[green]Renamed branch to main.[/green]")
        os.system("git push -u origin main")
        console.print("[green]Pushed changes to main branch.[/green]")
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
    console.print("[yellow]Welcome to the GitHub Pull and Push Script[/yellow]")

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


