def add_expense(expenses):
    try:
        buyed = input("What did you buy? (e.g., Food, Laundry): ")
        amount = float(input(f"How much did {buyed} cost? ₹"))
        expenses.append({"description": buyed, "amount": amount})
        print(f"Added: {buyed} for ₹{amount}")
    except ValueError:
        print("Invalid amount! Expense not added.")
    return expenses

def view_expenses(expenses):
    print("\n--- Your Expenses ---")
    if not expenses:
        print("No expenses recorded yet.")
    for item in expenses:
        print(f"- {item['description']}: ₹{item['amount']}")