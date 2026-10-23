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
    tracker.add_expense(Expense("2026-10-20", "Food", 150.0))
    tracker.add_expense(Expense("2026-10-21", "Transport", 80.0))
    tracker.add_expense(Expense("2026-10-22", "Food", 200.0))

    print("=== ALL EXPENSES ===")
    tracker.list_expenses()

    print(f"\nTotal: Rs.{tracker.total():.2f}")

    print("\n=== BY CATEGORY ===")
    for cat, amt in tracker.total_by_category().items():
        print(f"{cat:<12} Rs.{amt:.2f}")


if __name__ == "__main__":
    main()

