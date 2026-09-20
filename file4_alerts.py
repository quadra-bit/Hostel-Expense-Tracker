from file3_analytics import calculate_total


def check_warnings(budget, expenses):
    total_spent = calculate_total(expenses)
    balance = budget - total_spent

    if balance < 0:
        print("WARNING: You are completely out of money!")
    elif balance < (budget * 0.20):
        print("ALERT: You have less than 20% of your budget remaining. Spend carefully!")