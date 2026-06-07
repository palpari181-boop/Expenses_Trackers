import csv
import os

FILE_NAME = "expenses.csv"


if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount", "Description"])


def add_expense():
    date = input("Enter Date (DD-MM-YYYY): ")
    category = input("Enter Category: ")
    amount = float(input("Enter Amount: "))
    description = input("Enter Description: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

    print("✅ Expense Added Successfully!\n")


def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            print("\n----- Expense Records -----")
            for row in reader:
                print("{:<15} {:<15} {:<10} {}".format(*row))
            print()
    except FileNotFoundError:
        print("No expense records found.\n")


def total_expenses():
    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total += float(row["Amount"])

    print(f"\n💰 Total Expenses: ₹{total:.2f}\n")


def search_category():
    category = input("Enter Category to Search: ")

    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        print("\nMatching Expenses:")
        for row in reader:
            if row["Category"].lower() == category.lower():
                print(
                    f"{row['Date']} | {row['Category']} | ₹{row['Amount']} | {row['Description']}"
                )
                found = True

    if not found:
        print("No records found for this category.\n")


while True:
    print("====== EXPENSE TRACKER ======")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Search by Category")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expenses()

    elif choice == "4":
        search_category()

    elif choice == "5":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("❌ Invalid Choice. Try Again.\n")