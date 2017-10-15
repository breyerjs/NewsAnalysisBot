"""
Class representing a selection of articles from a source at a given time
"""
from Statistics import Statistics

class Articles_From_Source:
    def __init__(self, source):
        self.articles = []
        self.titles = []
        self.source = source
        # These are filled in by Analyzer.py
        self.statistics = Statistics()

    def add_article(self, article_json):
        """ todo just the article text """
        self.articles.append(article)
        """ todo just the title """
        self.titles.append(article)

    def get_articles(self):
        return self.articles
