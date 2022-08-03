import os
import random
import json
from pathlib import Path
import tweepy
import csv

ROOT = Path(__file__).resolve().parents[0]


def get_tweet(tweets_file, excluded_tweets=None):
    """Get tweet to post from CSV file"""

    with open(tweets_file) as csvfile:
        reader = csv.DictReader(csvfile)
        possible_tweets = [row["tweet"] for row in reader]

    if excluded_tweets:
        recent_tweets = [status_object.text for status_object in excluded_tweets]
        possible_tweets = [tweet for tweet in possible_tweets if tweet not in recent_tweets]

    selected_tweet = random.choice(possible_tweets)

    return selected_tweet


def lambda_handler(event, context):
    print("Get credentials")
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    print("Authenticate")
    client = tweepy.Client(
                       consumer_key=consumer_key,
                       consumer_secret=consumer_secret,
                       access_token=access_token,
                       access_token_secret=access_token_secret
                    )

    print("Get tweet from csv file")
    tweets_file = ROOT / "tweets.csv"
    tweet = get_tweet(tweets_file)
    print(f"Post tweet: {tweet}") 
    client.create_tweet(text=tweet, user_auth=True)

    return {"statusCode": 200, "tweet": tweet}
