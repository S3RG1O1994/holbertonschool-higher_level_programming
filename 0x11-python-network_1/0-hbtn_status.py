#!/usr/bin/python3
import urllib.request
'''This function is for print status of an site-web'''


if __name__ == '__main__':
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        the_page = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(the_page)))
        print('\t- content: {}'.format(the_page))
        print('\t- utf8 content: {}'.format(the_page.decode('utf-8')))
