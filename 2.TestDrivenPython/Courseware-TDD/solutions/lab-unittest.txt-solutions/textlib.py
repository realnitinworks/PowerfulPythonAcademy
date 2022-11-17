class BodyOfText:
    def __init__(self, text):
        self.text = text
    def num_paragraphs(self):
        if self.text == '':
            return 0
        return 1 + self.text.count('\n\n')

# Part of Powerful Python Academy. Copyright MigrateUp LLC. All rights reserved.
