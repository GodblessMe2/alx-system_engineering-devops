#!/usr/bin/python3
"""queries the Reddit API and prints the titles of the first 10 hot posts"""
import requests


def top_ten(subreddit):
    """Get the top 10 hot posts from the url given"""

    url = 'http://reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-agent': 'alptem'}
    res = requests.get(url, headers=headers)

    if res.status_code == 200:
        topTen = res.json()
        for i in range(10):
            print(topTen['data']['children'][i]['data']['title'])
    else:
        return print('None')
