## Helper script for making migrations
docker-compose -f local.yml run --rm django python manage.py makemigrations