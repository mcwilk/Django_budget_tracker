import os
import sys
from pathlib import Path

import django
from django.contrib.auth import get_user_model

sys.path.append(str(Path(__file__).parent.parent))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'budget_project.settings')
django.setup()

user = get_user_model()

admin_user = os.getenv("DJANGO_SUPERUSER_USERNAME")
admin_email = os.getenv("DJANGO_SUPERUSER_EMAIL")
admin_passwd = os.getenv("DJANGO_SUPERUSER_PASSWORD")
generic_user = os.getenv("DJANGO_GENERIC_USERNAME")
generic_email = os.getenv("DJANGO_GENERIC_EMAIL")
generic_passwd = os.getenv("DJANGO_GENERIC_PASSWORD")
created_users = 0

def create_django_user(username: str, email: str, password: str, is_superuser: bool=False):
    global created_users

    if not user.objects.filter(username=username).exists():
        if is_superuser:
            user.objects.create_superuser(username, email, password)
            print("Superuser has been created!")
        else:
            user.objects.create_user(username, email, password)
            print("Generic user has been created!")

        created_users += 1


create_django_user(admin_user, admin_email, admin_passwd, is_superuser=True)
create_django_user(generic_user, generic_email, generic_passwd)

if created_users == 0:
    print(f"All necessary users already exist!")