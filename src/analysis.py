"""
Module for analyzing and categorizing expenses.
"""
from typing import List, Dict, Any
from collections import defaultdict
from datetime import datetime

def analyze_expenses(expenses: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Analyze expenses and return totals by category, by month, and overall.

    Args:
        expenses (List[Dict]): List of expense records (as from import_expenses_from_csv).

    Returns:
        Dict[str, Any]: Dictionary with totals by category, by month, and overall total.
    """
    totals_by_category = defaultdict(float)
    totals_by_month = defaultdict(float)
    overall_total = 0.0

    for exp in expenses:
        # By category
        category = exp["category"]
        totals_by_category[category] += exp["amount"]
        # By month (YYYY-MM)
        try:
            month = datetime.strptime(exp["date"], "%Y-%m-%d").strftime("%Y-%m")
        except Exception:
            month = "unknown"
        totals_by_month[month] += exp["amount"]
        # Overall
        overall_total += exp["amount"]

    return {
        "by_category": dict(totals_by_category),
        "by_month": dict(totals_by_month),
        "overall_total": overall_total
    } 