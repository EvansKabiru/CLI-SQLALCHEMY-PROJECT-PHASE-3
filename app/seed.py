from faker import Faker
fake = Faker()

from config import *
from models import User, Income, Expense, FinancialGoal, Category

# Seed Income
for _ in range(20):
    income = Income(
        amount=round(fake.pyfloat(left_digits=4, right_digits=2, positive=True), 2),
        source=fake.job()
    )
    session.add(income)

# Seed Expenses
for _ in range(20):
    expense = Expense(
        amount=round(fake.pyfloat(left_digits=3, right_digits=2, positive=True), 2),
        category=fake.word(ext_word_list=["Food", "Rent", "Utilities", "Transport", "Entertainment"])
    )
    session.add(expense)

# Seed Savings Goals
for _ in range(10):
    goal = FinancialGoal(
        amount=round(fake.pyfloat(left_digits=4, right_digits=2, positive=True), 2),
        description=fake.text(max_nb_chars=50)
    )
    session.add(goal)

# Commit the data to the database
session.commit()
print("Database seeded successfully!")