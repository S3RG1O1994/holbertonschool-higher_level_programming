#!/usr/bin/python3
'''This function is print response with id of the site-web'''
import requests
import sys

if __name__ == '__main__':
    rqt = requests.get(sys.argv[1])
    if rqt.status_code < 400:
        print(rqt.text)
    else:
        print('Error code:', rqt.status_code)
