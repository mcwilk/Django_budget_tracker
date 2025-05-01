#!/bin/bash

set -eu
# Optional: debugging
# set -x

echo "Running entrypoint script..."
echo "Waiting for Postgres..."

until nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do
    sleep 1
done

echo "Postgres is up!"

python budget/manage.py makemigrations
python budget/manage.py migrate

if [[ "$DJANGO_ENV" == "dev" || "$DJANGO_ENV" == "test" ]]; then
  echo "Creating django users..."
  python budget/budget_scripts/create_users.py

  echo "Loading demo data..."
  python budget/manage.py loaddata budget/budget_app/data/initial_data.json
fi

python budget/manage.py runserver 0.0.0.0:8000