#!/usr/bin/python3
""" queries the Reddit API and returns the number of subscribers. """
import requests


def number_of_subscribers(subreddit):
    """ returns the number of subscribers for a given subreddit """

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'MyPythonScript/1.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        subscribers = response.json().get('data').get('subscribers')
        return subscribers if subscribers else 0

    return 0
