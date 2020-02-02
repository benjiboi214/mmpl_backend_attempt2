#/bin/bash

## Get rid of dead containers ##
docker ps -a | grep Exit | cut -d ' ' -f 1 | xargs docker rm || true

## Clean up dangling images ##
docker rmi -f $(docker images -f "dangling=true" -q) || trues