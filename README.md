# weeek3-

# Daily Blocker Logger

A simple command-line application that allows users to record their **daily blockers** and persist them in a text file.

## Features

- Add a new daily blocker (appends to the file without overwriting)
- View all saved blockers
- File persistence using Python `with open()` in append mode (`'a'`)
- Error handling (checks if the file exists before reading)
- User-friendly menu interface

## How to Run

1. Open your terminal and navigate to the project folder:
   ```bash
   cd path/to/week3_project

Run the script:Bashpython persistence_log.py

Usage

Choose 1 → Enter your daily blocker
Choose 2 → View all previously saved blockers
Choose 3 → Exit the program

Technologies Used

Python 3
File I/O (open() with 'a' and 'r' modes)
os module for path handling
Basic error handling with conditionals


