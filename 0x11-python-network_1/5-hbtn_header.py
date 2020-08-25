#!/usr/bin/python3
'''This function is print response with id of the site-web'''
import requests
import sys


if __name__ == '__main__':
    rqt = requests.get(sys.argv[1])
    print(rqt.headers.get('X-Request-Id'))
