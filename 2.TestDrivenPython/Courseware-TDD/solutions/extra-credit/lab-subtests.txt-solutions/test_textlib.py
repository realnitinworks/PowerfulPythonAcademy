import unittest
from textlib import BodyOfText, Paragraph

class TestBodyOfText(unittest.TestCase):
    def test_empty_story(self):
        with self.assertRaises(ValueError):
            BodyOfText('')
    def test_single_paragraph(self):
        bot = BodyOfText('Hello, world.')
        self.assertEqual(1, bot.num_paragraphs())
    def test_several_paragraphs(self):
        bot = BodyOfText('''This is a longer story.

Once upon a time, there was a princess in a castle.

She grew up to be a famous dancer.''')
        self.assertEqual(3, bot.num_paragraphs())

class TestParagraph(unittest.TestCase):
    def test_main(self):
        # Notice that I've collapsed all tests into into a single test
        # method.  This is just so I can put all tests into a single
        # set of subtests. Keeping the separate test methods wuld also
        # be a fine decision; it would make the code more repetitive,
        # but also give more informative error message, and may just
        # "feel" more natural.
        # 
        # But really, both are fine. The only wrong way to write tests
        # is to not write them at all!
        testdata = [
            (0, ''),
            (1, 'This is a paragraph with one sentence.'),
            (3, 'This is a paragraph. It has several sentences.\nThree, in fact.'),
            (1, 'My favorite website is docs.python.org, with reddit.com a close second.'),
            (1, "I bought a basket of fruit for Mrs. Smith's birthday."),
            (1, 'I will arrive between 6 a.m. and 7 a.m.'),
            (1, 'Your total is $10.43.'),
            (3, 'Yay! We made it. High five!'),
            (2, "Did you tell Mr. Burke yesterday? We're bringing the birthday cake tomorrow."),
        ]
        for count, text in testdata:
            with self.subTest(count=count, text=text):
                para = Paragraph(text)
                self.assertEqual(count, para.num_sentences())
                
        
# Part of Powerful Python Academy. Copyright MigrateUp LLC. All rights reserved.
