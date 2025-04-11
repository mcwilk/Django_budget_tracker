#/bin/bash
USER_NAME="django_user"
USER_PASSWD="django_user_passwd123"

# Create user and add to sudo
if [ -n "$USER_NAME" ] && [ -n "$USER_PASSWD" ]; then
  useradd -m "$USER_NAME"
  echo "$USER_NAME:$USER_PASSWD" | chpasswd
  adduser "$USER_NAME" sudo
fi