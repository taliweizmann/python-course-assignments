# Day 04 - Web Interface with Flask

## Objective
Convert the Day 03 command-line biological calculation (DNA Longest Common Substring Finder) into an interactive web application using Flask.

## Files
- `lcs_finder.py`: Preserved core calculation logic from Day 03.
- `sequences.txt`: Preserved sample input dataset.
- `app.py`: Flask application routing HTTP GET/POST requests and rendering output.
- `templates/index.html`: Responsive HTML/CSS user interface.
- `.gitignore`: Excludes Python bytecode and cache (`__pycache__`).

## How to Run Locally

1. **Install Flask:**
   ```bash
   pip install flask

## Running Automated Tests (Day 05)

Unit tests for the core business logic (`find_longest_common_substring` in `lcs_finder.py`) are located in `test_lcs.py`.

1. Install pytest:
   ```bash
   pip install pytest
2. run using pytest
