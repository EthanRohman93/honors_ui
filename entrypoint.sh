#!/bin/bash

# Exit on error
set -e

# Wait for the database to start
# Uncomment the lines below if you need to wait for a database to be ready
# echo "Waiting for database to start..."
# while ! nc -z dbhost 5432; do
#   sleep 0.1
# done
# echo "Database started"

# Apply database migrations
echo "Applying database migrations..."
python manage.py makemigrations
python manage.py migrate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start Gunicorn
exec gunicorn --bind 0.0.0.0:8000 honors_ui.wsgi:application

