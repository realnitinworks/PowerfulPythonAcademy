class BodyOfText:
    def __init__(self, text):
        if text == '':
            raise ValueError
        self.text = text
    def num_paragraphs(self):
        if self.text == '':
            return 0
        return 1 + self.text.count('\n\n')

class Paragraph:
    def __init__(self, text):
        self.text = text
    def num_sentences(self):
        if self.text == '':
            return 0
        return 1 + self.text.replace('\n', ' ').count('. ')
    
# Part of Powerful Python Academy. Copyright MigrateUp LLC. All rights reserved.
