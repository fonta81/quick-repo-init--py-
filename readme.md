# Repository Generator (Base.py)

A simple interactive Python automation tool designed to streamline project initialization. This script helps you quickly set up a new project directory, generate boilerplate development files (Python or Bash), include a default markdown file, and automatically initialize a local Git repository—all through a clean terminal interface.

## Features

- **Automated Directory Creation**: Safely creates a target folder for your project without overwriting existing data (`exist_ok=True`).
- **Flexible File Boilerplates**: Easily generate empty boilerplate files for:
  - Python scripts (`.py`)
  - Shell/Bash scripts (`.sh`)
- **Built-in Documentation Setup**: Automatically creates a blank `Readme.md` file inside the target folder.
- **Git Initialization**: Uses Python's `subprocess` module to automatically execute `git init` directly inside the newly created project folder.
- **Interactive CLI**: Friendly command-line interface with a loops/menu system that guides you step-by-step.

## Prerequisites

- **Python**: Version 3.x or higher installed on your system.
- **Git**: Git must be installed and added to your system's environment variables (`PATH`) for the automated repository initialization to work.

## How to Run

1. Open your terminal or command prompt.
2. Navigate to the folder containing the `Base.py` file.
3. Run the script using the following command:

```bash
python Base.py
