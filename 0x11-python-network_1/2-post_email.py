#!/usr/bin/python3
'''This function is print response with id of the site-web'''
from urllib import request, parse
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    email = parse.urlencode({'email' : sys.argv[2]})
    email = email.encode('ascii')
    request = request.Request(url, email)
    with request.urlopen(request) as response:
        the_page = response.read()
        print(the_page.decode('utf-8'))
