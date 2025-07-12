---
language: en
---

- **Python version used**: `3.12.10`

# 📋 Index
- [📄 Description](#-description)
- [ℹ️ General Info](#️-general-info)
- [⚙️ Configuration Info](#️-configuration-info)

## 📄 Description
Personal Finance Tracker

- Import your expenses from CSV files (bank statements, etc.)
- View basic charts and statistics about your spending habits
- Set a monthly budget and receive a warning if you exceed it

## ℹ️ General Info
- For the **list of dependencies** see [requirements.txt](requirements.txt)
- For the **repository structure** see [repo_structure.md](docs/repo_structure.md)

## ⚙️ Configuration Info
To use the app, run one of the following commands from the project root:

```bash
python -m src.main analyze expenses.csv
python -m src.main plot expenses.csv
python -m src.main budget expenses.csv 100.0 2025-06
```

## 📝 Example CSV file

```csv
date,description,category,amount
2024-06-01,Coffee,Food,2.50
2024-06-01,Bus ticket,Transport,1.80
2024-06-02,Lunch,Food,8.00
2024-07-01,Groceries,Food,20.00
2024-07-02,Taxi,Transport,10.00
```

## 💡 Example output

```text
Overall total spent: €42.30
Expenses by category:
Food: €30.50
Transport: €11.80
Expenses by month:
2024-06: €12.30
2024-07: €30.00
```
