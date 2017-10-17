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

    """ This is the feature event. Fills the given object with all of the stats available. """
    def fill_stats(self):
        for articles_from_source in self.list_of_articles_from_source:
            articles_from_source.statistics.words_per_sentence = self.get_avg_words_per_sentence(articles_from_source)
            articles_from_source.statistics.readability = self.get_readability_score(articles_from_source)

    """ Below here, methods for getting the various stats """
    def get_avg_words_per_sentence(self, articles_from_source):
        tokenized_words = articles_from_source.get_tokenized_words()
        tokenized_sents = articles_from_source.get_tokenized_sents()
        return self._round(len(tokenized_words) / len(tokenized_sents))

    # Based on Flesch-kinkaid grade level
    def get_readability_score(self, articles_from_source):
        tokenized_words = articles_from_source.get_tokenized_words()
        tokenized_sents = articles_from_source.get_tokenized_sents()
        words_per_sent = len(tokenized_words) / len(tokenized_sents)
        syllables_per_word = self._get_syllables_per_word(tokenized_words)
        return (0.39*(words_per_sent)) + (11.8*(syllables_per_word)) - 15.59

    """ Private helpers """

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
