#!/usr/bin/env python3
"""
Expense Tracker GUI - A beginner-friendly graphical interface
Built with tkinter (no external dependencies needed)
"""

import tkinter as tk
from tkinter import ttk, messagebox
import csv
from pathlib import Path
from datetime import datetime

# File path for storing expenses
DATA_FILE = Path(__file__).parent / "expenses.csv"


class ExpenseTrackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("💰 Expense Tracker")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # Configure style
        self.root.configure(bg="#f0f0f0")
        style = ttk.Style()
        style.theme_use("clam")
        
        # Create main frame
        self.create_widgets()
        self.load_expenses()
    
    def create_widgets(self):
        """Create all GUI elements."""
        # Header
        header_frame = tk.Frame(self.root, bg="#2c3e50", height=80)
        header_frame.pack(fill=tk.X)
        
        header_label = tk.Label(
            header_frame,
            text="💰 Expense Tracker",
            font=("Arial", 24, "bold"),
            bg="#2c3e50",
            fg="white"
        )
        header_label.pack(pady=15)
        
        # Month Selection Frame
        month_frame = ttk.LabelFrame(self.root, text="Select Month to View", padding=10)
        month_frame.pack(fill=tk.X, padx=15, pady=5)
        
        ttk.Label(month_frame, text="Month:").grid(row=0, column=0, sticky=tk.W, padx=5)
        self.month_var = tk.StringVar()
        month_combo = ttk.Combobox(
            month_frame,
            textvariable=self.month_var,
            values=["All Months", "January", "February", "March", "April", "May", "June",
                   "July", "August", "September", "October", "November", "December"],
            state="readonly",
            width=15
        )
        month_combo.set("All Months")
        month_combo.grid(row=0, column=1, sticky=tk.W, padx=5)
        month_combo.bind("<<ComboboxSelected>>", lambda e: self.load_expenses())
        
        ttk.Label(month_frame, text="Year:").grid(row=0, column=2, sticky=tk.W, padx=5)
        self.year_var = tk.StringVar()
        year_combo = ttk.Combobox(
            month_frame,
            textvariable=self.year_var,
            values=list(map(str, range(2024, 2031))),
            state="readonly",
            width=10
        )
        year_combo.set(str(datetime.now().year))
        year_combo.grid(row=0, column=3, sticky=tk.W, padx=5)
        year_combo.bind("<<ComboboxSelected>>", lambda e: self.load_expenses())
        
        # Input Section
        input_frame = ttk.LabelFrame(self.root, text="Add New Expense", padding=20)
        input_frame.pack(fill=tk.X, padx=15, pady=10)
        
        # Date Selection
        ttk.Label(input_frame, text="Date (YYYY-MM-DD):").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.date_var = tk.StringVar()
        self.date_var.set(datetime.now().strftime("%Y-%m-%d"))
        date_entry = ttk.Entry(input_frame, textvariable=self.date_var, width=15)
        date_entry.grid(row=0, column=1, sticky=tk.W, padx=10, pady=5)
        
        # Amount
        ttk.Label(input_frame, text="Amount (₹):").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.amount_var = tk.StringVar()
        amount_entry = ttk.Entry(input_frame, textvariable=self.amount_var, width=15)
        amount_entry.grid(row=1, column=1, sticky=tk.W, padx=10, pady=5)
        
        # Category
        ttk.Label(input_frame, text="Category:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.category_var = tk.StringVar()
        category_combo = ttk.Combobox(
            input_frame,
            textvariable=self.category_var,
            values=["Food", "Transport", "Groceries", "Entertainment", "Utilities", "Healthcare", "Other"],
            width=13
        )
        category_combo.grid(row=2, column=1, sticky=tk.W, padx=10, pady=5)
        
        # Note
        ttk.Label(input_frame, text="Note (optional):").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.note_var = tk.StringVar()
        note_entry = ttk.Entry(input_frame, textvariable=self.note_var, width=30)
        note_entry.grid(row=3, column=1, columnspan=2, sticky=tk.EW, padx=10, pady=5)
        
        # Add Button
        add_button = ttk.Button(input_frame, text="➕ Add Expense", command=self.add_expense)
        add_button.grid(row=4, column=0, columnspan=2, sticky=tk.EW, pady=15)
        
        # Expenses List Section
        list_frame = ttk.LabelFrame(self.root, text="Your Expenses", padding=10)
        list_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)
        
        # Treeview with scrollbar
        scrollbar = ttk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        columns = ("Date", "Amount", "Category", "Note")
        self.tree = ttk.Treeview(
            list_frame,
            columns=columns,
            height=12,
            yscrollcommand=scrollbar.set
        )
        scrollbar.config(command=self.tree.yview)
        
        # Define column headings
        self.tree.column("#0", width=0, stretch=tk.NO)
        self.tree.column("Date", anchor=tk.W, width=150)
        self.tree.column("Amount", anchor=tk.CENTER, width=100)
        self.tree.column("Category", anchor=tk.W, width=100)
        self.tree.column("Note", anchor=tk.W, width=200)
        
        self.tree.heading("#0", text="", anchor=tk.W)
        self.tree.heading("Date", text="📅 Date", anchor=tk.W)
        self.tree.heading("Amount", text="💵 Amount", anchor=tk.CENTER)
        self.tree.heading("Category", text="📂 Category", anchor=tk.W)
        self.tree.heading("Note", text="📝 Note", anchor=tk.W)
        
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        # Delete button for selected expense
        delete_button = ttk.Button(list_frame, text="🗑️  Delete Selected", command=self.delete_expense)
        delete_button.pack(pady=10)
        
        # Summary Section
        summary_frame = tk.Frame(self.root, bg="#ecf0f1")
        summary_frame.pack(fill=tk.X, padx=15, pady=10)
        
        self.summary_label = ttk.Label(summary_frame, text="Total (All Months):", font=("Arial", 12, "bold"))
        self.summary_label.pack(side=tk.LEFT, padx=10)
        self.total_label = ttk.Label(summary_frame, text="₹0.00", font=("Arial", 12, "bold"), foreground="green")
        self.total_label.pack(side=tk.LEFT, padx=5)
        
        # Buttons Frame
        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(fill=tk.X, padx=15, pady=10)
        
        refresh_button = ttk.Button(button_frame, text="🔄 Refresh", command=self.load_expenses)
        refresh_button.pack(side=tk.LEFT, padx=5)
        
        export_button = ttk.Button(button_frame, text="💾 Export to CSV", command=self.export_data)
        export_button.pack(side=tk.LEFT, padx=5)
        
        clear_button = ttk.Button(button_frame, text="🗑️  Clear All", command=self.clear_all)
        clear_button.pack(side=tk.LEFT, padx=5)
    
    def add_expense(self):
        """Add a new expense."""
        try:
            date_str = self.date_var.get().strip()
            amount_str = self.amount_var.get().strip()
            category = self.category_var.get().strip()
            note = self.note_var.get().strip()
            
            # Validation - Date
            try:
                datetime.strptime(date_str, "%Y-%m-%d")
            except ValueError:
                messagebox.showerror("Error", "❌ Invalid date format. Use YYYY-MM-DD (e.g., 2026-02-09)")
                return
            
            # Validation - Amount
            if not amount_str:
                messagebox.showerror("Error", "❌ Please enter an amount.")
                return
            
            try:
                amount = float(amount_str)
                if amount < 0:
                    messagebox.showerror("Error", "❌ Amount cannot be negative.")
                    return
            except ValueError:
                messagebox.showerror("Error", "❌ Please enter a valid number.")
                return
            
            if not category:
                messagebox.showerror("Error", "❌ Please select a category.")
                return
            
            # Format timestamp with date
            timestamp = f"{date_str} {datetime.now().strftime('%H:%M')}"
            
            # Write to CSV
            file_exists = DATA_FILE.exists()
            with open(DATA_FILE, "a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                if not file_exists:
                    writer.writerow(["timestamp", "amount", "category", "note"])
                writer.writerow([timestamp, amount, category, note])
            
            # Clear inputs
            self.amount_var.set("")
            self.category_var.set("")
            self.note_var.set("")
            self.date_var.set(datetime.now().strftime("%Y-%m-%d"))
            
            messagebox.showinfo("Success", "✅ Expense added successfully!")
            self.load_expenses()
        
        except Exception as e:
            messagebox.showerror("Error", f"❌ Error: {e}")
    
    def load_expenses(self):
        """Load and display expenses filtered by selected month."""
        # Clear tree
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        if not DATA_FILE.exists():
            self.total_label.config(text="₹0.00")
            return
        
        # Get selected month and year
        selected_month = self.month_var.get()
        selected_year = self.year_var.get()
        
        # Month mapping
        months = {
            "January": "01", "February": "02", "March": "03", "April": "04",
            "May": "05", "June": "06", "July": "07", "August": "08",
            "September": "09", "October": "10", "November": "11", "December": "12"
        }
        
        total = 0.0
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        timestamp = row.get("timestamp", "")
                        amount = float(row.get("amount", 0))
                        category = row.get("category", "")
                        note = row.get("note", "")
                        
                        # Filter by month and year
                        if selected_month != "All Months":
                            month_num = months[selected_month]
                            if not timestamp.startswith(f"{selected_year}-{month_num}"):
                                continue
                        elif selected_year and not timestamp.startswith(selected_year):
                            continue
                        
                        total += amount
                        self.tree.insert("", tk.END, values=(timestamp, f"₹{amount:.2f}", category, note))
                    except (ValueError, KeyError):
                        continue
            
            # Update summary with month/year info
            summary_text = f"Total ({selected_month if selected_month != 'All Months' else f'Year {selected_year}'}):"
            self.summary_label.config(text=summary_text)
            self.total_label.config(text=f"₹{total:.2f}")
        
        except Exception as e:
            messagebox.showerror("Error", f"❌ Error reading file: {e}")
    
    def delete_expense(self):
        """Delete selected expense."""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "⚠️  Please select an expense to delete.")
            return
        
        if messagebox.askyesno("Confirm", "Are you sure you want to delete this expense?"):
            try:
                # Get all data
                all_data = []
                with open(DATA_FILE, "r", encoding="utf-8") as file:
                    reader = csv.DictReader(file)
                    all_data = list(reader)
                
                # Get index of selected item
                selected_index = self.tree.index(selected[0])
                
                # Remove the selected expense
                del all_data[selected_index]
                
                # Write back to file
                with open(DATA_FILE, "w", newline="", encoding="utf-8") as file:
                    writer = csv.DictWriter(file, fieldnames=["timestamp", "amount", "category", "note"])
                    writer.writeheader()
                    writer.writerows(all_data)
                
                messagebox.showinfo("Success", "✅ Expense deleted!")
                self.load_expenses()
            
            except Exception as e:
                messagebox.showerror("Error", f"❌ Error: {e}")
    
    def clear_all(self):
        """Clear all expenses."""
        if messagebox.askyesno("Confirm", "⚠️  This will delete ALL expenses. Are you sure?"):
            try:
                if DATA_FILE.exists():
                    DATA_FILE.unlink()
                messagebox.showinfo("Success", "✅ All expenses cleared!")
                self.load_expenses()
            except Exception as e:
                messagebox.showerror("Error", f"❌ Error: {e}")
    
    def export_data(self):
        """Export current data (file already exists as CSV)."""
        try:
            if not DATA_FILE.exists():
                messagebox.showwarning("Warning", "⚠️  No expenses to export.")
                return
            
            messagebox.showinfo(
                "Info",
                f"✅ Your expenses are saved at:\n{DATA_FILE}\n\nYou can open this file in Excel or Google Sheets."
            )
        except Exception as e:
            messagebox.showerror("Error", f"❌ Error: {e}")


def main():
    root = tk.Tk()
    app = ExpenseTrackerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
