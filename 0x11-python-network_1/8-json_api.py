#!/usr/bin/python3
'''This function is print response with id of the site-web'''
import requests
import sys

if __name__ == '__main__':
    letter = {'q': ''}
    try:
        letter['q'] = sys.argv[1]
    except:
        pass
    rqt = requests.post('http://0.0.0.0:5000/search_user', letter)
    try:
        result = rqt.json()
        if result:
            print('[{}] {}'.format(result.get('id'), result.get('name')))
        else:
            print('No result')
    except:
        print('Not a valid JSON')
