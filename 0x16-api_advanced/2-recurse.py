#!/usr/bin/python3
"""recursive function that queries the Reddit API"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """returns a list containing the titles of all hot articles of subreddit"""

    url = 'http://reddit.com/r/{}/hot.json?after={}'.format(subreddit,
                                                            after)
    headers = {'User-agent': 'alptem'}
    res = requests.get(url, headers=headers)

    if res.status_code == 200:
        top = res.json()
        key = top['data']['after']
        parent = top['data']['children']

        for obj in parent:
            hot_list.append(obj['data']['title'])

        if key is not None:
            recurse(subreddit, hot_list, key)
        return hot_list
    else:
        return None
