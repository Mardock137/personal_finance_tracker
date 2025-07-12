"""
Tests for the budget module.
"""
from src.budget import check_monthly_budget

def test_budget_exceeded():
    expenses = [
        {"date": "2024-06-01", "amount": 50.0},
        {"date": "2024-06-15", "amount": 60.0},
        {"date": "2024-07-01", "amount": 10.0},
    ]
    result = check_monthly_budget(expenses, budget=100.0, month="2024-06")
    assert result["exceeded"] is True
    assert result["total"] == 110.0
    assert result["difference"] == 10.0

def test_budget_not_exceeded():
    expenses = [
        {"date": "2024-06-01", "amount": 30.0},
        {"date": "2024-06-15", "amount": 40.0},
    ]
    result = check_monthly_budget(expenses, budget=100.0, month="2024-06")
    assert result["exceeded"] is False
    assert result["total"] == 70.0
    assert result["difference"] == -30.0

def test_budget_exact_match():
    expenses = [
        {"date": "2024-06-01", "amount": 50.0},
        {"date": "2024-06-15", "amount": 50.0},
    ]
    result = check_monthly_budget(expenses, budget=100.0, month="2024-06")
    assert result["exceeded"] is False
    assert result["total"] == 100.0
    assert result["difference"] == 0.0 