def adding_expenses():
    expenseamount = input("Enter amount: ")
    expensecategory = input("Enter category: ")
    date = input("Enter date (YYYY-MM-DD): ")

    file = open("customer_expenses.csv", "a")
    file.write(expenseamount + "," + expensecategory + "," + date + "\n")
    file.close()

    print("Expense saved successfully!")
def show_expenses():
    try:
        file = open("customer_expenses.csv", "r")
        data = file.readlines()
        file.close()

        print("\n--- Displaying All Expenses ---")

        c = 0
        for l in data:
            parts = l.strip().split(",")

            amount = parts[0]
            category = parts[1]

            if len(parts) == 3:
                date = parts[2]
                print("Amount:", amount, "| Category:", category, "| Date:", date)
            else:
                print("Amount:", amount, "| Category:", category)

            c += 1

        print("\nTotal Records:", c)

    except:
        print("No expenses found!")
def view_summary():
    total = 0
    count = 0

    try:
        file = open("customer_expenses.csv", "r")
        for line in file:
            parts = line.strip().split(",")

            amount = float(parts[0])
            total += amount
            count += 1

        file.close()

        print("\n--- Expense Summary ---")
        print("Total Expense:", total)
        print("Total Records:", count)

    except:
        print("No data available!")
    
def category_summary():
    category_totals = {}

    try:
        file = open("customer_expenses.csv", "r")
        for line in file:
            parts = line.strip().split(",")

            amount = float(parts[0])
            category = parts[1]

            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount

        file.close()

        print("\n--- Category-wise Expenses ---")

        for cat in category_totals:
            print("Category:", cat, "| Total:", category_totals[cat])

        max_category = max(category_totals, key=category_totals.get)
        print("\nHighest spending category:", max_category)

    except:
        print("No data available!")
def main():
    print("Welcome to my smart Expense Tracker, Please select any one option from below")
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Summary")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            adding_expenses()
        elif choice == '2':
            show_expenses()
        elif choice == '3':
            view_summary()
        elif choice == '4':
            category_summary()
        elif choice=="5":
            print("Exiting...")
            break
        else:
            print("Invalid choice")
main()