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

exec bash