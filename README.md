# Expense Tracker

A simple Python-based expense tracker that reads and manages expense records stored in a CSV file.

## Overview

This project helps you log, track, and review your personal or business expenses using a lightweight Python script and a CSV file as the data store — no database setup required.

## Features

- Add new expense entries
- View a summary of recorded expenses
- Store data persistently in `expenses.csv`
- Simple, dependency-light Python implementation

## Project Structure

```
expensetracker/
├── main.py          # Main application script
├── expenses.csv      # Stores expense records
└── .idea/            # IDE configuration (PyCharm)
```

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mrchandru51-debug/expensetracker.git
   cd expensetracker
   ```

2. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install any dependencies (if applicable):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script:

```bash
python main.py
```

Follow the on-screen prompts to add or view expenses. Data is saved to `expenses.csv`.

## Example CSV Format

| Date       | Category | Amount | Description       |
|------------|----------|--------|--------------------|
| 2026-08-01 | Food     | 250.00 | Groceries          |
| 2026-08-05 | Travel   | 500.00 | Bus fare           |

## Contributing

Contributions are welcome! Feel free to fork this repo, make changes, and submit a pull request.

## License

This project currently has no license specified. Add a `LICENSE` file if you'd like to define usage rights.
