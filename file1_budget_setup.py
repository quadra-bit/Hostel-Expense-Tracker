def get_budget():
    while True:
        try:
            budget = float(input("Enter your total monthly allowance: ₹"))
            if budget > 0:
                return budget
            print("Budget must be greater than zero.")
        except ValueError:
            print("Invalid input! Please enter a number.")