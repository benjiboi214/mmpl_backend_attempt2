#!/bin/bash

if [ "$1" == "" ]; then
    echo "Error: Unsupported command. Select from \"create\" or \"remove\""
elif [ "$1" == "create" ]; then
    if [ "$2" == "" ]; then
        echo "Error: Must supply DB name as postional argument"
    else
        echo "Creating postgresql DB named \"$2\""
        createdb $2
        echo "Done"
    fi
elif [ "$1" == "remove" ]; then
    if [ "$2" == "" ]; then
        echo "Error: Must supply DB name as postional argument"
    else
        echo "Removing postgresql DB named \"$2\""
        dropdb $2
        echo "Done"
    fi
else
    echo "Error: Unsupported command. Select from \"create\" or \"remove\""
fi

# createuser -D -l -S -W mmpl_backend
# https://www.postgresql.org/docs/9.1/app-createuser.html

# Testing user creation
# mmpl_backend
# !m8#Tg!XQ77J2HtpV6FX


