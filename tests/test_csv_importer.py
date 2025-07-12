"""
Tests for the csv_importer module.
"""

import os
import tempfile
import pytest
from src.csv_importer import import_expenses_from_csv, CSVImportError

def test_import_valid_csv():
    csv_content = """date,description,category,amount\n2024-06-01,Coffee,Food,2.50\n2024-06-01,Bus ticket,Transport,1.80\n"""
    with tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".csv") as tmp:
        tmp.write(csv_content)
        tmp.flush()
        result = import_expenses_from_csv(tmp.name)
    os.unlink(tmp.name)
    assert len(result) == 2
    assert result[0]["description"] == "Coffee"
    assert result[1]["amount"] == 1.80

def test_import_missing_column():
    csv_content = """date,description,amount\n2024-06-01,Coffee,2.50\n"""
    with tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".csv") as tmp:
        tmp.write(csv_content)
        tmp.flush()
        with pytest.raises(CSVImportError) as exc:
            import_expenses_from_csv(tmp.name)
    os.unlink(tmp.name)
    assert "Missing required columns" in str(exc.value)

def test_import_invalid_amount():
    csv_content = """date,description,category,amount\n2024-06-01,Coffee,Food,notanumber\n"""
    with tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".csv") as tmp:
        tmp.write(csv_content)
        tmp.flush()
        with pytest.raises(CSVImportError) as exc:
            import_expenses_from_csv(tmp.name)
    os.unlink(tmp.name)
    assert "Invalid row" in str(exc.value) 