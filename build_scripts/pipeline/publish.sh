#!/bin/bash

sam deploy \
    --s3-bucket systemiphus-lambda-artifact-storage \
    --capabilities  CAPABILITY_NAMED_IAM \
    --stack-name mmpl-backend
