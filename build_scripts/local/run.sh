#!/bin/bash

source .env

EXT_HOST=$DJANGO_EXTERNAL_HOST_NAME
EXT_PORT=$DJANGO_EXTERNAL_PORT_NUM
INT_PORT=$DJANGO_INTERNAL_PORT_NUM
DOCKER_IMG=$(docker images | awk '{print $3}' | awk 'NR==2')

docker run -d \
  --env-file .env \
  -p $EXT_HOST:$EXT_PORT:$INT_PORT $DOCKER_IMG \
  /app/start.sh