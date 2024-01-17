#!/usr/bin/python3
"""
This script queries Reddit API and returns subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Get the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: Number of subscribers if the subreddit is valid, 0 otherwise.
    """
    url = 'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'MyRedditBot/1.0'}

    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers)

        # Check if the response is successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Extract and return the number of subscribers
            return data['data']['subscribers']
        else:
            # Return 0 for invalid subreddits or other errors
            return 0

    except Exception as e:
        # Handle any exceptions and return 0
        print(f"An error occurred: {e}")
        return 0


if __name__ == "__main__":
    subreddit_name = "python"
    subscribers_count = number_of_subscribers(subreddit_name)
