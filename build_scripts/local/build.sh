#/bin/bash

#!/bin/bash

if [ "$1" == "" ]; then
    echo "Error: Unsupported command. Select from \"test\", \"prod\""
elif [ "$1" == "test" ]; then
    docker build -f docker/test/Dockerfile .
elif [ "$1" == "prod" ]; then
    docker build -f docker/prod/Dockerfile .
else
    echo "Error: Unsupported command. Select from XXX"
fi


