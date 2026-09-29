def add_expense(expenses):
    try:
        item = input("What did you buy? (e.g., Food, Laundry): ")
        amount = float(input(f"How much did {item} cost? ₹"))
        if amount <= 0:
            print("Expense must be greater than zero.")
            return expenses
        expenses.append({"description": item, "amount": amount})
        print(f"Added: {item} for ₹{amount}")
    except ValueError:
        print("Invalid amount! Expense not added.")
    return expenses

def view_expenses(expenses):
    print("\n--- Your Expenses ---")
    if not expenses:
        print("No expenses recorded yet.")
    for item in expenses:
        print(f"- {item['description']}: ₹{item['amount']}")
