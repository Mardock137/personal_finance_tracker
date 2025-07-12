"""
Main entry point for the Personal Finance Tracker CLI application.
"""

import typer
from rich import print
from rich.panel import Panel
from rich.table import Table
from src.csv_importer import import_expenses_from_csv, CSVImportError
from src.analysis import analyze_expenses
from src.plotter import plot_expenses_by_category, plot_expenses_by_month
from src.budget import check_monthly_budget

app = typer.Typer(help="Personal Finance Tracker - Manage, analyze, and visualize your expenses easily.")

@app.command()
def analyze(csv_file: str = typer.Argument(..., help="Path to the expenses CSV file.")):
    """
    Analyze expenses and print statistics by category, by month, and overall total.
    """
    try:
        expenses = import_expenses_from_csv(csv_file)
    except CSVImportError as e:
        print(f"[bold red]Error importing CSV:[/bold red] {e}")
        raise typer.Exit(code=1)
    stats = analyze_expenses(expenses)
    table = Table(title="Expenses by Category")
    table.add_column("Category", style="cyan")
    table.add_column("Total", style="magenta")
    for cat, total in stats["by_category"].items():
        table.add_row(cat, f"€{total:.2f}")
    print(table)
    table2 = Table(title="Expenses by Month")
    table2.add_column("Month", style="green")
    table2.add_column("Total", style="magenta")
    for month, total in stats["by_month"].items():
        table2.add_row(month, f"€{total:.2f}")
    print(table2)
    print(Panel(f"[bold]Overall total spent:[/bold] €{stats['overall_total']:.2f}", style="bold blue"))

@app.command()
def plot(csv_file: str = typer.Argument(..., help="Path to the expenses CSV file.")):
    """
    Generate and save bar charts of expenses by category and by month (PNG files).
    """
    try:
        expenses = import_expenses_from_csv(csv_file)
    except CSVImportError as e:
        print(f"[bold red]Error importing CSV:[/bold red] {e}")
        raise typer.Exit(code=1)
    stats = analyze_expenses(expenses)
    plot_expenses_by_category(stats["by_category"])
    plot_expenses_by_month(stats["by_month"])
    print(Panel("[bold green]Charts saved as [italic]expenses_by_category.png[/italic] and [italic]expenses_by_month.png[/italic]![/bold green]", style="green"))

@app.command()
def budget(
    csv_file: str = typer.Argument(..., help="Path to the expenses CSV file."),
    budget: float = typer.Argument(..., help="Monthly budget amount."),
    month: str = typer.Argument(..., help="Month to check in YYYY-MM format (e.g. 2024-06)."),
):
    """
    Check if the monthly budget is exceeded and notify the user in the terminal.
    """
    try:
        expenses = import_expenses_from_csv(csv_file)
    except CSVImportError as e:
        print(f"[bold red]Error importing CSV:[/bold red] {e}")
        raise typer.Exit(code=1)
    result = check_monthly_budget(expenses, budget, month)
    if result["exceeded"]:
        print(Panel(f"⚠️  [bold red]Warning: You have exceeded your budget for {month}![/bold red]\n"
                    f"Total spent: [bold]{result['total']:.2f}[/bold] | Budget: [bold]{budget:.2f}[/bold] | Over budget: [bold red]{result['difference']:.2f}[/bold red]",
                    title="Budget Alert", style="red"))
    else:
        print(Panel(f"✅ [bold green]Good job! You are within your budget for {month}.[/bold green]\n"
                    f"Total spent: [bold]{result['total']:.2f}[/bold] | Budget: [bold]{budget:.2f}[/bold] | Remaining: [bold green]{-result['difference']:.2f}[/bold green]",
                    title="Budget Status", style="green"))

if __name__ == "__main__":
    app() 