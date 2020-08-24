#!/usr/bin/python3
'''This function is print response with id of the site-web'''
from urllib import request, parse
import sys


if __name__ == '__main__':
    email = parse.urlencode({'email': sys.argv[2]})
    email = email.encode('ascii')
    request = request.Request(sys.argv[1], email)
    with request.urlopen(request) as response:
        body = response.read()
        print(body.decode('utf-8'))
