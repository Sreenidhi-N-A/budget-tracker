import json
import os

def add_expense(expenses, description, amount):
    expenses.append({"description": description, "amount": amount})
    print(f"Added expense: {description}, Amount: {amount}")

def get_total_expenses(expenses):
    return sum(expense['amount'] for expense in expenses)

def get_balance(budget, expenses):
    return budget - get_total_expenses(expenses)

def show_budget_details(budget, expenses):
    print(f"Total Budget: {budget}")
    print("Expenses:")
    for expense in expenses:
        print(f"- {expense['description']}: {expense['amount']}")
    print(f"Total Spent: {get_total_expenses(expenses)}")
    print(f"Remaining Budget: {get_balance(budget, expenses)}")

def load_budget_data(filepath):
    if not os.path.exists(filepath):
        return 0, []
    
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data.get('initial_budget', 0), data.get('expenses', [])
    except (FileNotFoundError, json.JSONDecodeError):
        return 0, []  # Return default values if the file doesn't exist or is empty/corrupted

def save_budget_data(filepath, initial_budget, expenses):
    data = {
        'initial_budget': initial_budget,
        'expenses': expenses
    }
    try:
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=4)
        print("Budget details saved.")
    except IOError as e:
        print(f"Error saving budget data: {e}")

def main():
    print("Welcome to the Budget App")
    
    filepath = 'budget_data.json'  # Define the path to your JSON file
    initial_budget, expenses = load_budget_data(filepath)
    
    if initial_budget == 0:
        while True:
            try:
                initial_budget = float(input("Please enter your initial budget: "))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
    
    budget = initial_budget

    while True:
        print("\nWhat would you like to do?")
        print("1. Add an expense")
        print("2. Show budget details")
        print("3. Save budget details")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            description = input("Enter expense description: ")
            while True:
                try:
                    amount = float(input("Enter expense amount: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
            add_expense(expenses, description, amount)
        elif choice == "2":
            show_budget_details(budget, expenses)
        elif choice == "3":
            save_budget_data(filepath, initial_budget, expenses)
        elif choice == "4":
            save_budget_data(filepath, initial_budget, expenses)  # Save before exiting
            print("Exiting Budget App. Goodbye!")
            break
        else:
            print("Invalid choice, please choose again.")

if __name__ == "__main__":


    main()