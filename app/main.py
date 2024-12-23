from config import *
from models import Income, Expense, FinancialGoal, FinancialInstitution, User, Category, UserInstitution
import os

def close_session():
    session.commit()
    session.close()

# ==================== CRUD Operations for Income ====================
def add_income():
    amount = float(input("Enter income amount: "))
    source = input("Enter income source: ")
    income = Income(amount=amount, source=source)
    session.add(income)
    close_session()
    print("Income Added!")

def view_incomes():
    incomes = session.query(Income).all()
    if not incomes:
        print("No incomes found.")
    else:
        for income in incomes:
            print(f"ID: {income.id}, Amount: {income.amount}, Source: {income.source}")

def update_income():
    income_id = int(input("Enter Income ID to update: "))
    income = session.query(Income).filter_by(id=income_id).first()
    if income:
        income.amount = float(input(f"Enter new amount (Current: {income.amount}): ") or income.amount)
        income.source = input(f"Enter new source (Current: {income.source}): ") or income.source
        close_session()
        print("Income updated!")
    else:
        print("Income not found.")

def delete_income():
    income_id = int(input("Enter Income ID to delete: "))
    income = session.query(Income).filter_by(id=income_id).first()
    if income:
        session.delete(income)
        close_session()
        print("Income deleted!")
    else:
        print("Income not found.")

# ==================== CRUD Operations for Expenses ====================
def add_expense():
    amount = float(input("Enter expense amount: "))
    category_id = input("Enter expense category: ")
    income_id = input("Enter expense income:")
    expense = Expense(amount=amount, category_id=category_id, income_id=income_id)
    session.add(expense)
    close_session()
    print("Expense Added!")

def view_expenses():
    expenses = session.query(Expense).all()
    if not expenses:
        print("No expenses found.")
    else:
        for expense in expenses:
            print(f"ID: {expense.id}, Amount: {expense.amount}, Category_id: {expense.category_id}, Income_id: {expense.income_id}")

def update_expense():
    expense_id = int(input("Enter Expense ID to update: "))
    expense = session.query(Expense).filter_by(id=expense_id).first()
    if expense:
        expense.amount = float(input(f"Enter new amount (Current: {expense.amount}): ") or expense.amount)
        expense.category_id = (input(f"Enter new category (Current: {expense.category_id}): ") or expense.category_id)
        expense.income_id = (input(f"Enter new category (Current: {expense.income_id}): ") or expense.income_id)
        close_session()
        print("Expense updated!")
    else:
        print("Expense not found.")

def delete_expense():
    expense_id = int(input("Enter Expense ID to delete: "))
    expense = session.query(Expense).filter_by(id=expense_id).first()
    if expense:
        session.delete(expense)
        close_session()
        print("Expense deleted!")
    else:
        print("Expense not found.")

# ==================== CRUD Operations for Savings Goals ====================
def add_savings_goal():
    target_amount = float(input("Enter savings goal amount: "))
    
    goal = FinancialGoal(target_amount=target_amount)
    session.add(goal)
    close_session()
    print("Savings goal added!")

def view_savings_goals():
    goals = session.query(FinancialGoal).all()
    if not goals:
        print("No savings goals found.")
    else:
        for goal in goals:
            print(f"ID: {goal.id}, Target_Amount: {goal.target_amount}")

def update_savings_goal():
    goal_id = int(input("Enter Savings Goal ID to update: "))
    goal = session.query(FinancialGoal).filter_by(id=goal_id).first()
    if goal:
        goal.target_amount = float(input(f"Enter new amount (Current: {goal.target_amount}): ") or goal.target_amount)
        
        close_session()
        print("Savings goal updated!")
    else:
        print("Savings goal not found.")

def delete_savings_goal():
    goal_id = int(input("Enter Savings Goal ID to delete: "))
    goal = session.query(FinancialGoal).filter_by(id=goal_id).first()
    if goal:
        session.delete(goal)
        close_session()
        print("Savings goal deleted!")
    else:
        print("Savings goal not found.")

# CRUD Operations for Financial Institutions
def add_financial_institution():
    os.system('clear')
    print("Add a Financial Institution")
    name = input("Enter the name of the financial institution: ")
    account_type = input("Enter the account type (e.g., Savings, Checking): ")

    institution = FinancialInstitution(name=name, account_type=account_type)
    session.add(institution)
    session.commit()

    print(f"Financial Institution '{name}' added successfully!")

