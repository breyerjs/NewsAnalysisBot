"""
The Writer compiles all of the analysis for the different outlets,
pens the tweet. The Publisher can publish the writing.
"""

from Statistics import Statistics

class Writer:
    def __init__(self, list_of_articles_from_source):
        self.list_of_articles_from_source = list_of_articles_from_source
        self.statistics_names = Statistics().statistics_names
        self.list_of_sources = [arts_from_source.source_name for arts_from_source in list_of_articles_from_source]

    def write_all_tweets(self):
        """
            todo: add one Tweet() per statistic generated in Analyzer()
        """
        return [
            # self.write_avg_words_per_sent(),
            # self.write_readability(),
            self.write_appearances_of_trump_vs_pancakes()
        ]

    def write_avg_words_per_sent(self):
        text = "Avg words per sentence:\n"
        for arts_from_source in self.list_of_articles_from_source:
            text += "\n" + arts_from_source.source_name + ": "
            text += str(arts_from_source.statistics.words_per_sentence)
        return text

    def write_readability(self):
        text = "Grade-level estimate of writing:\n"
        for arts_from_source in self.list_of_articles_from_source:
            text += "\n" + arts_from_source.source_name + ": "
            text += str(arts_from_source.statistics.readability)
        return text

    def write_appearances_of_trump_vs_pancakes(self):
        text = "Appearances of the words 'Trump' / 'Pancakes'"
        for arts_from_source in self.list_of_articles_from_source:
            text += "\n" + arts_from_source.source_name + ": "
            text += str(arts_from_source.statistics.appearances_of_trump) + " / "
            text += str(arts_from_source.statistics.appearances_of_pancakes)
        return text
