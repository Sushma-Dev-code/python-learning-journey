
import csv
import os

class ExpenseTracker:

    def __init__(self):
        self.expenses = []
        self.filename = "expenses.csv"
        self.load_expenses()

    def load_expenses(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r", newline="") as file:
                reader = csv.DictReader(file)
                self.expenses = list(reader)

    def add_expense(self):
        name = input("Enter expense name: ")
        category = input("Enter category: ")

        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("Amount must be positive.")
                return
        except ValueError:
            print("Please enter a valid amount.")
            return

        expense = {
            "name": name,
            "category": category,
            "amount": amount
        }

        self.expenses.append(expense)
        self.save_expenses()

        print("Expense added successfully!")

    def save_expenses(self):
        with open(self.filename, "w", newline="") as file:
            fields = ["name", "category", "amount"]
            writer = csv.DictWriter(file, fieldnames=fields)

            writer.writeheader()
            writer.writerows(self.expenses)

    def display_expenses(self):
        if not self.expenses:
            print("No expenses found.")
            return

        for expense in self.expenses:
            print(
                expense["name"],
                expense["category"],
                expense["amount"]
            )

    def calculate_total(self):
        total = sum(float(e["amount"]) for e in self.expenses)
        print("Total Expenses:", total)

    def highest_expense(self):
        if not self.expenses:
            print("No expenses available.")
            return

        highest = max(
            self.expenses,
            key=lambda e: float(e["amount"])
        )

        print("Highest Expense:", highest)

    def category_summary(self):
        summary = {}

        for expense in self.expenses:
            category = expense["category"]
            amount = float(expense["amount"])

            summary[category] = summary.get(category, 0) + amount

        for category, total in summary.items():
            print(category, ":", total)


def main():
    tracker = ExpenseTracker()

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. Display Expenses")
        print("3. Calculate Total")
        print("4. Highest Expense")
        print("5. Category Summary")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            tracker.add_expense()

        elif choice == "2":
            tracker.display_expenses()

        elif choice == "3":
            tracker.calculate_total()

        elif choice == "4":
            tracker.highest_expense()

        elif choice == "5":
            tracker.category_summary()

        elif choice == "6":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
