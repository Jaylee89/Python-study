#!/usr/bin/env bash

set -e

#linux
python3 -m venv venv
# pip3 install --upgrade pip
# source venv/bin/activate

#win
python3 -m venv venv
cd venv\Scripts
python3 -m pip install -r requirements.txt
activate.bat
cd ../..