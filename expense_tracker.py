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

