"""
Given an Articles_From_Source object, it can analyze those articles and return
a variety of relevant statistics

Possible stats (per article):
    - Word Count
    - # of distinct words
    - Sentence length
    - Readability / grade level: See Flesch-kinkaid + Fog Score
    - Syllables / word + words / sent
    - Rarest words used?
"""
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import cmudict

class Analyzer:
    def __init__(self, list_of_articles_from_source):
        self.list_of_articles_from_source = list_of_articles_from_source
        self.pronounciation_dict = cmudict.dict()

    """
    This is the feature event. Fills the given object with all of the stats available.
    """
    def fill_stats(self):
        for articles_from_source in self.list_of_articles_from_source:
            articles_from_source.statistics.avg_word_count = self.get_avg_word_count(articles_from_source)
            articles_from_source.statistics.readability = self.get_readability_score(articles_from_source)

    """
    Below here, methods for getting the various stats
    """
    def get_avg_word_count(self, articles_from_source):
        articles = articles_from_source.get_articles()
        total_length = sum([len(art.split()) for art in articles])
        num_articles = len(articles)
        avg = total_length / num_articles
        return self._round(avg)

    def get_readability_score(self, articles_from_source):
        tokenized_words = []
        tokenized_sentences = []
        for art in articles_from_source.get_articles():
            tokenized_words.extend(word_tokenize(art))
            tokenized_sentences.extend(sent_tokenize(art))
        return self._calc_flesch_kincaid_grade_level(tokenized_words, tokenized_sentences)

    """
    Private helpers
    """
    def _calc_flesch_kincaid_grade_level(self, tokenized_words, tokenized_sentences):
        words_per_sent = len(tokenized_words) / len(tokenized_sentences)
        syllables_per_word = self._get_syllables_per_word(tokenized_words)
        return (0.39*(words_per_sent)) + (11.8*(syllables_per_word)) - 15.59

    def _get_syllables_per_word(self, tokenized_words):
        total_syllables = sum([self._get_num_syllables_in_word(word.lower()) for word in tokenized_words])
        return total_syllables / len(tokenized_words)

    def _get_num_syllables_in_word(self, word):
        try:
            # take the first entry in the dict
            combined_from_dict = "".join(self.pronounciation_dict[word][0])
            syllables = len([char for char in combined_from_dict if char.isdigit()])
            return syllables

        except KeyError:
            return 0

    def _round(self, number, num_places=2):
        return round(number, num_places)

if __name__ == '__main__':
    article = "The Australian platypus is seemingly a hybrid of a mammal and reptilian creature"
    tokenized_words = word_tokenize(article)
    tokenized_sentences = sent_tokenize(article)

    a = Analyzer(None)
    print(a._calc_flesch_kincaid_grade_level(tokenized_words, tokenized_sentences))
