#!/usr/bin/python3
""" queries the Reddit API and prints the titles of the first 10 hot posts """
import requests


def top_ten(subreddit):
    """ prints the titles of the first 10 hot posts listed """

    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'script/1.0'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json().get('data').get('children')
        if not data:
            return print("None")
        else:
            for post in data:
                print(post.get('data').get('title'))
    else:
        return print("None")
