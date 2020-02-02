#/bin/bash

docker stop $(docker ps -a | awk '{print $1}' | awk 'NR==2')