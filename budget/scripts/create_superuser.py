import os

import django
from django.contrib.auth import get_user_model


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'budget_project.settings')
django.setup()

user = get_user_model()
admin_username = os.getenv("DJANGO_SUPERUSER_USERNAME")
admin_email = os.getenv("DJANGO_SUPERUSER_EMAIL")
admin_passwd = os.getenv("DJANGO_SUPERUSER_PASSWORD")

if not user.objects.filter(username=admin_username).exists():
    user.objects.create_superuser(admin_username, admin_email, admin_passwd)
    print("Superuser has been created!")
else:
    print("Superuser already exists!")
