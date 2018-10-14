#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib3

APP_ID = '10673785'
API_KEY = 'uh1SnFZ2AvvCLcUxkR4VOkYk'
SECRET_KEY = 'PFxBMIfajiHGCtsG5NWuXWcwUhEGUvSu'

http=urllib3.PoolManager()
request=http.request(
    'GET',
    'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s' % (API_KEY, SECRET_KEY))
print(request.data)

# request=http.request(
#     'POST',
#     'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s' % (API_KEY, SECRET_KEY))
# print(request.data)