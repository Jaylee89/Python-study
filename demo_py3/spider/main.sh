#!/bin/bash

set -e

$(dirname $0)/venv/bin/python3 $(dirname $0)/app.py "$@"