# Expense Tracker 📊

A simple, beginner-friendly expense tracker built with Python. Choose between a **CLI** (command-line) or **GUI** (graphical) interface!

## Features ✨

- ✅ **Add Expenses** - Record your spending with amount, category, and notes
- 📋 **View Expenses** - See all your recorded expenses with timestamps
- 💰 **Calculate Totals** - Get a quick summary of your total spending
- 🔒 **Safe Data Storage** - Uses CSV format with proper error handling
- ⏰ **Automatic Timestamps** - Each expense is timestamped automatically
- 🎨 **Two Interfaces** - Choose between CLI (command-line) or GUI (graphical window)
- 🗑️  **Delete & Manage** - Easily remove or clear expenses

## Requirements

- **Python 3.6 or higher** (comes pre-installed on most systems)
- **No external packages needed!** Uses only Python's built-in modules.

## How to Run

### 🖥️ GUI Version (Graphical Interface - Recommended for Beginners)

**Windows (PowerShell):**
```powershell
cd C:\Users\Administrator\Desktop\expense_tracker
python expense_tracker_gui.py
```

**Mac/Linux (Terminal):**
```bash
cd ~/Desktop/expense_tracker
python3 expense_tracker_gui.py
```

### 💻 CLI Version (Command-Line Interface)

**Windows (PowerShell):**
```powershell
cd C:\Users\Administrator\Desktop\expense_tracker
python expense_tracker.py
```

**Mac/Linux (Terminal):**
```bash
cd ~/Desktop/expense_tracker
python3 expense_tracker.py
```

## How to Use

### 🎨 GUI Version

1. **Run the program** using the command above
2. **The window opens** with a beautiful interface
3. **Add expenses** by filling in:
   - Amount (₹)
   - Category (dropdown menu)
   - Note (optional)
4. **Click "➕ Add Expense"** button
5. **View all expenses** in the list below
6. **Delete expenses** by selecting and clicking "🗑️ Delete Selected"
7. **See total** at the bottom of the window

**Features:**
- ✅ Automatic total calculation
- ✅ Delete individual expenses
- ✅ Clear all expenses at once
- ✅ Refresh list anytime
- ✅ Export data to CSV

### 💻 CLI Version

1. **Run the program** using the command above
2. **Choose an option** from the menu (1-4):
   - **1** - Add a new expense
   - **2** - View all expenses
   - **3** - See total spending
   - **4** - Exit the program

### Example Workflow (CLI)
```
--- Expense Tracker ---
1. Add Expense
2. View Expenses
3. Total Expense
4. Exit
Enter choice (1-4): 1
Enter amount: 25.50
Enter category: Food
Enter note: Lunch with friend
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

## 📁 Project Files

- **expense_tracker.py** - Command-line interface version
- **expense_tracker_gui.py** - Graphical interface version (recommended!)
- **test_tracker.py** - Automated tests for core functionality
- **expenses.csv** - Your expense data (auto-created)
- **README.md** - This file
- **GITHUB_SETUP.md** - Instructions for pushing to GitHub

## 🚀 Push to GitHub

Want to share your project? See [GITHUB_SETUP.md](GITHUB_SETUP.md) for step-by-step instructions!

---

Happy tracking! 💚
