# Elysium Station – Sci‑Fi Adventure Game

Author: Vrajkumar Patel  
Date: 12/2/2025

## Where the Code Is Hosted

This project is hosted on GitHub:

`https://github.com/vrajkumarpatel/Elysium_Adventure_Game.git`

## External Services

- No external APIs or services are used. The game runs entirely on Python’s standard library.

## Languages and Technologies

- Python 3.x
- Standard library modules only
- Modular file structure using multiple `.py` files
- Optional ANSI color output for banners and prompts
- ASCII art loaded from `assets/` for title and chapters

## System Requirements

- Python 3.8 or higher
- Windows, macOS, or Linux
- Terminal or IDE (VS Code, PyCharm, Thonny)
- If colors look odd, set `USE_COLOR = False` in `player.py`

## Coding & Naming Conventions

- `snake_case` for variables and functions
- `PascalCase` for class names
- One chapter per file
- Descriptive function names (e.g., `run_chapter1()`)
- All game logic starts from `main.py`

## How to Run

```bash
python main.py
```

The game starts immediately. Enter the number for each choice when prompted.

Visuals: ASCII art displays automatically; color output can be toggled in `player.py`.

## Architecture Overview

- `main.py`
  - Imports `Player` class (`player.py`)
  - Imports `chapter1`–`chapter5`
  - Creates the player object
  - Displays title ASCII art (`assets/title.txt`)
  - Runs chapters via a loop

- `player.py`
  - `Player` class with inventory, status, and flags
  - UI helpers: `banner`, `divider`, `show_hud`, `choose`, `clear_screen`
  - ANSI color helper (`USE_COLOR` toggle)
  - `print_art` loader for `assets/*.txt`

- `chapter1.py` – `chapter5.py`
  - Print the story for each chapter
  - Prompt player choices
  - Return the next chapter or ending
  - Show chapter ASCII art from `assets/`

## Start the Game

```bash
python main.py
```

Choose actions by entering the numeric options shown on screen.
