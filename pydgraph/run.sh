#!/bin/bash

CWD=`pwd`
echo ${CWD}
export PYTHONPATH=${CWD}

python app/main.py