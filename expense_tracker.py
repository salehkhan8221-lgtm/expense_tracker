import csv
from pathlib import Path
from datetime import datetime

DATA_FILE = Path(__file__).parent / "expenses.csv"


def show_menu():
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")


def get_valid_amount():
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount < 0:
                print("Amount cannot be negative.")
            else:
                return amount
        except ValueError:
            print("Please enter a valid number.")


def add_expense():
    amount = get_valid_amount()
    category = input("Enter category: ").strip()
    note = input("Enter note: ").strip()
    timestamp = datetime.now().isoformat(timespec="seconds")

    file_exists = DATA_FILE.exists()

    with open(DATA_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["timestamp", "amount", "category", "note"])
        writer.writerow([timestamp, amount, category, note])

    print("✅ Expense added successfully!")


def view_expenses():
    if not DATA_FILE.exists():
        print("No expenses found.")
        return

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            print("\n--- All Expenses ---")
            for i, row in enumerate(reader, start=1):
                print(
                    f"{i}. [{row['timestamp']}] "
                    f"₹{float(row['amount']):.2f} | "
                    f"{row['category']} | {row['note']}"
                )
    except Exception as e:
        print("Error reading file:", e)


def total_expense():
    if not DATA_FILE.exists():
        print("No expenses found.")
        return

    total = 0.0
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    total += float(row["amount"])
                except (KeyError, ValueError):
                    continue

        print(f"💰 Total Expense: ₹{total:.2f}")
    except Exception as e:
        print("Error calculating total:", e)


def main():
    while True:
        show_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            print("Exiting... Bye 👋")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
