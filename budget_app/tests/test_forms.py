import pytest
from assertpy import assert_that, soft_assertions
from django import forms
from django.urls import reverse

from budget_app.forms import BudgetForm
from budget_app.models import BudgetInfo


class TestForms:

    def test_budget_creation_with_valid_data(self, client, test_user_login):
        user = test_user_login
        form_data = {'name': 'TestBudget', 'balance': 1000}
        response = client.post(reverse('new_budget'), form_data)

        with soft_assertions():
            assert_that(response.status_code).is_equal_to(302)
            assert_that(response.url).does_not_contain('login')
            assert_that(response.url).ends_with(f'/budgets/{user}')
            assert_that(BudgetInfo.objects.count()).is_equal_to(1)
            assert_that(BudgetInfo.objects.all()[0].name).is_upper()
            assert_that(BudgetInfo.objects.filter(name=form_data['name'].upper()).exists()).is_true()

    def test_budget_creation_with_invalid_balance(self, client, test_user_login):
        _ = test_user_login
        form_data = {'name': 'TestBudget', 'balance': -1000}
        response = client.post(reverse('new_budget'), form_data)

        with soft_assertions():
            assert_that(response.status_code).is_equal_to(200)
            assert_that(BudgetInfo.objects.filter(name=form_data['name'].upper()).exists()).is_false()
            assert_that(response.context['form'].errors['balance']).contains('Budget balance cannot be negative.')

    def test_clean_balance_raises_validation_error(self, test_user_login):
        _ = test_user_login

        # Exception is caught by Django's form validation (is_valid()) (not accessible outside, e.g. via response!)
        form = BudgetForm()
        form.cleaned_data = {'balance': -1000}

        with pytest.raises(forms.ValidationError):
            form.clean_balance()  # needs to be called manually to raise the exception

        assert_that(form.is_valid()).is_false()

    def test_budget_creation_with_existing_name(self, client, test_user_login):
        _ = test_user_login
        form_data = {'name': 'TestBudget', 'balance': 1000}
        response = client.post(reverse('new_budget'), form_data)

        # Checking if the budget was created successfully
        assert_that(response.status_code).is_equal_to(302)
        assert_that(BudgetInfo.objects.count()).is_equal_to(1)

        # Another budget with the same name
        form_data['balance'] = 500
        response = client.post(reverse('new_budget'), form_data)

        with soft_assertions():
            assert_that(BudgetInfo.objects.count()).is_equal_to(1)
            assert_that(BudgetInfo.objects.filter(name=form_data['name'].upper()).count()).is_equal_to(1)
            assert_that(BudgetInfo.objects.get(name=form_data['name'].upper()).balance).is_equal_to(1000)
            assert_that(BudgetInfo.objects.filter(balance=form_data['balance']).count()).is_equal_to(0)
            assert_that(response.context['form'].errors['name']).contains(
                f'Budget with name {form_data["name"]} already exists.'
            )

    def test_budget_creation_with_too_short_name(self, client, test_user_login):
        _ = test_user_login
        form_data = {'name': 'abc', 'balance': 1000}
        response = client.post(reverse('new_budget'), form_data)

        with soft_assertions():
            assert_that(BudgetInfo.objects.count()).is_equal_to(0)
            assert_that(BudgetInfo.objects.filter(name=form_data['name'].upper()).count()).is_equal_to(0)
            assert_that(response.context['form'].errors['name']).contains(
                'Budget name must be at least 5 characters long.'
            )

    def test_budget_creation_without_name(self, client, test_user_login):
        _ = test_user_login
        form_data = {'name': '', 'balance': 1000}
        response = client.post(reverse('new_budget'), form_data)

        with soft_assertions():
            assert_that(BudgetInfo.objects.count()).is_equal_to(0)
            assert_that(BudgetInfo.objects.filter(name=form_data['name'].upper()).count()).is_equal_to(0)
            assert_that(response.context['form'].errors['name']).contains(
                'Budget name is required.'
            )

    def test_budget_creation_without_balance(self, client, test_user_login):
        _ = test_user_login
        form_data = {'name': 'TestBudget', 'balance': ''}
        response = client.post(reverse('new_budget'), form_data)

        with soft_assertions():
            assert_that(BudgetInfo.objects.count()).is_equal_to(0)
            assert_that(BudgetInfo.objects.filter(name=form_data['name'].upper()).count()).is_equal_to(0)
            assert_that(response.context['form'].errors['balance']).contains(
                'Budget balance is required.'
            )