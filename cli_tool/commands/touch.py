from rich.console import Console
from rich.prompt import Prompt

console = Console()

def make_new_file(*args):
    try:
        for file in args:
            with open(file, "w") as f:
                pass
    except Exception as e:
        console.print(f"[red]An error occurred while creating the file {file}: {e}[/red]")
        return False
        

def main():
    console.print("[blue]Please provide the names of the files to create:[/blue]")
    file_to_create = Prompt.ask("Enter file names (space-separated)").split()
    make_new_file(*file_to_create)

if __name__ == "__main__":
    main()
    