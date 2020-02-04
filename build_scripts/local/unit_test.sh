#/bin/bash

pipenv run pytest api/ \
  --junitxml=${PYTEST_REPORT_OUTPUT:-"./pytest.xml"}