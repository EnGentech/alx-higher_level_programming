#!/usr/bin/python3
"""Get the first 10 commit messages"""

import requests
from sys import argv

if __name__ == '__main__':
    owner = argv[2]
    repo = argv[1]
    url = 'http://api.github.com/repos/{}/{}/commits'.format(repo, owner)

    header = {
        'Accept': 'application/vnd.github+json'
    }

    content = requests.get(url, headers=header).json()

    count = 1
    for x in content:
        print('{}: {}'.format(x['sha'], x['author name']))
        count += 1
        if count == 10:
            break

# Coded by EnGentech
