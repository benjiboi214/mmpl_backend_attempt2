#/bin/bash

pipenv run pytest \
  --junitxml=${PYTEST_REPORT_OUTPUT:-"./pytest.xml"}