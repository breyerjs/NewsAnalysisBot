"""
Class representing a selection of articles from a source at a given time
"""
from Statistics import Statistics

class Articles_From_Source:
    def __init__(self, source_name):
        self.articles = []
        self.source_name = source_name
        # These are filled in by Analyzer.py
        self.statistics = Statistics()
        self.tweets = []

    def add_article(self, article_json):
        clean_body = self.clean_article_body(article_json["body"])
        self.articles.append(clean_body)

    def get_articles(self):
        return self.articles

    def clean_article_body(self, body):
        body = body.replace('\n', ' ')
        print(body)
        return body
