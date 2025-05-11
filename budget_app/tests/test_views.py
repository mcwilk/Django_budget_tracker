from assertpy import assert_that, soft_assertions
from bs4 import BeautifulSoup
from django.urls import reverse

from budget_app.models import BudgetInfo


class TestViews:

    def test_index_view_basic_template(self, client):
        response = client.get(reverse('home'))
        html = response.content.decode("utf-8")
        soup = BeautifulSoup(response.content, "html.parser")
        index_view_temps = [t.name for t in response.templates]
        header = soup.find("header").text.strip()
        buttons = [btn.text.strip() for btn in soup.find_all("button")]

        with soft_assertions():
            assert_that(response.status_code).is_equal_to(200)
            assert_that(index_view_temps).contains("budget_app/index.html")
            assert_that(html).contains("Login or register to continue")
            assert_that(header).is_equal_to("Welcome to Budget-App")
            assert_that(buttons).contains("Login", "Register")

    def test_index_view_redirects_if_logged_in(self, client, test_user_login):
        user = test_user_login
        response = client.get(reverse('home'))
        response_follow = client.get(reverse('home'), follow=True)
        soup = BeautifulSoup(response_follow.content, "html.parser")
        index_view_temps = [t.name for t in response_follow.templates]
        buttons = [btn.text.strip() for btn in soup.find_all("button")]

        with soft_assertions():
            assert_that(response.status_code).is_equal_to(302)  # redirected
            assert_that(response.url).contains(f'budgets/{user}')
            assert_that(response.templates).is_empty()
            assert_that(response.content).is_empty()

            assert_that(response_follow.status_code).is_equal_to(200)  # follow=True --> GET to target URL
            assert_that(response.url).does_not_exist()
            assert_that(index_view_temps).contains("budget_app/budget_list.html")
            assert_that(buttons).contains("NEW")

    def test_budget_list_view(self, client, test_user_login):
        user = test_user_login
        budget = BudgetInfo.objects.create(name="budget1", owner=user, balance=2000, created_on="2025-02-10")
        response = client.get(reverse('budget_list', kwargs={'username': user}))
        soup = BeautifulSoup(response.content, "html.parser")
        index_view_temps = [t.name for t in response.templates]
        buttons = [btn.text.strip() for btn in soup.find_all("button")]
        budget_data = soup.find("div", class_="budget-list-item").text.strip()

        with soft_assertions():
            assert_that(BudgetInfo.objects.count()).is_equal_to(1)
            assert_that(response.status_code).is_equal_to(200)
            assert_that(index_view_temps).contains("budget_app/budget_list.html")
            assert_that(buttons).contains("NEW")
            assert_that(budget_data).contains(str(budget.name), str(budget.balance))
            assert_that(soup).does_not_contain("Your budget list is empty.")
