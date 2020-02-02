#/bin/bash

source .env

docker run --env-file .env -d -p $DJANGO_EXTERNAL_HOST_NAME:$DJANGO_EXTERNAL_PORT_NUM:$DJANGO_INTERNAL_PORT_NUM $(docker images | awk '{print $3}' | awk 'NR==2') /app/start.sh