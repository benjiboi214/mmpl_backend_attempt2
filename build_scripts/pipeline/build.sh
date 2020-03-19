#!/bin/bash

export BASE_DIR="build_config/pipeline/test_traffic"
export FUNC_DIR="$BASE_DIR/function"

if [ "$1" == "full" ]; then
    echo "Downloading headless chrome binaries."
    mkdir -p $FUNC_DIR/bin/

    # Get chromedriver
    curl -SL https://chromedriver.storage.googleapis.com/2.32/chromedriver_linux64.zip > $FUNC_DIR/chromedriver.zip
    unzip -o $FUNC_DIR/chromedriver.zip -d $FUNC_DIR/bin/

    # Get Headless-chrome
    curl -SL https://github.com/adieuadieu/serverless-chrome/releases/download/v1.0.0-29/stable-headless-chromium-amazonlinux-2017-03.zip > $FUNC_DIR/headless-chromium.zip
    unzip -o $FUNC_DIR/headless-chromium.zip -d $FUNC_DIR/bin/

    # Clean
    rm $FUNC_DIR/headless-chromium.zip $FUNC_DIR/chromedriver.zip
else
    echo "Continuing without downloading fresh binaries."
fi

cp functional_tests.py $FUNC_DIR/src/functional_tests.py

sam build -u \
  -s $BASE_DIR \
  -t $BASE_DIR/template.yaml

rm $FUNC_DIR/src/functional_tests.py