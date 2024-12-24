# Links:(Google Slides Presentation) https://docs.google.com/presentation/d/1AmtnxYljBivZqMialxoPqcF1i0c_Atr1tSksulSP95k/edit#slide=id.g2d7215db24f_0_72
#       (Video Presentation link on how the app works) https://youtu.be/rIyHv5JGW-A
# Personal Finance Dashboard

## Description
The **Personal Finance Dashboard** is a tool designed to help users effectively manage their financial data. It enables users to track spending, monitor savings goals, and gain valuable insights into their financial habits. By providing features such as transaction categorization, goal tracking, and data visualizations, this dashboard simplifies personal finance management.

---

## Problem Statement
Managing personal finances manually or through spreadsheets can be tedious, time-consuming, and error-prone. Common challenges include:
- Difficulty in tracking and categorizing daily expenses.
- Limited ability to visualize and analyze spending patterns.
- Challenges in setting and achieving financial goals.
- Lack of automated financial insights and advice.

These inefficiencies often result in untracked spending and missed opportunities for savings.

---

## Proposed Solution
The **Personal Finance Dashboard** provides users with a centralized and structured system for financial management. It offers:
1. **Income and Expense Management:** Easy input, viewing, and categorization of financial transactions.
2. **Goal Setting and Tracking:** Tools to set financial goals and track progress toward achieving them.
3. **Data Visualizations:** Charts and graphs for insights into spending habits and financial health.
4. **Expense Categorization:** Clear breakdowns of where money is being spent.
5. **Scalability:** A flexible design for future expansion, such as bill reminders and budget forecasts.
6. **Ease of Use:** An intuitive interface that simplifies finance management for all users.

---

## Features and Functionalities

### 1. **Income Management**
- Add, view, update, and delete income transactions.
- Input details such as amount, source, and date of income.

### 2. **Expense Management**
- Add, view, update, and delete expense transactions.
- Categorize expenses by type (e.g., groceries, rent, entertainment).

### 3. **Financial Goal Management**
- Set, view, update, and delete financial goals.
- Track progress on savings targets with visual indicators.

### 4. **Expense Category Management**
- Add, view, update, and delete categories for organizing expenses.

### 5. **Financial Institution Management**
- Link multiple financial institutions (e.g., banks, credit unions) to user accounts.
- Manage account types (e.g., checking, savings) and unlink institutions when needed.

### 6. **Dashboard Overview**
- Display a summary of total income, expenses, and progress on financial goals.


## Table Relationships

### Income and Expenses
- **One-to-Many Relationship:** One income transaction can be associated with multiple expenses.

### Users and Goals
- **One-to-Many Relationship:** One user can manage multiple financial goals.

### Transactions and Categories
- **One-to-Many Relationship:** Each transaction belongs to one category.

### Users and Financial Institutions
- **Many-to-Many Relationship:** 
  - A user can link multiple financial institutions.
  - A financial institution can serve multiple users.

---

## Scalability and Future Features
This dashboard is built with scalability in mind. Potential future enhancements include:
- **Bill Reminders:** Notifications for upcoming bill payments.
- **Budget Forecasts:** Tools to predict and plan future budgets.
- **Machine Learning Insights:** Personalized financial advice using AI.

---

## Setup
1. **Clone the Repository:** Clone this repository to your local machine.
2. Run 
- pipenv shell
Then ;
- pipenv install
Then ;
- pytest

and Finally:
- cd into the "app" directory and,
- run the main.py file

3. **Manage Finances:** Manage Income, Manage Expenses, Manage Saving Goals, Manage Financial Institutions

---

## Technologies Used
- **Backend:** Python3, SQLAlchemy, Alembic
- **Database:** SQLite3
- **Testing:** Pytest

---

## Project Structure
 CLI-SQLALCHEMY-APP-|---app---config.py
                    |       ---main.py
                    |       ---models.py
                    |       ---seed.py
                    |       ---__pycache__
                    |       ---.pytest_cache
                    |
                    |---tests---__init__.py
                    |         ---test_main.py
                    |
                    |---alembic.ini           
                    |---finance.sqlite
                    |---Pipfile
                    |---Pipfile.lock
                    |---README.md
                    |---.pytest_cache
                    |---.venv
                    |---alembic---versions
                    |          ---env.py
                    |          ---script.py.mako
                    |          ---README
---

## License
This project is licensed under the EvansKabiru© License.

---

## Contact
For questions or feedback, reach out to **Evans Kabiru**.