def view_financial_institutions():
    os.system('clear')
    print("Financial Institutions")
    institutions = session.query(FinancialInstitution).all()

    if not institutions:
        print("No financial institutions found.")
    else:
        for institution in institutions:
            print(f"ID: {institution.id}, Name: {institution.name}, Account Type: {institution.account_type}")

def update_financial_institution():
    os.system('clear')
    print("Update Financial Institution")
    view_financial_institutions()

    institution_id = input("Enter the ID of the financial institution to update: ")
    institution = session.query(FinancialInstitution).get(institution_id)

    if not institution:
        print("Financial Institution not found.")
        return

    institution.name = input(f"Enter new name (current: {institution.name}): ") or institution.name
    institution.account_type = input(f"Enter new account type (current: {institution.account_type}): ") or institution.account_type
    session.commit()

    print(f"Financial Institution '{institution.name}' updated successfully!")

def delete_financial_institution():
    os.system('clear')
    print("Delete Financial Institution")
    view_financial_institutions()

    institution_id = input("Enter the ID of the financial institution to delete: ")
    institution = session.query(FinancialInstitution).get(institution_id)

    if not institution:
        print("Financial Institution not found.")
        return

    session.delete(institution)
    session.commit()

    print(f"Financial Institution '{institution.name}' deleted successfully!")

# ========================== Main CLI Application ============================
def main():
    
    while True:
        os.system('clear')
        print("Welcome to Personal Finance Dashboard")
        print("1. Manage Income")
        print("2. Manage Expenses")
        print("3. Manage Savings Goals")
        print("4. Manage Financial Institutions")
        main_menu_choice = input("Enter your Choice: ")

        if main_menu_choice == '1':
            while True:
                os.system('clear')
                print("1. Add Income")
                print("2. View Incomes")
                print("3. Update Income")
                print("4. Delete Income")
                print("5. Back to Main Menu")
                income_menu_choice = input("Enter your Choice: ")
                if income_menu_choice == '1':
                    add_income()
                elif income_menu_choice == '2':
                    view_incomes()
                elif income_menu_choice == '3':
                    update_income()
                elif income_menu_choice == '4':
                    delete_income()
                elif income_menu_choice == '5':
                    break
                input("Press Enter to continue...")

        elif main_menu_choice == '2':
            while True:
                os.system('clear')
                print("1. Add Expense")
                print("2. View Expenses")
                print("3. Update Expense")
                print("4. Delete Expense")
                print("5. Back to Main Menu")
                expense_menu_choice = input("Enter your Choice: ")
                if expense_menu_choice == '1':
                    add_expense()
                elif expense_menu_choice == '2':
                    view_expenses()
                elif expense_menu_choice == '3':
                    update_expense()
                elif expense_menu_choice == '4':
                    delete_expense()
                elif expense_menu_choice == '5':
                    break
                input("Press Enter to continue...")

        elif main_menu_choice == '3':
            while True:
                os.system('clear')
                print("1. Add Savings Goal")
                print("2. View Savings Goals")
                print("3. Update Savings Goal")
                print("4. Delete Savings Goal")
                print("5. Back to Main Menu")
                goal_menu_choice = input("Enter your Choice: ")
                if goal_menu_choice == '1':
                    add_savings_goal()
                elif goal_menu_choice == '2':
                    view_savings_goals()
                elif goal_menu_choice == '3':
                    update_savings_goal()
                elif goal_menu_choice == '4':
                    delete_savings_goal()
                elif goal_menu_choice == '5':
                    break
                input("Press Enter to continue...")

        elif main_menu_choice == '4':
            while True:
                os.system('clear')
                print("1. Add Financial Institution")
                print("2. View Financial Institutions")
                print("3. Update Financial Institution")
                print("4. Delete Financial Institution")
                print("5. Back to Main Menu")
                institution_menu_choice = input("Enter your Choice: ")
                if institution_menu_choice == '1':
                    add_financial_institution()
                elif institution_menu_choice == '2':
                    view_financial_institutions()
                elif institution_menu_choice == '3':
                    update_financial_institution()
                elif institution_menu_choice == '4':
                    delete_financial_institution()
                elif institution_menu_choice == '5':
                    break
                input("Press Enter to continue...")

if __name__ == "__main__":
    main()
