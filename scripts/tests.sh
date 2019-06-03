#!/usr/bin/env bash
mkdir dependencies
cd dependencies
git clone https://github.com/foosel/OctoPrint.git
cd OctoPrint
virtualenv venv
source ./venv/bin/activate
pip install --upgrade pip
pip install -e .[develop,plugins]
cd ./ && nosetests
