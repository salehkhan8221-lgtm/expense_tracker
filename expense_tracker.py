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



def delete_expense():
    if not DATA_FILE.exists():
        print("No expenses to delete.")
        return

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        rows = list(csv.reader(f))

    header, data = rows[0], rows[1:]

    for i, row in enumerate(data, start=1):
        print(f"{i}. ₹{row[1]} | {row[2]} | {row[3]}")

    try:
        choice = int(input("Enter expense number to delete: "))
        deleted = data.pop(choice - 1)

        with open(DATA_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(data)

        print("Deleted:", deleted)
    except:
        print("Invalid choice")

def edit_expense():
    if not DATA_FILE.exists():
        print("No expenses to edit.")
        return

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        rows = list(csv.reader(f))

    header, data = rows[0], rows[1:]

    for i, row in enumerate(data, start=1):
        print(f"{i}. ₹{row[1]} | {row[2]} | {row[3]}")

    try:
        choice = int(input("Enter expense number to edit: "))
        expense = data[choice - 1]

        new_amount = input(f"New amount ({expense[1]}): ") or expense[1]
        new_category = input(f"New category ({expense[2]}): ") or expense[2]
        new_note = input(f"New note ({expense[3]}): ") or expense[3]

        expense[1] = new_amount
        expense[2] = new_category
        expense[3] = new_note

        with open(DATA_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(data)

        print("Expense updated!")
    except:
        print("Invalid choice")


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
            delete_expense()
        elif choice == "5":
            edit_expense()
        elif choice == "6":
            print("Exiting... Bye 👋")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
