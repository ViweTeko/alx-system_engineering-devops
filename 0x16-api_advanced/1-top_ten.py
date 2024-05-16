#!/usr/bin/python3
"""A function that queries the Reddit API and
returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "My user agent 1.0"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        children = response.json().get('data').get('children')
        for a in range(10):
            print(children[a].get('data').get('title'))
        else:
            print('None')
    except Exception:
        print('None')
