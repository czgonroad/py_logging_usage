#!/usr/bin/env bash


_CUR_DIR="$(pwd)"
_TESTS_HOME="./tests"
_PYTEST_CACHE="./.pytest_cache"
_PROJECT_HOME="$_CUR_DIR/logginglib_project"

py.test --verbose "$_TESTS_HOME"
#pylint   --rcfile="./.pylintrc"    "$_PROJECT_HOME"




