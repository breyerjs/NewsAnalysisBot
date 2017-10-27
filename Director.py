"""
The Director coordinates the publication schedule and manages all of the other classes
This is the "Main" class


TODO: Update the API call to search for the two topics rather than pull any-ol'
random articles
"""

from Paper_Boy import Paper_Boy
from Analyzer import Analyzer
from Writer import Writer
from Publisher import Publisher

class Director:
    def daily_news(self):
        # get all articles
        paper_bundle = Paper_Boy().get_the_paper()

        # add the statistics
        Analyzer(paper_bundle).fill_stats()

        # write tweets
        tweets = Writer(paper_bundle).write_all_tweets()

        # publish tweets
        publisher = Publisher()
        for tweet in tweets:
            publisher.post_tweet(tweet)

        return tweets

if __name__ == '__main__':
    d = Director()
    for tweet in d.daily_news():
        print(tweet)
