"""
Module for generating charts and visualizations of expenses.
"""
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict

sns.set_theme(style="whitegrid")

def plot_expenses_by_category(totals_by_category: Dict[str, float], output_path: str = "expenses_by_category.png"):
    """
    Plot a bar chart of expenses by category and save as PNG.
    Args:
        totals_by_category (Dict[str, float]): Totals per category.
        output_path (str): Path to save the PNG file.
    """
    categories = list(totals_by_category.keys())
    amounts = list(totals_by_category.values())
    plt.figure(figsize=(8, 5))
    ax = sns.barplot(x=categories, y=amounts, hue=categories, palette="pastel", legend=False)
    ax.set_title("Expenses by Category")
    ax.set_xlabel("Category")
    ax.set_ylabel("Total Amount")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

def plot_expenses_by_month(totals_by_month: Dict[str, float], output_path: str = "expenses_by_month.png"):
    """
    Plot a bar chart of expenses by month and save as PNG.
    Args:
        totals_by_month (Dict[str, float]): Totals per month (YYYY-MM).
        output_path (str): Path to save the PNG file.
    """
    months = list(totals_by_month.keys())
    amounts = list(totals_by_month.values())
    plt.figure(figsize=(8, 5))
    ax = sns.barplot(x=months, y=amounts, hue=months, palette="muted", legend=False)
    ax.set_title("Expenses by Month")
    ax.set_xlabel("Month")
    ax.set_ylabel("Total Amount")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close() 