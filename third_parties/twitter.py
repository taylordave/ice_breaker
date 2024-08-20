import os
from dotenv import load_dotenv
import tweepy
import requests

load_dotenv()

EDEN_TWITTER_GIST = os.getenv("EDEN_TWITTER_GIST")


def scrape_user_tweets(username, num_tweets=5, mock: bool = False):
    """
    Scrapes a Twitter user's original tweets (i.e., not retweets or replies) and returns them as a list of dictionaries.
    Each dictionary has three fields: "time_posted" (relative to now), "text", and "url".
    """
    tweet_list = []

    if mock:
        tweets_received = requests.get(EDEN_TWITTER_GIST, timeout=5).json()

    else:
        twitter_client = tweepy.Client(
            bearer_token=os.environ["TWITTER_BEARER_TOKEN"],
            consumer_key=os.environ["TWITTER_API_KEY"],
            consumer_secret=os.environ["TWITTER_API_KEY_SECRET"],
            access_token=os.environ["TWITTER_ACCESS_TOKEN"],
            access_token_secret=os.environ["TWITTER_ACCESS_TOKEN_SECRET"],
        )

        user_id = twitter_client.get_user(username=username).data.id
        tweets_received = twitter_client.get_users_tweets(
            id=user_id, max_results=num_tweets, exclude=["retweets", "replies"]
        )
        tweets_received = tweets_received.data

    for tweet in tweets_received:
        tweet_dict = {"text": tweet["text"], "url": f"https://twitter.com/{username}/status/{tweet['id']}"}
        tweet_list.append(tweet_dict)

    return tweet_list


if __name__ == "__main__":

    tweets = scrape_user_tweets(username="EdenEmarco177", mock=True)
    print(tweets)
