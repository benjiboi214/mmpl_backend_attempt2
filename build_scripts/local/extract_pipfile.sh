#!/bin/bash
rm Pipfile

jq -r '.default
        | to_entries[]
        | .key + .value.version' \
    Pipfile.lock > requirements.txt

jq -r '.develop
        | to_entries[]
        | .key + .value.version' \
    Pipfile.lock > requirements-dev.txt

pipenv install -r requirements.txt
pipenv install --dev -r requirements-dev.txt
pipenv lock -r

rm requirements.txt requirements-dev.txt