## Run flake8 ##
# Requires:
# - FLAKE8_REPORT_OUTPUT  ## eg: /app/flake8.xml
# - FLAKE8_CONFIG_FILE    ## eg: setup.cfg

echo "#### Running Flake8 ####"
docker-compose -f local.yml run django flake8 \
  --format junit-xml \
  --output-file=${FLAKE8_REPORT_OUTPUT:-"/app/flake8.xml"} \
  --config=${FLAKE8_CONFIG_FILE:-"setup.cfg"} .


## Run PyTest ##
# Requires:
# - PYTEST_REPORT_OUTPUT  ## eg: /app/pytest.xml

echo "#### Running PyTest ####"
docker-compose -f local.yml run django pytest \
  --junitxml=${PYTEST_REPORT_OUTPUT:-"/app/pytest.xml"}


## Run Coverage ##
# Requires:
# - COVERAGE_REPORT_OUTPUT  ## eg: /app/coverage.xml

echo "#### Running Coverage ####"
docker-compose -f local.yml run django coverage \
  run -m pytest
docker-compose -f local.yml run django coverage \
  xml -o ${COVERAGE_REPORT_OUTPUT:-"/app/coverage.xml"}