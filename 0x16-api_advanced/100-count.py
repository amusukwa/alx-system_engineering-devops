#!/usr/bin/python3
import requests

def count_words(subreddit, word_list, after=None, count_dict=None):
    """
    Recursive function that queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords.
    """
    if count_dict is None:
        count_dict = {}

    if after is None:
        url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    else:
        url = f'https://www.reddit.com/r/{subreddit}/hot.json?after={after}'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {})
        children = data.get('children', [])

        for post in children:
            title = post.get('data', {}).get('title', '').lower()
            for word in word_list:
                word = word.lower()
                if word in title:
                    count_dict[word] = count_dict.get(word, 0) + 1

        after = data.get('after')
        if after:
            count_words(subreddit, word_list, after, count_dict)

    sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
    
    for word, count in sorted_counts:
        print(f'{word}: {count}')


if __name__ == '__main__':
    subreddit = input("Enter subreddit: ")
    word_list = input("Enter space-separated keywords: ").split()
    
    count_words(subreddit, word_list)

