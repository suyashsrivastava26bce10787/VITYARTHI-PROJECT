def set_budget():
    amount = float(input("Enter your budget: "))

    if amount < 0:
        print("Budget cannot be negative.")
        return 0

    print("Budget set successfully.")
    return amount


def budget_status(budget, expenses):
    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("\n--- Budget Status ---")
    print("Budget:", budget)
    print("Total Spent:", total)
    print("Remaining:", budget - total)

    if total > budget:
        print("You have exceeded your budget.")
    else:
        print("You are within your budget.")
