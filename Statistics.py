"""
class holding the calculated stats about an Articles_From_Source object
"""

class Statistics:
    def __init__(self):
        self.words_per_sentence = None
        self.readability = None
        self.appearances_of_trump = None
        self.appearances_of_pancakes = None
        self.statistics_names = ["Readability", "Words per sentence", "Appearances of Trump vs. Pancakes"]
