from rich.console import Console
from rich.prompt import Prompt

console = Console()

def new_script():
    try: 
        console.print("Creating a new script...Please be patient.")
        script_name = Prompt.ask("Enter the name of the new script: ").strip().lower()
        script_name = script_name.replace(" ", "_") 
        console.print(f"Created new script: {script_name}.py")

        with open(f"{script_name}.py", "w") as f:
            f.write("import os\n")
            f.write("\n")
            f.write("def func_name():\n")
            f.write("   pass\n")
            f.write("\n")

            f.write("def main():\n")
            f.write("   print(\"Welcome to the new script!\")\n")
            f.write("   print(\"This script will help ypu...\")\n")
            f.write("\n")

            f.write("   # continue with your script...\n")
            f.write("\n")
            f.write("if __name__ == \"__main__\":\n")
            f.write("   main()\n")
    
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please check your script creation and try again.")

    finally:
        print("\n")
        print("Exiting...")
        print("Happy coding!")
        exit(0)


def main():
    console.print("Welcome to the new script creation tool!")
    console.print("This script will help you create a new script with a template.")
    console.print("\n")
    new_script()
    

if __name__ == "__main__":
    main()