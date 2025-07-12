"""
Module for managing the monthly budget and budget checks.
"""
from typing import List, Dict, Any

def check_monthly_budget(expenses: List[Dict[str, Any]], budget: float, month: str) -> Dict[str, Any]:
    """
    Check if the total expenses for a given month exceed the budget.

    Args:
        expenses (List[Dict]): List of expense records.
        budget (float): Monthly budget limit.
        month (str): Month to check in 'YYYY-MM' format.

    Returns:
        Dict[str, Any]:
            - 'exceeded' (bool): True if budget is exceeded, False otherwise.
            - 'total' (float): Total expenses for the month.
            - 'difference' (float): Amount over (+) or under (-) the budget.
    """
    total = sum(exp["amount"] for exp in expenses if exp["date"].startswith(month))
    exceeded = total > budget
    difference = total - budget
    return {
        "exceeded": exceeded,
        "total": total,
        "difference": difference
    } 