#/bin/bash

echo "#### Running PyTest ####"
pipenv run pytest \
  --junitxml=${PYTEST_REPORT_OUTPUT:-"./pytest.xml"}

echo "#### Running Flake8 ####"
pipenv run flake8 \
  --format junit-xml \
  --output-file=${FLAKE8_REPORT_OUTPUT:-"./flake8.xml"} \
  --config=${FLAKE8_CONFIG_FILE:-"setup.cfg"} .

echo "#### Running Coverage ####"
pipenv run coverage \
  run -m pytest
pipenv run coverage \
  xml -o ${COVERAGE_REPORT_OUTPUT:-"/coverage.xml"}