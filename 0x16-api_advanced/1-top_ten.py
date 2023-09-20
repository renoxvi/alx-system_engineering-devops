#!/usr/bin/python3
"""
Query Reddit API for titles of top ten posts of a given subreddit
"""
import requests

def top_ten(subreddit):
    """
        return top ten titles for a given subreddit
        return None if invalid subreddit given
    """
    # Set user agent
    headers = {'User-Agent': 'My User Agent 1.0'}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    response = requests.get(url, headers=headers).json()
    top_ten = response.get('data', {}).get('children', [])

    if not top_ten:
        print(None)

    for post in top_ten:
        print(post.get('data').get('title'))

if __name__ == "__main__":
    subreddit = input("Enter the subreddit: ")
    top_ten(subreddit)
