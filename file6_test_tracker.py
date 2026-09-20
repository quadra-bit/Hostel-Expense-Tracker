from file3_analytics import calculate_total

def test_math():
    mock_expenses = [
        {"description": "Food", "amount": 100},
        {"description": "Auto", "amount": 50}
    ]
    total = calculate_total(mock_expenses)
    if total == 150:
        print("Unit Test Passed: Analytics math is working correctly!")
    else:
        print("Unit Test Failed: Math is broken!")

if __name__ == "__main__":
    test_math()