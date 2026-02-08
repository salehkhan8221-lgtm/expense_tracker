import csv
from pathlib import Path
from datetime import datetime
import matplotlib.pyplot as plt
from collections import defaultdict



DATA_FILE = Path(__file__).parent / "expenses.csv"


def show_menu():
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Delete Expense")
    print("5. Edit Expense")
    print("6. Monthly Summary")
    print("7. Exit")


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

def monthly_summary():
    if not DATA_FILE.exists():
        print("No expenses found.")
        return

    monthly_totals = defaultdict(float)

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                date = datetime.fromisoformat(row["timestamp"])
                month = date.strftime("%Y-%m")  # e.g. 2026-02
                amount = float(row["amount"])
                monthly_totals[month] += amount
            except:
                continue

    if not monthly_totals:
        print("No valid data found.")
        return

    print("\n--- Monthly Expense Report ---")
    for month, total in monthly_totals.items():
        print(f"{month} : ₹{total:.2f}")

    show_monthly_chart(monthly_totals)


def show_monthly_chart(data):
    months = list(data.keys())
    totals = list(data.values())

    # create figure with a friendly size
    fig, ax = plt.subplots(figsize=(10, 5))

    # use a qualitative colormap to get distinct colors per bar
    cmap = plt.get_cmap("tab20")
    colors = [cmap(i % cmap.N) for i in range(len(months))]

    bars = ax.bar(months, totals, color=colors)

    # labels and title
    ax.set_xlabel("Month")
    ax.set_ylabel("Total Expense (₹)")
    ax.set_title("Monthly Expense Summary")

    # rotate x labels for readability
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right")

    # add grid for easier comparison
    ax.yaxis.grid(True, linestyle="--", alpha=0.5)

    # annotate bars with values
    for bar, value in zip(bars, totals):
        height = bar.get_height()
        ax.annotate(f"₹{height:.2f}",
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 4),
                    textcoords="offset points",
                    ha="center",
                    va="bottom",
                    fontsize=8)

    plt.tight_layout()

    # attempt to save a copy next to the data file for quick preview
    try:
        out_path = DATA_FILE.parent / "monthly_summary.png"
        fig.savefig(out_path, dpi=150)
        print(f"Saved chart to: {out_path}")
    except Exception:
        pass

    plt.show()


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
            monthly_summary()
        elif choice == "7":
            print("Exiting... Bye 👋")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
