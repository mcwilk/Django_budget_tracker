#!/bin/bash

set -eu
# Optional: debugging
# set -x

echo "Running entrypoint script..."
echo "Waiting for Postgres..."
# netcat tries to ping database with host:port
until nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do
    sleep 1
done
echo "Postgres is up!"

if [[ "$DJANGO_ENV" == "dev" || "$DJANGO_ENV" == "test" ]]; then
  python manage.py migrate
else
  echo "Skipping migrations when env not in (dev, test) - it needs to be run manually"
fi

if [[ "$DJANGO_ENV" == "dev" || "$DJANGO_ENV" == "test" || "$DJANGO_ENV" == "staging" ]]; then
  echo "Creating django users..."
  python budget_scripts/create_users.py
  echo "Loading demo data..."
  python manage.py loaddata budget_app/data/initial_data.json
fi

python manage.py runserver 0.0.0.0:8000