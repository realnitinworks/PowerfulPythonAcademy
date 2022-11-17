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
        # The code below uses one possible approach: iteratively
        # search for sentence endings, and check whether that sentence
        # ends with a "word" that ends with a period.
        #
        # Another possible approach is to "tokenize" the input text
        # into a stream of word-like chunks, checking whether each
        # chunk (a) ends with a punctuation mark, and/or (b) is one of
        # the recognized "words" ending with a period.
        #
        # Both of these approaches have a flaw, in that they will not
        # correctly recognize a sentence that ends with a "word" that
        # ends with a period; it'll mistakenly merge that sentence and
        # the following one as a single sentence. To solve that
        # semantic issue would probably require a higher-level
        # NLP/grammar analysis.
        # 
        # This actually points out something interesting. Because real
        # software is rarely "perfect". You're continually developing
        # it to a standard of "good enough". And what is "good enough"
        # usually shifts over time, as new requirements come in (and
        # as existing requirements become better understood).
        #
        # And in practice, the way you formally define "good enough"
        # is through the tests.
        #
        # The current set of tests don't require num_sentences() to
        # recognize a sentence that ends with "a.m.", for
        # example. That's essentially defining the "good enough"
        # standard in code (the unit test code). Which conveniently
        # means it's in version control.
        # 
        # In the future, if we do need our code to handle this
        # distinction - and we decide we need it enough that it
        # justifies the substantial development effort - we start by
        # simply adding a test for that. And then modify our code to
        # make that new test pass (as well as all existing tests).
        #
        # That kind of event means our standard of "good enough"
        # changed. (Or our understanding of it changed.) And in real
        # software development, that kind of change happens over and
        # over and over...
        # 
        # Until the program is abandoned for another one, where the
        # cycle starts anew. Forever, until the end of time.
        
        if self.text == '':
            return 0
        end_of_sentence_regex = re.compile(r'[\.!?][ \n]+')
        # Notice the regex above currently doesn't recognize tab characters as whitespace. Again: the "good enough" standard.
        count = 1
        start = 0
        while True:
            end_of_sentence = end_of_sentence_regex.search(self.text, start)
            if end_of_sentence is None:
                break # end of self.text
            end = end_of_sentence.start() + 1
            tail = self.text[start:end]
            if not ends_with_abbreviation(tail):
                count += 1
            start = end + 1
        return count

# Part of Powerful Python Academy. Copyright MigrateUp LLC. All rights reserved.
