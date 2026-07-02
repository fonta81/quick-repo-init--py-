# Base Project Initializer

`Base.py` is a lightweight Python script designed to automate the initial setup of a project directory. It provides an interactive command-line interface to create a folder, initialize a specific file with a custom extension, generate a blank `Readme.md` file, and automatically initialize a Local Git repository within that directory.

## Features

- **Folder Creation:** Automatically creates a target directory (handling exceptions if it already exists).
- **Custom File Generation:** Prompts the user for a custom filename and extension (e.g., `.py`, `.js`, `.sh`, `.html`) and generates a blank file inside the new folder.
- **Automated README Creation:** Generates an empty `Readme.md` file within the created folder.
- **Git Repository Initialization:** Runs `git init` behind the scenes using the `subprocess` module to turn the folder into a Git repository.
- **Interactive Menu:** Simple execution loops with an intuitive "Start / Exit" menu.

## Prerequisites

- **Python 3.x** installed on your system.
- **Git** installed and available in your system's PATH (required for the automated repository initialization).

## Usage

1. Clone or copy `Base.py` into your working workspace.
2. Open a terminal or command prompt in that location.
3. Run the script using Python:

```bash
python Base.py
