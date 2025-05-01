import pytest

from django.contrib.auth.models import User


@pytest.fixture
def test_user():
    if not User.objects.filter(username="testuser").exists():
        user = User.objects.create_user(username="testuser", password="testpasswd")
        print("Test user has been created!")
        print(User.objects.filter(username="testuser"))
    else:
        user = User.objects.get(username="testuser")

    return user