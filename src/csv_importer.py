"""
Module for importing and validating expense data from CSV files.
"""

import csv
from typing import List, Dict

REQUIRED_COLUMNS = ["date", "description", "category", "amount"]

class CSVImportError(Exception):
    """Custom exception for CSV import errors."""
    pass

def import_expenses_from_csv(file_path: str) -> List[Dict]:
    """
    Import expenses from a CSV file and validate required columns.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        List[Dict]: List of expense records as dictionaries.

    Raises:
        CSVImportError: If the file is missing or columns are invalid.
    """
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            if reader.fieldnames is None:
                raise CSVImportError("CSV file is empty or malformed.")
            missing = [col for col in REQUIRED_COLUMNS if col not in reader.fieldnames]
            if missing:
                raise CSVImportError(f"Missing required columns: {', '.join(missing)}")
            expenses = []
            for row in reader:
                # Basic validation: all required fields must be present and amount must be a number
                try:
                    expense = {
                        "date": row["date"].strip(),
                        "description": row["description"].strip(),
                        "category": row["category"].strip(),
                        "amount": float(row["amount"])
                    }
                except (KeyError, ValueError, AttributeError) as e:
                    raise CSVImportError(f"Invalid row: {row}. Error: {e}")
                expenses.append(expense)
            return expenses
    except FileNotFoundError:
        raise CSVImportError(f"File not found: {file_path}")
    except OSError as e:
        raise CSVImportError(f"Error reading file: {e}") 