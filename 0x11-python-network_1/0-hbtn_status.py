#!/usr/bin/python3

import urllib.request
'''This function is for print status of an site-web'''


if __name__ == '__main__':
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as res:
        html = res.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf8 content: {}'.format(html.decode('utf-8')))
