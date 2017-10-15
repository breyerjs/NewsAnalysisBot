"""
The Director coordinates the publication schedule and manages all of the other classes
This is the "Main" class
"""
from Paper_Boy import Paper_Boy
from Analyzer import Analyzer

class Director:
    def daily_news(self):
        paper_bundle = Paper_Boy().get_the_paper()
        Analyzer(paper_bundle).fill_stats()

        return paper_bundle

if __name__ == '__main__':
    d = Director()
    news = d.daily_news()
    for articles_from_source in news:
        print("================")
        print(articles_from_source.source_name)
        print(articles_from_source.statistics.avg_word_count)
        print(articles_from_source.statistics.readability)
