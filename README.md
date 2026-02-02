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