# Expense Tracker 📊

A simple, beginner-friendly expense tracker built with Python.

## Features ✨

- ✅ **Add Expenses** - Record your spending with amount, category, and notes
- 📋 **View Expenses** - See all your recorded expenses with timestamps
- 💰 **Calculate Totals** - Get a quick summary of your total spending
- 🔒 **Safe Data Storage** - Uses CSV format with proper error handling
- ⏰ **Automatic Timestamps** - Each expense is timestamped automatically

## Requirements

- Python 3.6 or higher (comes pre-installed on most systems)
- No external packages needed! Uses only Python's built-in modules.

## How to Run

### Option 1: Windows (PowerShell)
```powershell
cd C:\Users\Administrator\Desktop\expense_tracker
python expense_tracker.py
```

### Option 2: Mac/Linux (Terminal)
```bash
cd ~/Desktop/expense_tracker
python3 expense_tracker.py
```

## How to Use

1. **Run the program** using the commands above
2. **Choose an option** from the menu (1-4):
   - **1** - Add a new expense
   - **2** - View all expenses
   - **3** - See total spending
   - **4** - Exit the program

### Example Workflow
```
--- Expense Tracker ---
1. Add Expense
2. View Expenses
3. Total Expense
4. Exit
Enter choice (1-4): 1
Enter amount: $25.50
Enter category (e.g., Food, Transport): Food
Enter note (optional): Lunch with friend
✅ Expense added successfully!
```

## Data Storage

- Your expenses are saved in `expenses.csv` (created automatically)
- Each entry includes: timestamp, amount, category, and notes
- The file is formatted as CSV, which you can open in Excel/Google Sheets if needed

## Sample Data

If you want to test with sample expenses, create a file `expenses.csv` with:
```csv
timestamp,amount,category,note
2026-02-08T10:30:00,25.50,Food,Lunch
2026-02-08T14:15:00,50.00,Transport,Taxi fare
2026-02-08T19:00:00,120.00,Groceries,Weekly shopping
```

## Tips for Beginners

- **Enter amounts** as numbers (e.g., `25.50`, `100`, `5`)
- **Press Enter** after each input
- **Notes are optional** - just press Enter to skip
- **View expenses** anytime to check your spending
- **The file auto-saves** - no "Save" button needed!

## Troubleshooting

**"Python not found" error?**
- Make sure Python is installed. Download from [python.org](https://www.python.org/)
- On Windows, check the "Add Python to PATH" option during installation

**Can't find the expenses file?**
- It's saved in the same folder as `expense_tracker.py`
- Look for a file named `expenses.csv`

## Next Steps (Optional)

- Add expense deletion feature
- Add expense categories filtering
- Export data to PDF
- Add monthly/weekly summaries

---

Happy tracking! 💚
