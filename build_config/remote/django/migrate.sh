#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset

pipenv run python /app/manage.py migrate