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

python manage.py makemigrations
python manage.py migrate

if [[ "$DJANGO_ENV" == "dev" || "$DJANGO_ENV" == "test" ]]; then
  echo "Creating django users..."
  python budget_scripts/create_users.py

  echo "Loading demo data..."
  python manage.py loaddata budget_app/data/initial_data.json
fi

python manage.py runserver 0.0.0.0:8000