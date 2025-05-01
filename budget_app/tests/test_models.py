import logging

import pytest
from assertpy import assert_that, soft_assertions

from budget_app.models import BudgetInfo, Expenses


@pytest.mark.django_db
class TestBudgetInfo:

    def test_budget_info_creation(self, test_user):
        logging.info(f"Running first test...")
        user = test_user
        budget = BudgetInfo.objects.create(name="budget1", owner=user, balance=1000, created_on="2023-10-01")
        logging.info(f"All objects: {BudgetInfo.objects.all()}")

        with soft_assertions():
            assert_that(BudgetInfo.objects.count()).is_equal_to(1)
            assert_that(budget).is_not_none()
            assert_that(str(budget)).is_equal_to(f"Budget: budget1 (owner: {user.username}, date: 2023-10-01)")
            assert_that(budget.name).is_equal_to("budget1")
            assert_that(budget.owner_id).is_equal_to(1)
            assert_that(budget.balance).is_equal_to(1000)
            assert_that(budget.created_on).contains("2023-10-01")

            # assert_that(budget.get_total_expenses()).is_equal_to(0)
            # assert_that(budget.get_balance_left()).is_equal_to(1000)
            # assert_that(str(budget)).is_equal_to("Budget: budget1 (owner: 2, date: 2023-10-01)")