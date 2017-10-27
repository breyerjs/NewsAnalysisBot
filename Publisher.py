"""
The Publisher class takes the tweets and publishes them to Twitter
"""
from Credentials import Credentials
import twitter

class Publisher:
    def __init__(self):
        self.credentials = Credentials()
        self.api = twitter.Api(consumer_key=self.credentials.twitter_consumer_key,
                  consumer_secret=self.credentials.twitter_consumer_secret,
                  access_token_key=self.credentials.twitter_access_token_key,
                  access_token_secret=self.credentials.twitter_access_token_secret)

    def post_tweet(self, text):
        status_posted = self.api.PostUpdate(text)
        return status_posted

if __name__ == '__main__':
    p = Publisher()
    p.post_tweet("Hello world!")
