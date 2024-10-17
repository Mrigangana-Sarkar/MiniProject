import json # Import json module to handle saving and loading expense data
import os # Import os module to check for file existence
from datetime import datetime # Import datetime for handling and formatting dates

# File to store expenses
FILE_NAME = "expenses.json" # Define the filename for storing expenses

# Load data from file (if exists)
def load_expenses():
    if os.path.exists(FILE_NAME): # Check if the file exists
        with open(FILE_NAME, "r") as file: # Open the file in read mode
            return json.load(file) # Load and return JSON data as a list of expenses
    return [] # Return an empty list if the file does not exist

# Save data to file
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file: # Open the file in write mode
        json.dump(expenses, file, indent=4) # Save the expenses list as JSON with indentation for readability

# Display all expenses
def display_expenses(expenses):
    if not expenses: # Check if there are no expenses
        print("No expenses recorded yet.") # Print message if no expenses are found
    else:
        print("\nCurrent Expenses:") # Print header for expenses
        for expense in expenses: # Loop through each expense in the list
            print(f"Amount: Rs.{expense['amount']}, Category: {expense['category']}, Date: {expense['date']}") # Print expense details
        print("\n") # Add a newline for spacing

# Add an expense
def add_expense(expenses):
    amount = float(input("Enter the amount: ")) # Prompt user to input the expense amount and convert to float
    category = input("Enter the category (e.g., Food, Transport): ") # Prompt user to input the expense category
    date = input("Enter the date (YYYY-MM-DD) or press Enter for today: ") # Prompt user to input the expense date
    if not date: # If no date is entered, use today's date
        date = datetime.today().strftime('%Y-%m-%d') # Format today's date as 'YYYY-MM-DD'
    
    # Create expense dictionary
    expense = {
        "amount": amount, # Set the amount
        "category": category, # Set the category
        "date": date # Set the date
    }
    
    expenses.append(expense) # Add the new expense to the list
    save_expenses(expenses) # Save the updated list to the file
    print(f"Expense of {amount} in {category} added!") # Confirm addition to the user

# View summary
def view_summary(expenses):
    print("\n1. Total spending by category") # Print summary option 1
    print("2. Total overall spending") # Print summary option 2
    print("3. Spending over time (monthly)") # Print summary option 3
    choice = input("Choose an option: ") # Prompt user to choose a summary option
    
    if choice == "1": # If user chooses option 1
        category = input("Enter the category: ") # Prompt user for category input
        total = sum(expense['amount'] for expense in expenses if expense['category'].lower() == category.lower()) # Calculate total for that category
        print(f"Total spending on {category}: Rs.{total}") # Display the total spending on that category
    
    elif choice == "2": # If user chooses option 2
        total = sum(expense['amount'] for expense in expenses) # Calculate total spending
        print(f"Total overall spending: Rs.{total}") # Display the total spending
    
    elif choice == "3": # If user chooses option 3
        summary = {} # Initialize an empty dictionary for monthly summary
        for expense in expenses: # Loop through each expense
            month = expense['date'][:7] # Extract "YYYY-MM" for monthly summary
            if month in summary: # If the month is already in the summary
                summary[month] += expense['amount'] # Add the amount to the existing total
            else:
                summary[month] = expense['amount'] # Create a new month entry with the amount
        
        for month, total in summary.items(): # Loop through each month and its total spending
            print(f"{month}:Rs.{total}") # Display monthly spending

# Menu for the user
def main_menu():
    expenses = load_expenses() # Load expenses from file
    
    # Display expenses at the start
    display_expenses(expenses) # Show all existing expenses to the user
    
    while True: # Start an infinite loop for the main menu
        print("\nPersonal Expense Tracker") # Print application title
        print("1. Add Expense") # Print option 1 for adding an expense
        print("2. View Summary") # Print option 2 for viewing summary
        print("3. Exit") # Print option 3 for exiting the application
        
        choice = input("Enter your choice: ") # Prompt user for menu choice
        
        if choice == "1": # If user chooses to add an expense
            add_expense(expenses) # Call add_expense function
        elif choice == "2": # If user chooses to view summary
            view_summary(expenses) # Call view_summary function
        elif choice == "3": # If user chooses to exit
            print("Exiting program...") # Print exit message
            break # Exit the loop and end the program
        else:
            print("Invalid choice. Please choose again.") # Prompt for valid input if choice is invalid

if __name__ == "__main__":
    main_menu() # Run the main_menu function to start the application

