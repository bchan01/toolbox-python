#!/bin/bash
echo "building  ..."

# downloand dependencies in virtualenv
pip install -q virtualenv
virtualenv my_env
source my_env/bin/activate
pip install -r requirements.txt
