# 🗓️ Month-Wise Expense Tracking Guide

## ✅ Fixed Issues & New Features

### Problems Fixed
1. ❌ **Invalid code at line 13** - Removed orphaned `self.date_entry` code
2. ❌ **Missing import dependency** - Removed unused `tkcalendar` requirement
3. ✅ **Now uses tkinter only** - No extra packages needed!

### New Features Added
- 📅 **Date Selection** - Choose the date for each expense
- 🗓️ **Month Filter** - View expenses by month
- 📆 **Year Filter** - View expenses by year
- 📊 **Dynamic Totals** - Shows total for selected month/year
- 📈 **Better Organization** - Keep expenses organized chronologically

---

## 🎯 How to Use Month-Wise Tracking

### Step 1: Launch the GUI
```powershell
python expense_tracker_gui.py
```

### Step 2: Add Expense with Date
1. **Date field** - Default is today's date (YYYY-MM-DD format)
   - Example: `2026-02-09` for February 9, 2026
   - You can change to past/future dates
2. **Amount** - Enter the expense amount (₹)
3. **Category** - Select from dropdown
4. **Note** - Optional description
5. **Click "➕ Add Expense"**

### Step 3: Filter by Month
1. **Select Month** dropdown - Choose specific month (or "All Months")
2. **Select Year** dropdown - Choose year (2024-2030)
3. **Table updates automatically** - Shows only expenses from that month/year
4. **Total updates** - Shows sum for selected month

---

## 📋 Example Workflow

### Add Multiple Expenses
```
Date: 2026-02-05, Amount: ₹500, Category: Food, Note: Groceries
Date: 2026-02-10, Amount: ₹200, Category: Transport, Note: Taxi
Date: 2026-02-15, Amount: ₹1000, Category: Utilities, Note: Electricity
Date: 2026-03-05, Amount: ₹300, Category: Food, Note: Restaurant
```

### View February 2026
1. Click Month dropdown → Select "February"
2. Year dropdown → Select "2026"
3. **Result**: Shows only Feb 5, 10, 15 expenses
4. **Total**: ₹1700 (for February only)

### View All Expenses
1. Click Month dropdown → Select "All Months"
2. **Result**: Shows all expenses from selected year
3. **Total**: ₹2000 (all months combined)

---

## 🎨 GUI Layout (Month-Wise Version)

```
╔════════════════════════════════════════════════╗
║         💰 Expense Tracker                     ║
╠════════════════════════════════════════════════╣
║ Select Month to View                           ║
║ Month: [All Months ▼]  Year: [2026 ▼]        ║
├────────────────────────────────────────────────┤
║ Add New Expense                                ║
║ Date:        [2026-02-09]                     ║
║ Amount (₹):  [___________]                    ║
║ Category:    [Food ▼]                         ║
║ Note:        [_________________________]       ║
║              [➕ Add Expense]                   ║
├────────────────────────────────────────────────┤
║ Your Expenses                                  ║
║ ┌─────────────────────────────────────────┐   ║
║ │ Date      │ Amount  │ Category │ Note  │   ║
║ ├───────────┼─────────┼──────────┼───────┤   ║
║ │ 2026-02-05│ ₹500.00 │ Food     │ Gro...│   ║
║ │ 2026-02-10│ ₹200.00 │ Transport│ Taxi  │   ║
║ │ 2026-02-15│ ₹1000.00│ Utilities│ Elec..│   ║
║ └─────────────────────────────────────────┘   ║
║              [🗑️ Delete Selected]              ║
├────────────────────────────────────────────────┤
║ Total (February 2026): ₹1700.00               ║
├────────────────────────────────────────────────┤
║ [🔄 Refresh] [💾 Export] [🗑️ Clear All]      ║
└════════════════════════════════════════════════┘
```

---

## 📊 Features Explained

### Date Field
- **Default**: Today's date (auto-filled)
- **Format**: YYYY-MM-DD (e.g., 2026-02-09)
- **Can change**: Add expenses from past or future
- **Example dates**:
  - `2026-02-09` = February 9, 2026
  - `2026-01-15` = January 15, 2026
  - `2026-03-20` = March 20, 2026

### Month Dropdown
- **"All Months"** - Shows all expenses from selected year
- **"January" to "December"** - Shows only that month's expenses
- **Updates automatically** - Table filters instantly

