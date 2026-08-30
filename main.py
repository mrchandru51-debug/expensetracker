import csv
import os
from datetime import datetime

FILENAME = "expenses.csv"

def init_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["date", "category", "amount", "description"])

def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Category (e.g. food, rent, fun): ")
    amount = float(input("Amount: "))
    description = input("Description: ")

    with open(FILENAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount, description])
    print("Expense added!")

def view_summary():
    totals = {}
    with open(FILENAME, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cat = row["category"]
            amt = float(row["amount"])
            totals[cat] = totals.get(cat, 0) + amt

    print("\n--- Spending by Category ---")
    for cat, total in totals.items():
        print(f"{cat}: ${total:.2f}")
    print(f"Total: ${sum(totals.values()):.2f}")

def main():
    init_file()
    while True:
        print("\n1. Add expense\n2. View summary\n3. Exit")
        choice = input("Choose: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_summary()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()