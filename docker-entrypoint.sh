#!/bin/bash

set -e

echo "Waiting for Postgres..."

until nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do
    sleep 1
done

echo "Postgres is up!"

python budget/manage.py makemigrations
python budget/manage.py migrate

#if [[ "$DJANGO_ENV" == "dev" || "$DJANGO_ENV" == "test" ]]; then
#  echo "Creating django superuser..."
#  python budget_project/scripts/create_superuser.py
#fi

python budget/manage.py runserver 0.0.0.0:8000