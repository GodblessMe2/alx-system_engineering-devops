#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers of subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Get the number of the subscribers"""

    url = 'http://reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'user-agent': 'alptem'}
    res = requests.get(url, headers=headers)

    if res.status_code == 200:
        subscribers_num = res.json().get('data').get('subscribers')
        return subscribers_num
    else:
        return 0
