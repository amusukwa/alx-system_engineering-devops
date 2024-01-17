#!/usr/bin/python3
"""
2-recursive
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursive function to get titles of all hot articles in a subreddit."""
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {})
        children = data.get('children', [])
        after = data.get('after')

        for child in children:
            title = child.get('data', {}).get('title')
            if title:
                hot_list.append(title)

        if after:
            recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None


if __name__ == "__main__":
    subreddit = input("Enter subreddit: ")
    result = recurse(subreddit)
