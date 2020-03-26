#!/bin/bash

#WIP DOES NOT WORK

export BASE_DIR="build_config/pipeline/test_traffic"
export PWD

sam local invoke \
    --template-file $BASE_DIR/template.yaml \
    --env-vars $BASE_DIR/env.json 