### Year Dropdown
- **Range**: 2024 to 2030 (editable if needed)
- **Works with month** - Filters by both month AND year
- **Default**: Current year (2026)

### Dynamic Total
- **Shows month name** - "Total (February 2026):"
- **Shows year only** - "Total (Year 2026):" when "All Months" selected
- **Real-time update** - Changes when you filter or add expense

---

## 🔄 Month-Wise Operations

### View Single Month
```
Month: February
Year: 2026
│
└─ Shows only expenses from Feb 1-29, 2026
   Total: Sum of February expenses
```

### View Entire Year
```
Month: All Months
Year: 2026
│
└─ Shows all expenses from Jan 1 - Dec 31, 2026
   Total: Sum of all 2026 expenses
```

### Compare Different Months
1. Set Month: January, Year: 2026 → Note total
2. Set Month: February, Year: 2026 → Compare totals
3. Set Month: March, Year: 2026 → Compare totals
4. Easily see which month you spent the most!

---

## 📈 Analytics You Can Do

### Monthly Spending Trend
Track spending across months:
```
January:   ₹2500
February:  ₹3200  (↑ 28% increase)
March:     ₹2800  (↓ 12% decrease)
```

### Category-Wise by Month
Filter and count by category:
```
February 2026:
- Food:       ₹800
- Transport:  ₹400
- Utilities:  ₹2000
```

### Year-over-Year Comparison
Compare same month different years:
```
February 2025: ₹2100
February 2026: ₹3200 (↑ 52% increase)
```

---

## 💾 Data Storage

### CSV Format
```
timestamp,amount,category,note
2026-02-05 10:30,500,Food,Groceries
2026-02-10 14:15,200,Transport,Taxi
2026-02-15 18:00,1000,Utilities,Electricity
2026-03-05 12:45,300,Food,Restaurant
```

**Benefits:**
- ✅ Can open in Excel/Google Sheets
- ✅ Easy to analyze in spreadsheets
- ✅ Backup by copying the CSV file
- ✅ Import into other tools

---

## ⚙️ Technical Details

### Date Validation
- Format must be: `YYYY-MM-DD`
- Will reject invalid dates like:
  - `02-02-2026` (wrong format)
  - `2026-13-01` (month > 12)
  - `2026-02-30` (invalid day)

### Filtering Logic
```python
# If month selected (e.g., February)
if timestamp starts with "2026-02"
    │
    └─ Include in display

# If "All Months" selected
if timestamp starts with "2026"
    │
    └─ Include in display
```

### Total Calculation
- Reads all CSV rows
- Filters by month/year
- Sums amounts of matching rows
- Displays with ₹ symbol and 2 decimals

---

## 🎯 Best Practices

1. **Use consistent dates** - Always use YYYY-MM-DD format
2. **Add notes** - Helps remember purchases later
3. **Monthly reviews** - Check each month's total
4. **Export monthly** - Backup by exporting to Excel
5. **Category consistency** - Use same category names
6. **Regular updates** - Add expense on same day if possible

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Date field empty | Click field and type date in YYYY-MM-DD format |
| Month filter doesn't work | Make sure dates in CSV match selected month |
| No expenses shown | Check month/year filters or add new expenses |
| Invalid date error | Use format YYYY-MM-DD only |
| Total shows ₹0 | Try "All Months" or check if expenses exist |

---

## ✨ Example: Managing Multiple Months

**Scenario**: Tracking 3 months of expenses

```
JANUARY 2026 (Month: January, Year: 2026)
├─ 2026-01-05: ₹1000 (Food)
├─ 2026-01-15: ₹500 (Transport)
└─ Total: ₹1500

FEBRUARY 2026 (Month: February, Year: 2026)
├─ 2026-02-05: ₹1200 (Food)
├─ 2026-02-10: ₹800 (Utilities)
└─ Total: ₹2000

MARCH 2026 (Month: March, Year: 2026)
├─ 2026-03-05: ₹900 (Food)
├─ 2026-03-20: ₹600 (Transport)
└─ Total: ₹1500

ALL MONTHS (Month: All Months, Year: 2026)
└─ Grand Total: ₹5000
```

---

## 🚀 Ready to Use!

Your month-wise expense tracker is now working perfectly!

```powershell
python expense_tracker_gui.py
```

**Features:**
✅ Add expenses with custom dates
✅ Filter by month and year
✅ View monthly totals
✅ Track spending trends
✅ No external dependencies

**Happy tracking! 💚**
