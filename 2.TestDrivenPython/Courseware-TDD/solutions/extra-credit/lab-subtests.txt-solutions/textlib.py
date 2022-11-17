import re

class BodyOfText:
    def __init__(self, text):
        if not self.text_is_valid(text):
            raise ValueError
        self.text = text
    def num_paragraphs(self):
        if self.text == '':
            return 0
        return 1 + self.text.count('\n\n')
    @staticmethod
    def text_is_valid(text):
        # There are several ways to do this. But the cleanest, most
        # readable, and most efficient is to simply use a regular
        # expression. This is basically saying: "if text consists of
        # nothing except whitespace characters (space, tab, newline,
        # etc.), then it's not valid."
        return not re.search(r'^\s*$', text)

_words_with_period = {
     'a.m.',
     'p.m.',
     'Mr.',
     'Mrs.',
     }
def ends_with_abbreviation(fragment):
    for word in _words_with_period:
        if fragment.endswith(word):
            return True
    return False

class Paragraph:
    def __init__(self, text):
        self.text = text
    def num_sentences(self):
        if self.text == '':
            return 0
        end_of_sentence_regex = re.compile(r'[\.!?][ \n]+')
        count = 1
        start = 0
        while True:
            end_of_sentence = end_of_sentence_regex.search(self.text, start)
            if end_of_sentence is None:
                break
            end = end_of_sentence.start() + 1
            tail = self.text[start:end]
            if not ends_with_abbreviation(tail):
                count += 1
            start = end + 1
        return count
        

# Part of Powerful Python Academy. Copyright MigrateUp LLC. All rights reserved.
