#!/usr/bin/python3
'''This function is print response with id of the site-web'''
import requests
import sys

if __name__ == '__main__':
    email = {'email': sys.argv[2]}
    rqt = requests.post(sys.argv[1], email)
    print(rqt.text)
