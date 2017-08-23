#!/usr/bin/env python

import requests
from requests.auth import AuthBase
import creds

code = 'PUT_CODE_HERE'

url='https://api.home.nest.com/oauth2/access_token'

data={
    'client_id':creds.product_id,
    'client_secret':creds.product_secret,
    'code':code,
    'grant_type':'authorization_code',
}

r = requests.post(url,data=data)

print r.text

