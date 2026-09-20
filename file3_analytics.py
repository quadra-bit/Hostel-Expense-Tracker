def calculate_total(expenses):
    total = 0
    for item in expenses:
        total += item["amount"]
    return total

def show_balance(budget, expenses):
    total_spent = calculate_total(expenses)
    balance = budget - total_spent
    print(f"\nTotal Budget: ₹{budget}")
    print(f"Total Spent: ₹{total_spent}")
    print(f"Remaining Balance: ₹{balance}")
    return balance