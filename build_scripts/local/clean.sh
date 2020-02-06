#/bin/bash

. .env

## Get rid of dead containers ##
docker ps -a | grep Exit | cut -d ' ' -f 1 | xargs docker rm || true

## Clean up dangling images ##
docker rmi -f $(docker images -f "dangling=true" -q) || trues

## Clean up testing reports
rm $PYTEST_UNIT_REPORT_PATH
rm $PYTEST_FUNC_REPORT_PATH
rm $COVERAGE_REPORT_PATH
rm $FLAKE8_REPORT_PATH
rm $GECKO_LOG_PATH