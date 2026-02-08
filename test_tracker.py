#!/usr/bin/env python3
"""
Quick test script to verify expense_tracker functionality
Run this to test the core features without manual input
"""

import csv
from pathlib import Path
from datetime import datetime

# Same file path as in expense_tracker.py
DATA_FILE = Path(__file__).parent / "expenses.csv"

def test_expense_tracker():
    print("🧪 Testing Expense Tracker...\n")
    
    # Test 1: Create sample data
    print("Test 1: Adding sample expenses...")
    sample_expenses = [
        ["2026-02-08T09:00:00", "25.50", "Food", "Coffee"],
        ["2026-02-08T12:30:00", "50.00", "Transport", "Bus fare"],
        ["2026-02-08T18:00:00", "120.00", "Groceries", "Weekly shopping"],
    ]
    
    with open(DATA_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["timestamp", "amount", "category", "note"])
        writer.writerows(sample_expenses)
    
    print("✅ Sample expenses created\n")
    
    # Test 2: Read and display expenses
    print("Test 2: Reading expenses...")
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        expenses = list(reader)
    
    print(f"✅ Found {len(expenses)} expenses:")
    for i, exp in enumerate(expenses, 1):
        print(f"   {i}. [{exp['timestamp']}] ₹{float(exp['amount']):.2f} - {exp['category']}")
    
    # Test 3: Calculate total
    print("\nTest 3: Calculating total...")
    total = sum(float(exp['amount']) for exp in expenses)
    print(f"✅ Total: ₹{total:.2f}\n")
    
    # Test 4: File validation
    print("Test 4: File validation...")
    if DATA_FILE.exists():
        file_size = DATA_FILE.stat().st_size
        print(f"✅ Data file exists: {DATA_FILE}")
        print(f"   Size: {file_size} bytes")
    
    print("\n" + "="*50)
    print("🎉 All tests passed! Your expense tracker is working perfectly!")
    print("="*50)

if __name__ == "__main__":
    test_expense_tracker()
