def category_report(expenses):
    if len(expenses) == 0:
        print("No expenses available.")
        return

    categories = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    print("\n--- Spending by Category ---")

    for category in categories:
        print(category, ":", categories[category])


def average_expense(expenses):
    if len(expenses) == 0:
        print("No expenses available.")
        return

    total = 0

    for expense in expenses:
        total += expense["amount"]

    average = total / len(expenses)

    print("Average expense:", average)


def highest_category(expenses):
    if len(expenses) == 0:
        print("No expenses available.")
        return

    categories = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    highest = max(categories, key=categories.get)

    print("Highest spending category:", highest)
    print("Amount spent:", categories[highest])


def show_report(expenses):
    if len(expenses) == 0:
        print("No expenses available.")
        return

    print("\n--- Expense Report ---")

    print("Number of expenses:", len(expenses))

    category_report(expenses)
    average_expense(expenses)
    highest_category(expenses)

