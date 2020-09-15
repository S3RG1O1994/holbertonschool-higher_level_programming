#!/usr/bin/python3
'''This function is for print status of an site-web'''
import requests


if __name__ == '__main__':
    rqt = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(rqt.text)))
    print('\t- content: {}'.format(rqt.text))
