```plaintext
   _____ _                 _                  _____ _      _____ 
  / ____(_)               | |                / ____| |    |_   _|
 | (___  _ _ __ ___  _ __ | | ___   ______  | |    | |      | |  
  \___ \| | '_ ` _ \| '_ \| |/ _ \ |______| | |    | |      | |  
  ____) | | | | | | | |_) | |  __/          | |____| |____ _| |_ 
 |_____/|_|_| |_| |_| .__/|_|\___|           \_____|______|_____|
                    | |                                          
                    |_|                                          
```
 **Automate Your Repetitive Tasks**

---

## Overview
Simple-CLI is a command line interface designed to simplify repetitive tasks such as setting up a Python project directory, creating a Vite app, and performing npm install. It also features a animations to make the experience more engaging.

---

## Features
- **Simplifies Repetitive Tasks**: Automates tasks such as setting up a Python project directory, creating a Vite app, and performing npm install.
- **GitHub Integration**: Supports GitHub commands to streamline your workflow.
- **Folder Structure Generation**: Generates a basic folder structure for your projects.
- **Animations**: Features animations to make the experience more engaging.

---

## Technology Stack
- **Programming Language**: Python
- **Package Manager**: pip
- **CLI Framework**: Custom implementation

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Madhur-Prakash/Simple-CLI.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Simple-CLI
   ```
3. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
4. Install the package:
   ```bash
   pip install .
   ```

> **Ubuntu / Debian:** skip steps 3–4 and use `uv tool install .` instead. Running `pip install .` outside a virtual environment fails there with `externally-managed-environment`. See [Installing on Ubuntu / Debian](#installing-on-ubuntu--debian).

### Installing on Ubuntu / Debian

On Ubuntu 23.04 and later (including 24.04 LTS), Debian 12 and later, and other Linux distributions that follow [PEP 668](https://peps.python.org/pep-0668/), installing outside a virtual environment fails:

```console
$ pip install .
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.
    ...
```

`uv pip install .` fails too, with `No virtual environment found`, and with `--system` it reports `The interpreter at /usr is externally managed`.

**Why it happens:** the distribution ships a marker file (for example `/usr/lib/python3.12/EXTERNALLY-MANAGED`) that declares the system Python as owned by `apt`. Ubuntu's own tools depend on the packages installed in that interpreter, so pip and uv refuse to install into it: a pip install could upgrade or replace a package those tools need. `sudo pip install .` fails the same way, because this is a policy check, not a permissions problem.

**The fix — install Simple-CLI as a uv tool** ([install uv](https://docs.astral.sh/uv/getting-started/installation/) first with `curl -LsSf https://astral.sh/uv/install.sh | sh` if you don't have it):

```bash
uv tool install .
```

This creates a private virtual environment for Simple-CLI in `~/.local/share/uv/tools/` and links the `simple` command into `~/.local/bin`. The command then works from any directory without activating anything, and the system Python is never touched.

If your shell reports `simple: command not found`, `~/.local/bin` is not on your `PATH` yet:

```bash
uv tool update-shell   # then open a new terminal
```

| Task | Command |
|------|---------|
| Pick up code changes (after `git pull` or local edits) | `uv tool install . --reinstall-package simple-cli` |
| Development install (edits take effect immediately) | `uv tool install --editable .` (run `uv tool uninstall simple-cli` first if you already installed it the regular way) |
| Uninstall | `uv tool uninstall simple-cli` |

**Alternatives:**

- **pipx** works the same way as `uv tool`:

  ```bash
  sudo apt install pipx
  pipx ensurepath   # then open a new terminal
  pipx install .
  ```

- **A virtual environment** (steps 3–4 above). On Ubuntu the command is `python3`, not `python`, and the `venv` module is a separate package, so if `python3 -m venv venv` fails with `ensurepip is not available`, run `sudo apt install python3-venv` first. `simple` is then only available while the environment is active.

> **Don't use `--break-system-packages`.** It switches off the safeguard, and this package's dependencies can then replace the apt-managed versions that system tools rely on.

---

## Usage

1. Run the CLI:
   ```bash
   simple
   ```
2. Follow the prompts to perform various tasks.

---

## Project Structure

```
SimpleCLI/
├── .gitignore  # gitignore file for GitHub
├── .python-version
├── LICENSE
├── README.md  # Project documentation
├── cli_tool
│   ├── __init__.py  # initializes package
│   ├── cli.py
│   └── commands
│       ├── __init__.py  # initializes package
│       ├── create.py
│       ├── github.py
│       ├── inst.py
│       ├── react.py
│       ├── structure.py
│       └── touch.py
├── pyproject.toml
├── requirements.txt
├── setup.py
└── uv.lock
```

---

## Future Enhancements
- Add support for more programming languages and frameworks.
- Implement more advanced animations and user interface features.
- Enhance the GitHub integration to support more commands and features.

---

## Contribution Guidelines

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and submit a pull request.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Author
**Madhur Prakash**  
[GitHub](https://github.com/Madhur-Prakash) | [Medium](https://medium.com/@madhurprakash2005)

---