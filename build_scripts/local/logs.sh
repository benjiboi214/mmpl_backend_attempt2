#!/bin/bash

docker logs $(docker ps -a | awk '{print $1}' | awk 'NR==2')