#!/bin/bash

. .env.test

echo "#### Running PyTest ####"
pipenv run pytest ./api \
  -c $PYTEST_UNIT_CONFIG_PATH \
  --cov=api \
  --cov-report term-missing

echo "#### Running Flake8 ####"
pipenv run flake8 \
  --config=$FLAKE8_CONFIG_PATH .
