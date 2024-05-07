#!/usr/bin/python3
""" This script contains function top_ten"""
from sys import argv
import requests

def top_ten(subreddit):
    """Returns top ten posts for subreddit"""
    user = {"User-Agent": "Lizzie"}
    url = requests.get('https://www.reddit.com/r/{}/hot/.json?limit=10'
                       .format(subreddit), headers=user).json()
    try:
        for post in url.get('data').get('children'):
            print(post.get('data').get('title'))
    except Exception:
        print(None)


if __name__ == "__main__":
    top_ten(argv[1])
