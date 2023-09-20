#!/usr/bin/python3
""" Function that queries the Reddit API """
import requests

def number_of_subscribers(subreddit):
    """  Args:
        subreddit: subreddit name
    Returns:
        number of subscribers to the subreddit,
        or 0 if subreddit requested is invalid"""
    headers = {'User-Agent': 'xica369'}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    return 0

if __name__ == "__main__":
    subreddit = input("Enter the subreddit: ")
    subscribers = number_of_subscribers(subreddit)
    print(f"Number of subscribers to the subreddit: {subscribers}")
