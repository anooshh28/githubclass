
class Expense:
    def __init__(self, date, category, amount):
        self.date = date
        self.category = category
        self.amount = amount

    def display(self):
        print(f"{self.date} {self.category:<12} Rs.{self.amount:.2f}")


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
    print("Enter a date, then add expenses for that day.\n")

    while True:
        date = input("Enter date (YYYY-MM-DD): ")

        # add expenses for this one day
        while True:
            category = input("  Enter category: ")
            amount = float(input("  Enter amount: "))

            tracker.add_expense(Expense(date, category, amount))

            more = input("  Add another for this day? (y/n): ").lower()
            if more != "y":
                break

        next_day = input("Move to next day? (y/n): ").lower()
        if next_day != "y":
            break

    # --- per-day totals ---
    print("\n=== SPENDING PER DAY ===")
    daily = {}
    for e in tracker.expenses:
        daily[e.date] = daily.get(e.date, 0) + e.amount

    for date, amt in daily.items():
        print(f"{date}: Rs.{amt:.2f}")

    # --- overall total ---
    print(f"\nTotal spent: Rs.{tracker.total():.2f}")
    print(f"Over {len(daily)} day(s)")


if __name__ == "__main__":
    main()




       
   
    

