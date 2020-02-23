#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset

# pipenv run python /app/manage.py collectstatic --noinput
pipenv run gunicorn config.wsgi --bind 0.0.0.0:$DJANGO_INTERNAL_PORT_NUM
