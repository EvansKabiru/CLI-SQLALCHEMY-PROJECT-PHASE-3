import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, Income, Expense, FinancialGoal, FinancialInstitution, Category, User

# Create a test database in memory
test_engine = create_engine("sqlite:///:memory:")
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)
Base.metadata.create_all(bind=test_engine)

# Fixture for setting up a clean database session for each test
@pytest.fixture(scope="function")
def session():
    session = TestingSessionLocal()
    yield session
    session.close()

# ==================== Tests for Income ====================
def test_add_income(session):
    income = Income(amount=1000.0, source="Salary")
    session.add(income)
    session.commit()

    incomes = session.query(Income).all()
    assert len(incomes) == 1
    assert incomes[0].amount == 1000.0
    assert incomes[0].source == "Salary"

def test_view_incomes(session):
    income = Income(amount=1500.0, source="Freelancing")
    session.add(income)
    session.commit()

    incomes = session.query(Income).all()
    assert len(incomes) == 1
    assert incomes[0].amount == 1500.0
    assert incomes[0].source == "Freelancing"

def test_update_income(session):
    income = Income(amount=2000.0, source="Investment")
    session.add(income)
    session.commit()

    income.amount = 2500.0
    session.commit()

    updated_income = session.query(Income).filter_by(source="Investment").first()
    assert updated_income.amount == 2500.0

def test_delete_income(session):
    income = Income(amount=3000.0, source="Business")
    session.add(income)
    session.commit()

    session.delete(income)
    session.commit()

    incomes = session.query(Income).all()
    assert len(incomes) == 0

# ==================== Tests for Expenses ====================
def test_add_expense(session):
    category = Category(name="Utilities")
    session.add(category)
    session.commit()

    expense = Expense(amount=500.0, category_id=category.id)
    session.add(expense)
    session.commit()

    expenses = session.query(Expense).all()
    assert len(expenses) == 1
    assert expenses[0].amount == 500.0
    assert expenses[0].category_id == category.id

def test_view_expenses(session):
    category = Category(name="Groceries")
    session.add(category)
    session.commit()

    expense = Expense(amount=200.0, category_id=category.id)
    session.add(expense)
    session.commit()

    expenses = session.query(Expense).all()
    assert len(expenses) == 1
    assert expenses[0].amount == 200.0
    assert expenses[0].category_id == category.id

def test_update_expense(session):
    category = Category(name="Transport")
    session.add(category)
    session.commit()

    expense = Expense(amount=100.0, category_id=category.id)
    session.add(expense)
    session.commit()

    expense.amount = 150.0
    session.commit()

    updated_expense = session.query(Expense).filter_by(category_id=category.id).first()
    assert updated_expense.amount == 150.0

def test_delete_expense(session):
    category = Category(name="Entertainment")
    session.add(category)
    session.commit()

    expense = Expense(amount=400.0, category_id=category.id)
    session.add(expense)
    session.commit()

    session.delete(expense)
    session.commit()

    expenses = session.query(Expense).all()
    assert len(expenses) == 0

# ==================== Tests for Savings Goals ====================
def test_add_savings_goal(session):
    user = User(username="testuser", email="test@example.com", password="password")
    session.add(user)
    session.commit()

    goal = FinancialGoal(target_amount=10000.0, user_id=user.id)
    session.add(goal)
    session.commit()

    goals = session.query(FinancialGoal).all()
    assert len(goals) == 1
    assert goals[0].target_amount == 10000.0
    assert goals[0].user_id == user.id

# Test reading savings goals
def test_read_savings_goals(session):
    user = User(username="testuser", email="test@example.com", password="password")
    session.add(user)
    session.commit()

    goal1 = FinancialGoal(target_amount=10000.0, user_id=user.id)
    goal2 = FinancialGoal(target_amount=5000.0, user_id=user.id)
    session.add_all([goal1, goal2])
    session.commit()

    goals = session.query(FinancialGoal).filter_by(user_id=user.id).all()
    assert len(goals) == 2
    assert goals[0].target_amount == 10000.0
    assert goals[1].target_amount == 5000.0


# Test updating a savings goal
def test_update_savings_goal(session):
    user = User(username="testuser", email="test@example.com", password="password")
    session.add(user)
    session.commit()

    goal = FinancialGoal(target_amount=10000.0, user_id=user.id)
    session.add(goal)
    session.commit()

    # Update the goal
    goal.target_amount = 15000.0
    session.commit()

    updated_goal = session.query(FinancialGoal).filter_by(id=goal.id).first()
    assert updated_goal.target_amount == 15000.0


# Test deleting a savings goal
def test_delete_savings_goal(session):
    user = User(username="testuser", email="test@example.com", password="password")
    session.add(user)
    session.commit()

    goal = FinancialGoal(target_amount=10000.0, user_id=user.id)
    session.add(goal)
    session.commit()

    # Delete the goal
    session.delete(goal)
    session.commit()

    goals = session.query(FinancialGoal).filter_by(user_id=user.id).all()
    assert len(goals) == 0
    
# Additional tests for categories and financial institutions can be implemented similarly.
def test_add_financial_institution(test_session):
    # Add a financial institution
    institution = FinancialInstitution(name="Bank of Test", account_type="Savings")
    test_session.add(institution)
    test_session.commit()

    # Verify it was added
    result = test_session.query(FinancialInstitution).filter_by(name="Bank of Test").first()
    assert result is not None
    assert result.account_type == "Savings"

def test_view_financial_institutions(test_session):
    # Add a second financial institution
    institution = FinancialInstitution(name="Test Credit Union", account_type="Checking")
    test_session.add(institution)
    test_session.commit()

    # Verify both institutions exist
    institutions = test_session.query(FinancialInstitution).all()
    assert len(institutions) == 2
    assert institutions[0].name == "Bank of Test"
    assert institutions[1].name == "Test Credit Union"

def test_update_financial_institution(test_session):
    # Update the first institution
    institution = test_session.query(FinancialInstitution).filter_by(name="Bank of Test").first()
    institution.name = "Updated Bank of Test"
    test_session.commit()

    # Verify the update
    updated_institution = test_session.query(FinancialInstitution).filter_by(name="Updated Bank of Test").first()
    assert updated_institution is not None
    assert updated_institution.name == "Updated Bank of Test"

def test_delete_financial_institution(test_session):
    # Delete the second institution
    institution = test_session.query(FinancialInstitution).filter_by(name="Test Credit Union").first()
    test_session.delete(institution)
    test_session.commit()

    # Verify deletion
    deleted_institution = test_session.query(FinancialInstitution).filter_by(name="Test Credit Union").first()
    assert deleted_institution is None

def test_add_user_to_institution(test_session):
    # Create a user and associate with a financial institution
    user = User(username="test_user", email="test_user@example.com", password="password123")
    institution = test_session.query(FinancialInstitution).filter_by(name="Updated Bank of Test").first()
    user.financial_institutions.append(institution)
    test_session.add(user)
    test_session.commit()

    # Verify the association
    result = test_session.query(User).filter_by(username="test_user").first()
    assert result is not None
    assert len(result.financial_institutions) == 1
    assert result.financial_institutions[0].name == "Updated Bank of Test"

def test_remove_user_from_institution(test_session):
    # Remove user from financial institution
    user = test_session.query(User).filter_by(username="test_user").first()
    institution = user.financial_institutions[0]
    user.financial_institutions.remove(institution)
    test_session.commit()

    # Verify the removal
    updated_user = test_session.query(User).filter_by(username="test_user").first()
    assert updated_user is not None
    assert len(updated_user.financial_institutions) == 0
