#!/usr/bin/env bash
npm i -g gitinspector
virtualenv -p /usr/bin/python3.6 ._venv
source ./._venv/bin/activate
pip install -r requirements.txt
mkdir -p git-reports
mkdir -p git-repos
