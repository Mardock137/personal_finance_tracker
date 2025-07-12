"""
Tests for the plotter module.
"""
import os
import tempfile
from src.plotter import plot_expenses_by_category, plot_expenses_by_month

def test_plot_expenses_by_category_creates_file():
    data = {"Food": 30.5, "Transport": 11.8}
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
        output_path = tmp.name
    plot_expenses_by_category(data, output_path)
    assert os.path.exists(output_path)
    os.unlink(output_path)

def test_plot_expenses_by_month_creates_file():
    data = {"2024-06": 12.3, "2024-07": 30.0}
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
        output_path = tmp.name
    plot_expenses_by_month(data, output_path)
    assert os.path.exists(output_path)
    os.unlink(output_path) 