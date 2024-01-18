#!/usr/bin/python3
""" queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    # a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'MyBot/1.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json().get('data', {})
        subscribers = data.get('subscribers', 0)
        return subscribers
    else:
        return 0
