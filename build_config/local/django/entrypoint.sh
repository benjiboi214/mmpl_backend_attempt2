#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset



# N.B. If only .env files supported variable expansion...
# export CELERY_BROKER_URL="$a{REDIS_URL}"


if [ -z "${DJANGO_DB_USER}" ]; then
    base_postgres_image_default_user='postgres'
    export DJANGO_DB_USER="${base_postgres_image_default_user}"
fi
export DATABASE_URL="postgres://${DJANGO_DB_USER}:${DJANGO_DB_PASS}@${DJANGO_DB_HOST}:${DJANGO_DB_PORT}/${DJANGO_DB_NAME}"

postgres_ready() {
python << END
import sys
import psycopg2
try:
    psycopg2.connect(
        dbname="${DJANGO_DB_NAME}",
        user="${DJANGO_DB_USER}",
        password=${DJANGO_DB_PASS},
        host="${DJANGO_DB_HOST}",
        port="${DJANGO_DB_PORT}",
    )
except psycopg2.OperationalError as e:
    print("ERROR!")
    print(e)
    sys.exit(-1)
sys.exit(0)
END
}
until postgres_ready; do
  >&2 echo 'Waiting for PostgreSQL to become available...'
  sleep 1
done
>&2 echo 'PostgreSQL is available'

exec "$@"