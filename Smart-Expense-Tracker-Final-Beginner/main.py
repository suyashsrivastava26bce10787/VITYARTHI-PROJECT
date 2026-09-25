from expense import add_expense, show_expenses, delete_expense
from analysis import total_expense, highest_expense, category_expense
from budget import set_budget, budget_status

expenses = []
budget = 0

while True:
    print()
    print("================================")
    print("       SMART EXPENSE TRACKER")
    print("================================")
    print("1. Add Expense")
    print("2. Show Expenses")
    print("3. Delete Expense")
    print("4. Total Expense")
    print("5. Highest Expense")
    print("6. Category Expense")
    print("7. Set Budget")
    print("8. Budget Status")
    print("9. Exit")
    print("================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense(expenses)
    elif choice == "2":
        show_expenses(expenses)
    elif choice == "3":
        delete_expense(expenses)
    elif choice == "4":
        total_expense(expenses)
    elif choice == "5":
        highest_expense(expenses)
    elif choice == "6":
        category_expense(expenses)
    elif choice == "7":
        budget = set_budget()
    elif choice == "8":
        budget_status(budget, expenses)
    elif choice == "9":
        print("Thank you for using Smart Expense Tracker.")
        break
    else:
        print("Invalid choice.")
