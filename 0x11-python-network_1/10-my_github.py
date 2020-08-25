#!/usr/bin/python3
'''This function is print response with id of the site-web'''
from requests import get, auth
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    rqt = get('https://api.github.com/user', auth=auth.HTTPBasicAuth(username, password))
    print(rqt.json().get('id'))
