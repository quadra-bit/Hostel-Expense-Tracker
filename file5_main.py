from file1_budget_setup import get_budget
from file2_expense_manager import add_expense, view_expenses
from file3_analytics import show_balance
import file4_alerts


def main_menu():
    print("=== Hostel Expense Tracker ===")
    budget = get_budget()
    expenses = []

    while True:
        print("\nMenu:\n1. Add an Expense\n2. View All Expenses\n3. Check Balance\n4. Exit")
        choice = input("Select an option (1-4): ")

        if choice == '1':
            expenses = add_expense(expenses)
            file4_alerts.check_warnings(budget, expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            show_balance(budget, expenses)
            file4_alerts.check_warnings(budget, expenses)
        elif choice == '4':
            print("Exiting Tracker... Have a great month! and spend with caution.")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main_menu()
