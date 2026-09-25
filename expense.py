def add_expense(expenses):
    print("\n--- Add Expense ---")
    amount = int(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")
    date = input("Enter date: ")

    expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    }

    expenses.append(expense)
    print("Expense added successfully.")


def show_expenses(expenses):
    print("\n--- All Expenses ---")

    if len(expenses) == 0:
        print("No expenses found.")
        return

    for i in range(len(expenses)):
        print("\nExpense", i + 1)
        print("Amount:", expenses[i]["amount"])
        print("Category:", expenses[i]["category"])
        print("Description:", expenses[i]["description"])
        print("Date:", expenses[i]["date"])


def delete_expense(expenses):
    if len(expenses) == 0:
        print("No expenses found.")
        return

    show_expenses(expenses)
    number = int(input("\nEnter expense number to delete: "))

    if number >= 1 and number <= len(expenses):
        expenses.pop(number - 1)
        print("Expense deleted successfully.")
    else:
        print("Invalid expense number.")
