#!/usr/bin/python3
'''This function is print response with id of the site-web'''

from urllib import request, error
import sys


if __name__ == '__main__':
    try:
        with request.urlopen(sys.argv[1]) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except error.HTTPError as e:
        print('Error code: {}'.format(e.code))
