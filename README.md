# Hostel Expense & Budget Tracker

## Overview of the Project
The Hostel Expense & Budget Tracker is a modular, console-based Python application designed to help university students track their monthly pocket money and prevent overspending. It acts as an interactive financial ledger that monitors budget health in real-time without requiring complex software.

## Features
* **Initial Budget Configuration:** Establish your starting allowance for the month.
* **Categorized Expense Logging:** Add daily expenses (CRUD capabilities) with custom descriptions and positive-value validation.
* **Running Ledger:** View a complete, running list of all recorded expenses in your active session.
* **Real-Time Analytics:** Instantly calculate total spending, subtract it from the budget, and output the exact remaining balance.
* **Automated Alerts:** Automatic alert triggers evaluate the balance after every transaction, issuing a console warning if funds drop below 20% or hit exactly ₹0.

## Technologies/Tools Used
* Python 3
* Core Concepts: Modular architecture (6 files), `while` loops, lists, dictionaries, and `try/except` error handling.
* Version Control: Git and GitHub

## Steps to Install & Run the Project
1. Clone this repository to your local machine:
   `git clone https://github.com/quadra-bit/Hostel-Expense-Tracker.git`
2. Open your terminal or command prompt and navigate to the project folder:
   `cd Hostel-Expense-Tracker`
3. Run the central router file to launch the application:
   `python file5_main.py`

## Instructions for Testing
* **Unit Testing:** Run the command `python file6_test_tracker.py` in your terminal to execute the built-in unit tests. This validates the core arithmetic and analytics modules in isolation without launching the main menu.
* **Manual Testing:** Launch the main program and deliberately log an expense that exceeds the budget to verify that the 20% low-balance and zero-balance alerts trigger accurately.

## Screenshots

### Screenshot 1:
<img width="367" height="193" alt="Screenshot 2026-09-30 145359" src="https://github.com/user-attachments/assets/5aea345f-c2ba-432e-afbd-d9994f317768" />

This image shows the main menu of the code and the starting prompt thats gets printed.

### Screenshot 2:
<img width="396" height="101" alt="image" src="https://github.com/user-attachments/assets/5612a0d4-fa14-4534-a8b1-0d3db5671168" />

This image shows the expense being added.

### Screenshot 3:
<img width="595" height="661" alt="image" src="https://github.com/user-attachments/assets/f3251451-2289-4dfa-a34a-9ae1c4e9667e" />

<img width="606" height="251" alt="image" src="https://github.com/user-attachments/assets/ce757d5d-b013-41eb-997b-9874724ba997" />

This image shows a 20% alert being displayed.

### Screenshot 4:
<img width="412" height="220" alt="image" src="https://github.com/user-attachments/assets/16028294-4a14-4f41-97bd-2f1b009dc1ec" />

<img width="347" height="246" alt="image" src="https://github.com/user-attachments/assets/40ab00cc-9550-420c-b526-72a63b09b6f5" />

This image shows "You are completely out of money!" being displayed.


