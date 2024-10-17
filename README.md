Personal Expense Tracker

The Personal Expense Tracker is a simple command-line application built with Python that helps users manage their daily expenses. It allows users to add expenses, view summaries by category or month, and save their expense data for later use.

Features

1. Add Expense: Record a new expense with details such as amount, category, and date.


2. View Summary:

Total spending by category

Total overall spending

Monthly,Daily and weekly spending summary



3. Data Persistence: Automatically saves expense data to a JSON file, so data is retained between sessions.


4. Display Expenses: Shows all recorded expenses at the start of the application.



Requirements

Python 3.x

No additional external libraries are required.


Files

expenses.json: This file stores all expense data in JSON format. The program will create it automatically if it does not exist.

Main Script: The Python script contains all functionality, including expense tracking and summary viewing.


Functions

1. load_expenses()

Loads expense data from expenses.json if it exists. If the file does not exist, it returns an empty list.

Returns: List of expenses


2. save_expenses(expenses)

Saves the current list of expenses to expenses.json in a readable JSON format.

Parameters:

expenses (list): List of expense dictionaries to save.



3. display_expenses(expenses)

Displays all current expenses to the user. If no expenses are found, it notifies the user.

Parameters:

expenses (list): List of expense dictionaries to display.



4. add_expense(expenses)

Prompts the user to enter details for a new expense (amount, category, and date).

If no date is entered, it defaults to the current date.

Adds the expense to the list and saves it to expenses.json.

Parameters:

expenses (list): List of current expenses to which the new expense will be added.



5. view_summary(expenses)

Provides three summary options to the user:

1. Total Spending by Category: Prompts for a category and displays the total spending in that category.


2. Total Overall Spending: Displays the total spending for all categories.


3. Spending Over Time (Monthly,Daily,Weekly): Displays total spending for each month,or day or week in the respective format.



Parameters:

expenses (list): List of current expenses to generate a summary from.



6. main_menu()

The main menu function for the application. It loads expenses from the file, displays the current expenses, and provides the following options:

1. Add a new expense


2. View summaries of expenses


3. Exit the application



It continuously loops, allowing users to enter expenses and view summaries until they choose to exit.
