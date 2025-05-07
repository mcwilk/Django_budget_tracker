import logging
from datetime import timedelta

import pytest
from assertpy import assert_that, soft_assertions
from django.utils import timezone

from budget_app.models import BudgetInfo, Expenses


@pytest.mark.django_db
class TestModels:

    def test_budget_info_creation(self, test_user):
        logging.info(f"Running 'test_budget_info_creation'...")
        user = test_user
        budget = BudgetInfo.objects.create(name="budget1", owner=user, balance=2000, created_on="2025-02-10")

        with soft_assertions():
            assert_that(hasattr(budget, 'name')).is_true()
            assert_that(hasattr(budget, 'owner')).is_true()
            assert_that(hasattr(budget, 'balance')).is_true()
            assert_that(hasattr(budget, 'created_on')).is_true()
            assert_that(hasattr(budget, 'get_total_expenses')).is_true()
            assert_that(hasattr(budget, 'get_balance_left')).is_true()
            assert_that(str(budget)).is_equal_to(f"Budget: budget1 (owner: {user.username}, date: 2025-02-10)")

        with soft_assertions():
            assert_that(BudgetInfo.objects.count()).is_equal_to(1)
            assert_that(budget.name).is_equal_to("budget1")
            # TODO: add condition that if tested on DEV than it may fail (more users)
            # assert_that(budget.owner_id).is_equal_to(1)
            assert_that(budget.balance).is_equal_to(2000)
            assert_that(str(budget.created_on)).contains("2025-02-10")

    def test_expense_creation(self, test_budget):
        logging.info(f"Running 'test_expense_creation'...")
        budget = test_budget
        today = timezone.now()
        today_plus_1 = today + timedelta(days=1)

        # Create new expenses
        Expenses.objects.create(budget=budget, title="expense1", price=100, category=1, transaction=1)
        Expenses.objects.create(budget=budget, title="expense2", date=today_plus_1, price=100, category=2,
                                transaction=2)

        all_expenses = Expenses.objects.all()
        titles = [expense.title for expense in all_expenses]

        with soft_assertions():
            for expense in all_expenses:
                assert_that(hasattr(expense, 'budget')).is_true()
                assert_that(hasattr(expense, 'title')).is_true()
                assert_that(hasattr(expense, 'date')).is_true()
                assert_that(hasattr(expense, 'price')).is_true()
                assert_that(hasattr(expense, 'category')).is_true()
                assert_that(hasattr(expense, 'transaction')).is_true()
                assert_that(len(expense.CATEGORIES)).is_equal_to(20)
                assert_that(len(expense.PAYMENTS)).is_equal_to(4)
                assert_that(str(expense)).is_equal_to(expense.title)

        with soft_assertions():
            assert_that(Expenses.objects.count()).is_equal_to(2)
            assert_that(titles).is_equal_to(["expense2", "expense1"])

            for idx, expense in zip(range(len(all_expenses), 0, -1), all_expenses):
                assert_that(expense.budget_id).is_equal_to(budget.id)
                assert_that(expense.title).is_equal_to(f"expense{idx}")
                assert_that(str(expense.date)).starts_with(str(today.date())) if idx == 1 else \
                    assert_that(str(expense.date)).starts_with(str(today_plus_1.date()))
                assert_that(expense.price).is_equal_to(100)
                assert_that(expense.category).is_equal_to(idx)
                assert_that(expense.transaction).is_equal_to(idx)

    def test_get_total_expenses(self, test_expenses):
        logging.info(f"Running 'test_get_total_expenses'...")
        budget, expenses = test_expenses

        assert_that(budget.get_total_expenses()).is_equal_to(300)

    def test_get_balance_left(self, test_expenses):
        logging.info(f"Running 'test_get_balance_left'...")
        budget, _ = test_expenses

        assert_that(budget.get_balance_left()).is_equal_to(700)
