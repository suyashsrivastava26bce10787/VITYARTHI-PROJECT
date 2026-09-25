def total_expense(expenses):
    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("\nTotal Expense:", total)


def highest_expense(expenses):
    if len(expenses) == 0:
        print("No expenses found.")
        return

    highest = expenses[0]

    for expense in expenses:
        if expense["amount"] > highest["amount"]:
            highest = expense

    print("\n--- Highest Expense ---")
    print("Amount:", highest["amount"])
    print("Category:", highest["category"])
    print("Description:", highest["description"])


def category_expense(expenses):
    if len(expenses) == 0:
        print("No expenses found.")
        return

    category = input("Enter category: ")
    total = 0

    for expense in expenses:
        if expense["category"].lower() == category.lower():
            total = total + expense["amount"]

    print("Total spent on", category, ":", total)
