#!/usr/bin/env python

import requests
import arrow
from requests.auth import AuthBase
import creds
import json

base_url='https://developer-api.nest.com/devices/thermostats/'

class NestAuth(AuthBase):
    """Attaches HTTP Pizza Authentication to the given Request object."""
    def __init__(self, token):
        # setup any auth-related data here
        self.token = token

    def __call__(self, r):
        # modify and return the request
        r.headers={}
        r.headers['Content-Type'] = 'application/json'
        r.headers['Authorization'] = 'Bearer {}'.format(self.token)
        return r

def nest_post(url, data={}):
    if data:
        method = requests.put
    else:
        method = requests.get
    initial_response = method(
            url,
            auth=NestAuth(creds.access_token),
            data=data,
            allow_redirects=False
    )
    if initial_response.status_code == 307:
            initial_response = method(
                    initial_response.headers['Location'],
                    auth=NestAuth(creds.access_token),
                    data=data,
                    allow_redirects=False
            )
    return initial_response.json()

def get_devices():
    url = base_url[:-1]
    return nest_post(url)

def get_variable(var):
    url = base_url + creds.device + '/' + var
    return nest_post(url)

def set_variable(var, value):
    url = base_url + creds.device + '/' + var
    str_val = json.dumps({var:value})
    return nest_post(url, str_val)

def get_timeout():
    if get_variable('is_online') == True:
        if get_variable('has_fan') == True:
            return get_variable('fan_timeout')
    return False

