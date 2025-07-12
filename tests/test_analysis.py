"""
Tests for the analysis module.
"""

from src.analysis import analyze_expenses

def test_analyze_expenses_basic():
    expenses = [
        {"date": "2024-06-01", "description": "Coffee", "category": "Food", "amount": 2.5},
        {"date": "2024-06-01", "description": "Bus ticket", "category": "Transport", "amount": 1.8},
        {"date": "2024-06-02", "description": "Lunch", "category": "Food", "amount": 8.0},
        {"date": "2024-07-01", "description": "Groceries", "category": "Food", "amount": 20.0},
        {"date": "2024-07-02", "description": "Taxi", "category": "Transport", "amount": 10.0},
    ]
    result = analyze_expenses(expenses)
    # Check overall total
    assert result["overall_total"] == 42.3
    # Check totals by category
    assert result["by_category"]["Food"] == 30.5
    assert result["by_category"]["Transport"] == 11.8
    # Check totals by month
    assert result["by_month"]["2024-06"] == 12.3
    assert result["by_month"]["2024-07"] == 30.0 