"""
    Class holding the information about a single tweet that the writer has constructed.
    This is a tweet about a single statistic
"""

class Tweet:
    def __init__(self, text, statistic_name):
        self.text = text
        self.statistic_name = statistic_name
