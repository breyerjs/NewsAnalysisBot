"""
Paper_Boy is a class that can fetch the text of news articles from various sources
He packages those into an Articles_From_Source object and returns them
"""

from eventregistry import *
from Articles_From_Source import Articles_From_Source
from Credentials import Credentials
from datetime import datetime, timedelta

class Paper_Boy:
    def __init__(self):
        self.URIS = {
            "Fox": "foxnews.com",
            "NYT": "nytimes.com",
            "Wash. Post": "washingtonpost.com",
            "BBC": "bbc.com",
            #"Vice News": "news.vice.com",
        }
        self.credentials = Credentials()

    def get_the_paper(self):
        paper_bundle = []
        for source in self.URIS:
            paper_bundle.append(self._query_articles(source))
        return paper_bundle

    def _query_articles(self, source):
        event_registry = EventRegistry(apiKey = self.credentials.event_registry_api_key)
        q = QueryArticlesIter(
            lang="eng",
            dateStart=datetime.now() - timedelta(5),
            sourceUri=event_registry.getNewsSourceUri(self.URIS[source]))
        articles = Articles_From_Source(source)
        for article in q.execQuery(event_registry, maxItems=1000):
            articles.add_article(article)
        return articles

if __name__ == '__main__':
    pb = Paper_Boy()
    arts = pb.get_the_paper()
    print(arts[0].get_articles())
