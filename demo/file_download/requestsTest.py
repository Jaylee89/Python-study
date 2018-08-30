#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, sys, os, re, time


r = requests.get('https://api.github.com/user', auth=('Jaylee89', 'jal891012'))

print r.status_code

print r.headers['content-type']

print r.headers['content-range']

print r.encoding

print r.text

print r.json()

