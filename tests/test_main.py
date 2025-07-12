"""
Smoke tests for the Personal Finance Tracker CLI (main.py).
"""
from typer.testing import CliRunner
from src.main import app

runner = CliRunner()

def test_analyze_help():
    result = runner.invoke(app, ["analyze", "--help"])
    assert result.exit_code == 0
    assert "Analyze expenses" in result.output

def test_plot_help():
    result = runner.invoke(app, ["plot", "--help"])
    assert result.exit_code == 0
    assert "Generate and save bar charts" in result.output

def test_budget_help():
    result = runner.invoke(app, ["budget", "--help"])
    assert result.exit_code == 0
    assert "Check if the monthly budget" in result.output 