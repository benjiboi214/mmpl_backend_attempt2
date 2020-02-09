#!/bin/bash

./build_scripts/local/stop.sh
./build_scripts/local/clean.sh
./build_scripts/local/unit_test.sh
./build_scripts/local/build.sh
./build_scripts/local/run.sh
./build_scripts/local/func_test.sh
