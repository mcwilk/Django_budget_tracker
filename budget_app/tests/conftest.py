import logging

import pytest
from django.contrib.auth.models import User

from budget_app.models import BudgetInfo, Expenses


@pytest.fixture
def test_user():
    if not User.objects.filter(username="test_user").exists():
        user = User.objects.create_user(username="test_user", password="test_passwd")
        logging.info("Test user has been created!")
    else:
        user = User.objects.get(username="testuser")

    return user

@pytest.fixture
def test_budget(test_user):
    user = test_user
    budget = BudgetInfo.objects.create(name="test_budget", owner=user, balance=1000, created_on="2025-02-01")
    logging.info("Test budget has been created!")

    return budget

@pytest.fixture
def test_expenses(test_budget):
    budget = test_budget

    for n in range(1, 4):
        Expenses.objects.create(budget=budget, title=f"expense{n}", date=f"2025-02-0{n}", price=100, category=1,
                                transaction=1)
        logging.info(f"Test expense no.{n} has been created!")

    all_expenses = Expenses.objects.all()

    return budget, all_expenses