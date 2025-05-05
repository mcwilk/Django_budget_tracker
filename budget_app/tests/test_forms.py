import logging

import pytest
from assertpy import assert_that, soft_assertions
from django import forms
from django.urls import reverse

from budget_app.models import BudgetInfo


@pytest.mark.django_db
class TestForms:

    def test_budget_creation_with_valid_data(self, client):
        form_data = {
            'name': 'Test Budget',
            'balance': 1000,
        }

        response = client.post(reverse('new_budget'), form_data)

        assert_that(response.status_code).is_equal_to(302)
        assert_that(BudgetInfo.objects.filter(name='Test Budget').exists()).is_true()

    # def test_budget_creation_with_invalid_balance(self, client):
    #     form_data = {
    #         'name': 'Test Budget',
    #         'balance': -1000,
    #     }
    #
    #     # with pytest.raises(forms.ValidationError):
    #     response = client.post(reverse('new_budget'), form_data)
    #     assert_that(response.status_code).is_equal_to(200)
    #     assert_that(response.errors).contains('Budget balance cannot be negative.')
    #         # assert_that(BudgetInfo.objects.filter(name='Test Budget').exists()).is_false()
