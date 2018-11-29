#!/usr/bin/env bash

set -e

source $(dirname $0)/venv/bin/activate
$(dirname $0)/venv/bin/python3 $(dirname $0)/app.py