#!/bin/bash

sam deploy -t build_config/pipeline/test_traffic_lambda/template.yaml --s3-bucket systemiphus-lambda-artifact-storage --capabilities  CAPABILITY_NAMED_IAM --stack-name mmpl-backend