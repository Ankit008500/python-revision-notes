FILE_PATH = "data/expenses.txt"


def add_expense():
    amount = input("Enter expense amount: ")
    category = input("Enter category: ")

    with open(FILE_PATH, "a") as file:
        file.write(f"{amount} - {category}\n")

    print("Expense added successfully!\n")


def view_expenses():
    try:
        with open(FILE_PATH, "r") as file:
            expenses = file.readlines()

            if not expenses:
                print("No expenses found.\n")
                return

            print("\nExpenses:")

            for expense in expenses:
                print(expense.strip())

            print()

    except FileNotFoundError:
        print("Expense file not found.\n")


def total_expenses():
    total = 0

    try:
        with open(FILE_PATH, "r") as file:
            expenses = file.readlines()

            for expense in expenses:
                amount = expense.split(" - ")[0]
                total += float(amount)

        print(f"\nTotal Expenses: ₹{total}\n")

    except FileNotFoundError:
        print("Expense file not found.\n")
