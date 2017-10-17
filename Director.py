"""
The Director coordinates the publication schedule and manages all of the other classes
This is the "Main" class
"""
from Paper_Boy import Paper_Boy
from Analyzer import Analyzer
from Writer import Writer

class Director:
    def daily_news(self):
        # get all articles
        paper_bundle = Paper_Boy().get_the_paper()
        # add the statistics
        Analyzer(paper_bundle).fill_stats()
        # write tweets
        tweets = Writer(paper_bundle).write_all_tweets()

        return tweets

if __name__ == '__main__':
    d = Director()
    print(d.daily_news())
