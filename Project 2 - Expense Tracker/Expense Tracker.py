# Project 2 - Expense Tracker

expenses = []
total = 0

def show_menu():
    print("\n----- EXPENSE TRACKER -----")
    print("1. Add an expense")
    print("2. View all expenses")
    print("3. View summary")
    print("4. Exit")

def get_valid_amount():
    entry = input("Enter expense amount: ")

    try:
        amount = int(entry)
    except ValueError:
        print("That's not a valid number.")
        return None

    if amount < 0:
        print("Expense cannot be negative.")
        return None

    if amount == 0:
        print("Expense cannot be zero.")
        return None

    return amount

def add_expense():
    global total

    amount = get_valid_amount()

    if amount is None:
        return

    label = input("What was this expense for? (optional): ").strip()

    if label == "":
        label = "Unlabeled"

    expense = {"amount": amount, "label": label}
    expenses.append(expense)

    total = total + amount

    print(f"Added '{label}' - {amount}. Current total: {total}")


def view_expenses():
    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return

    print("\nYour Expenses:")
    for index, expense in enumerate(expenses):
        print(f"{index + 1}. {expense['label']} - {expense['amount']}")

def calculate_average():
    if len(expenses) == 0:
        return 0

    return total / len(expenses)


def find_highest_expense():
    if len(expenses) == 0:
        return None

    highest = expenses[0]

    for expense in expenses:
        if expense["amount"] > highest["amount"]:
            highest = expense

    return highest


def find_lowest_expense():
    if len(expenses) == 0:
        return None

    lowest = expenses[0]

    for expense in expenses:
        if expense["amount"] < lowest["amount"]:
            lowest = expense

    return lowest


def show_summary():
    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return

    average = calculate_average()
    highest = find_highest_expense()
    lowest = find_lowest_expense()

    print("\n----- SUMMARY -----")
    print(f"Number of expenses: {len(expenses)}")
    print(f"Total spent: {total}")
    print(f"Average expense: {average:.2f}")
    print(f"Highest expense: {highest['label']} - {highest['amount']}")
    print(f"Lowest expense: {lowest['label']} - {lowest['amount']}")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_summary()
        elif choice == "4":
            print(f"\nFinal Total Spent: {total}")
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
