#!/bin/bash

echo "#### Running PyTest ####"
pipenv run pytest ./api \
  -c $PYTEST_UNIT_CONFIG_PATH \
  --junitxml=$PYTEST_UNIT_REPORT_PATH \
  
echo "#### Running Coverage ####"
pipenv run pytest --cov=api ./api \
  -c $PYTEST_UNIT_CONFIG_PATH \
  --junitxml=$COVERAGE_REPORT_PATH 

echo "#### Running Flake8 ####"
pipenv run flake8 \
  --format junit-xml \
  --output-file=$FLAKE8_REPORT_PATH \
  --config=$FLAKE8_CONFIG_PATH .
