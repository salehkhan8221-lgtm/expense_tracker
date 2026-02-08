# 🎨 GUI Launch Guide

## Easiest Way to Start (Copy & Paste)

### Windows PowerShell
```powershell
cd C:\Users\Administrator\Desktop\expense_tracker
python expense_tracker_gui.py
```

### Mac Terminal
```bash
cd ~/Desktop/expense_tracker
python3 expense_tracker_gui.py
```

### Linux Terminal
```bash
cd ~/Desktop/expense_tracker
python3 expense_tracker_gui.py
```

---

## What You'll See

After running the command, a window will appear:

```
╔══════════════════════════════════════════════════════════════╗
║                  💰 Expense Tracker                          ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  Add New Expense                                             ║
║  ┌────────────────────────────────────────────────────────┐ ║
║  │ Amount (₹): [_______________]                         │ ║
║  │ Category:   [Food ▼              ]                    │ ║
║  │ Note:       [_________________________________]        │ ║
║  │                     [➕ Add Expense]                     │ ║
║  └────────────────────────────────────────────────────────┘ ║
║                                                              ║
║  Your Expenses                                               ║
║  ┌────────────────────────────────────────────────────────┐ ║
║  │ 📅 Date         │ 💵 Amount │ 📂 Category │ 📝 Note  │ ║
║  ├─────────────────┼───────────┼─────────────┼──────────┤ ║
║  │ 2026-02-08 10:30│ ₹25.50   │ Food        │ Coffee  │ ║
║  │ 2026-02-08 12:30│ ₹50.00   │ Transport   │ Bus     │ ║
║  │ 2026-02-08 18:00│ ₹120.00  │ Groceries   │ Weekly  │ ║
║  └────────────────────────────────────────────────────────┘ ║
║                    [🗑️ Delete Selected]                      ║
║                                                              ║
║  Total Expense: ₹195.50                                      ║
║                                                              ║
║  [🔄 Refresh] [💾 Export to CSV] [🗑️ Clear All]             ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

---

## How to Use the GUI

### 1. **Add an Expense** ➕
   1. Enter the amount (e.g., `25.50`)
   2. Select category from dropdown
   3. Add optional note
   4. Click **"➕ Add Expense"**

### 2. **View Expenses** 📊
   - All expenses appear in the table below
   - Shows: Date, Amount, Category, and Notes
   - Total automatically updates at the bottom

### 3. **Delete an Expense** 🗑️
   1. Click on an expense in the table to select it
   2. Click **"🗑️ Delete Selected"**
   3. Confirm when asked

### 4. **Refresh the List** 🔄
   - Click **"🔄 Refresh"** to reload data from file

### 5. **Export Data** 💾
   - Click **"💾 Export to CSV"**
   - Your data is saved as `expenses.csv`
   - Open in Excel, Google Sheets, or any spreadsheet app

### 6. **Clear Everything** 🗑️
   - Click **"🗑️ Clear All"** to delete all expenses
   - Be careful! This cannot be undone without backing up first

---

## Troubleshooting GUI

### "Python not found" Error
```
'python' is not recognized as an internal or external command
```

**Solution:**
1. Download Python from https://www.python.org
2. During installation, check **"Add Python to PATH"**
3. Restart PowerShell
4. Try again

### GUI Window Doesn't Appear
- Make sure you're in the correct folder:
  ```powershell
  cd C:\Users\Administrator\Desktop\expense_tracker
  ```
- Try using `python3` instead of `python`:
  ```powershell
  python3 expense_tracker_gui.py
  ```

### "No module named tkinter"
Tkinter comes with Python, but on Linux you might need:
```bash
sudo apt-get install python3-tk
```

### CSV File Not Found
- The file is created automatically when you add the first expense
- Look in the same folder as `expense_tracker_gui.py`

---

## Features Explained

### 🎨 Clean Interface
- Modern design with emojis
- Easy to read and navigate
- No coding knowledge needed

### 💾 Data Persistence
- Automatically saves to `expenses.csv`
- Data survives after closing the app
- Can open in Excel

### ✅ Input Validation
- Warns if amount is invalid
- Prevents negative amounts
- Requires category selection

### 🗑️ Data Management
- Delete individual expenses
- Clear all at once
- Refresh to see latest data

### 📊 Automatic Totals
- Updates in real-time
- Shows formatted currency (₹)
- Includes all expenses

---

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `Tab` | Move to next field |
| `Shift + Tab` | Move to previous field |
| `Enter` | Add expense (when focused on button) |
| `Ctrl + C` | Close app (in terminal) |

---

## Tips for Best Experience

1. **Keep it organized**: Use consistent categories
2. **Add notes**: Help remember purchases
3. **Check totals regularly**: Monitor spending
4. **Export monthly**: Back up your data

---

## Next: Share on GitHub

Once you're happy with your project:

1. Create account: https://github.com
2. Follow: [GITHUB_SETUP.md](GITHUB_SETUP.md)
3. Share link with friends!

---

**Ready? Go ahead and run:**
```powershell
python expense_tracker_gui.py
```

**Happy tracking! 💚**
