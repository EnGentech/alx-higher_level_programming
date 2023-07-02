#!/usr/bin/python3
"""Get the first 10 commit messages"""

import requests
from sys import argv

if __name__ == '__main__':
    owner = argv[2]
    repo = argv[1]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(repo, owner)

    header = {
        'Accept': 'application/vnd.github.v3+json'
    }

    content = requests.get(url, headers=header).json()

    for x in content[:10]:
        print('{}: {}'.format(x.get('sha'), x.get('commit').get('author').get('name')))

# Coded by EnGentech
