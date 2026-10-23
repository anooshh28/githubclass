class Expense:
    def __init__(self, date, category, amount):
        self.date = date
        self.category = category
        self.amount = amount

    def display(self):
        print(f"{self.date}  {self.category:<12} Rs.{self.amount:.2f}")


class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def list_expenses(self):
        for e in self.expenses:
            e.display()

    def total(self):
        return sum(e.amount for e in self.expenses)

    def total_by_category(self):
        totals = {}
        for e in self.expenses:
            totals[e.category] = totals.get(e.category, 0) + e.amount
        return totals
def main():
    tracker = ExpenseTracker()

    print("=== EXPENSE TRACKER ===")
    print("Categories:", ", ".join(ExpenseTracker.CATEGORIES))

    while True:
        date = input("\nEnter date (YYYY-MM-DD): ")
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))

        tracker.add_expense(Expense(date, category, amount))

        again = input("Add another expense? (y/n): ").lower()
        if again != "y":
            break

    # --- all expenses ---
    print("\n=== ALL EXPENSES ===")
    tracker.list_expenses()

    # --- total ---
    print(f"\nTotal: Rs.{tracker.total():.2f}")

    # --- category-wise totals ---
    print("\n=== TOTAL BY CATEGORY ===")
    for cat, amt in tracker.total_by_category().items():
        print(f"{cat:<12} Rs.{amt:.2f}")


if __name__ == "__main__":
    main()



