class BudgetTracker:
    def __init__(self):
        self.income = 0
        self.expenses = []
    
    def add_income(self, amount):
        self.income += amount
        print(f"Income of ${amount} added.")
    
    def add_expense(self, category, amount):
        self.expenses.append((category, amount))
        print(f"Expense of ${amount} under '{category}' added.")
    
    def total_income(self):
        return self.income
    
    def total_expenses(self):
        return sum(amount for category, amount in self.expenses)
    
    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded yet.")
        else:
            print("Expense List:")
            for category, amount in self.expenses:
                print(f"{category}: ${amount}")
    
    def budget_summary(self):
        total_income = self.total_income()
        total_expenses = self.total_expenses()
        balance = total_income - total_expenses
        
        print("\nBudget Summary:")
        print(f"Total Income: ${total_income}")
        print(f"Total Expenses: ${total_expenses}")
        print(f"Balance: ${balance}")
        

def main():
    budget_tracker = BudgetTracker()
    
    while True:
        print("\nMenu:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Expenses")
        print("4. View Budget Summary")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            try:
                amount = float(input("Enter income amount: "))
                budget_tracker.add_income(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        elif choice == '2':
            category = input("Enter expense category: ")
            try:
                amount = float(input("Enter expense amount: "))
                budget_tracker.add_expense(category, amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        elif choice == '3':
            budget_tracker.view_expenses()
        
        elif choice == '4':
            budget_tracker.budget_summary()
        
        elif choice == '5':
            print("Exiting budget tracker. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
