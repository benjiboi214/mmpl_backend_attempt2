#!/bin/bash

jq -r '.default
        | to_entries[]
        | .key + .value.version' \
    Pipfile.lock > requirements.txt

pipenv install -r requirements.txt
pipenv lock -r

rm requirements.txt