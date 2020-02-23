#!/bin/bash

if [ "$1" == "django" ]; then
    echo "Building Django Image"
    docker build -t $IMAGE_REPO_NAME:$IMAGE_TAG -f build_config/remote/django/Dockerfile .
    docker tag $IMAGE_REPO_NAME:$IMAGE_TAG $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/$IMAGE_REPO_NAME:$IMAGE_TAG      
    printf '{"ImageURI":"%s"}'  $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/$IMAGE_REPO_NAME:latest  > /imageDetail.json
elif [ "$1" == "traefik" ]; then
    echo "Building Traefik Image"
    docker build -t $IMAGE_REPO_NAME:$IMAGE_TAG -f build_config/remote/traefik/Dockerfile .
    docker tag $IMAGE_REPO_NAME:$IMAGE_TAG $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/$IMAGE_REPO_NAME:$IMAGE_TAG      
    printf '{"ImageURI":"%s"}'  $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/$IMAGE_REPO_NAME:latest  > /imageDetail.json
else
    echo "ERROR: Must specify which image to build."
fi
