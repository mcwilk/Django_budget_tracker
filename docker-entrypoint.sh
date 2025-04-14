#!/bin/bash
#USER_NAME="django_user"
#USER_PASSWD="django_user_passwd123"

# Create user and add to sudo
#if [ -n "$USER_NAME" ] && [ -n "$USER_PASSWD" ]; then
#  useradd -m -s /bin/bash "$USER_NAME"
#  echo "$USER_NAME:$USER_PASSWD" | chpasswd
#  adduser "$USER_NAME" sudo
#fi

# Przełączenie na tego użytkownika
#export HOME=/home/$USER_NAME
#export USER=$USER_NAME
#exec su - "$USER_NAME"
pwd
ls
python budget/manage.py makemigrations
python budget/manage.py migrate

#if [[ "$DJANGO_ENV" == "dev" || "$DJANGO_ENV" == "test" ]]; then
#  echo "Creating django superuser..."
#  python budget/scripts/create_superuser.py
#fi

python budget/manage.py runserver

#exec bash