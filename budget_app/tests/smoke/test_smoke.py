import logging
from http import HTTPStatus

import requests
from assertpy import assert_that
from django.urls import reverse

from budget_app.models import BudgetInfo


class TestSmoke:
    homepage = "http://localhost:8000/"

    def test_homepage(self):
        """Test to check that application is up and running"""
        response = requests.get(self.homepage)

        assert_that(response.status_code).is_equal_to(HTTPStatus.OK)
        assert_that(response.text).contains("Welcome to Budget-App")

    @staticmethod
    def test_db_connection(test_user_login):
        """Test to check that database connection is established properly"""
        user = test_user_login
        _ = BudgetInfo.objects.create(name="budget1", owner=user, balance=2000, created_on="2025-02-10")
        assert_that(BudgetInfo.objects.count()).is_equal_to(1)

    def test_admin_panel(self):
        """Test to check that admin panel is configured"""
        response = requests.get(self.homepage + "/admin/login")

        assert_that(response.status_code).is_equal_to(HTTPStatus.OK)
        assert_that(response.text).contains("Django administration")

    def test_not_auth_access(self):
        """Test to check that unauthorized user has no access and redirected to login page"""
        response = requests.get(self.homepage + "/budgets/new", allow_redirects=False)

        assert_that(response.status_code).is_equal_to(HTTPStatus.FOUND)  # 302
        assert_that(response.headers['Location']).contains("/login/")

    def test_auth_access(self, client, test_user):
        """Test to check that authorized user is able to see the data"""
        client.force_login(test_user)
        budget = BudgetInfo.objects.create(name="budget1", owner=test_user, balance=2000, created_on="2025-02-10")
        assert_that(BudgetInfo.objects.count()).is_equal_to(1)
        response = client.get(reverse('budget_list', kwargs={'username': test_user}))

        assert_that(response.status_code).is_equal_to(HTTPStatus.OK)
        assert_that(response.content.decode("utf-8")).contains(budget.name)


