#!/usr/bin/python3
""" This script queries Reddit API recursively"""
import requests


def count_words(subreddit, word_list, after="", word_dict={}):
    """This function queries Reddit API and counts given keywords"""
    if not word_dict:
        for word in word_list:
            if word.lower() not in word_dict:
                word_dict[word.lower()] = 0
    if after is None:
        new_dict = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))
        for word in new_dict:
            if word[1]:
                print(f'{word[0]}: {word[1]}')
        return None
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    header = {'User-Agent': 'redquery'}
    parameters = {'limit': 100, 'after': after}
    response = requests.get(url, headers=header, params=parameters,
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    try:
        hot = response.json()['data']['children']
        af = response.json()['data']['after']
        for post in hot:
            title = post['data']['title']
            lower = [word.lower() for word in title.split(' ')]
            for word in word_dict.keys():
                word_dict[word] += lower.count(word)
    except Exception:
        return None

    count_words(subreddit, word_list, af, word_dict)
