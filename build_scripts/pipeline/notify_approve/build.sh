#!/bin/bash

export BASE_DIR="build_config/pipeline/notify_approve"
export FUNC_DIR="$BASE_DIR/function"

sam build -u \
  -s $BASE_DIR \
  -t $BASE_DIR/template.yaml
