#!/usr/bin/python3
"""
1-top_ten
"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    url = f'https://www.reddit.com/[/r/:subreddit]/hot.json?limit=10'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(
        url,
        headers=headers,
        allow_redirects=False
    )

    if response.status_code == 200:
        try:
            data = response.json().get('data', {}).get('children', [])
            if data:
                for post in data:
                    print(post['data']['title'])
            else:
                print('No posts found.')
        except ValueError:
            print('Invalid JSON response.')
    else:
        print(None)


if __name__ == '__main__':
    subreddit = input('Enter subreddit: ')
    top_ten(subreddit)
