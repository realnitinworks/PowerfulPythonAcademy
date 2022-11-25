import unittest
from textwrap import dedent

from textlib import BodyOfText, Paragraph


class TestBodyOfText(unittest.TestCase):
    def test_empty_story(self):
        with self.assertRaises(ValueError):
            body = BodyOfText("")

    def test_single_paragraph(self):
        body = BodyOfText("A string with no blank lines")
        self.assertEqual(1, body.num_paragraphs())
        self.assertEqual(["A string with no blank lines"], body.paragraphs())

    def test_several_paragraphs(self):
        text = """\
        First Para
                  
        Second Para

        Third Para
        """
        body = BodyOfText(dedent(text))
        self.assertEqual(3, body.num_paragraphs())
        self.assertEqual(["First Para", "Second Para", "Third Para"], body.paragraphs())

    def test_wordcounts(self):
        testitems = [
            {
                "text": "This is a sentence.",
                "counts": {"this": 1, "is": 1, "a": 1, "sentence": 1},
            },
            {
                "text": "Truth is beauty; beauty, truth.",
                "counts": {"truth": 2, "beauty": 2, "is": 1},
            },
            {
                "text": "I could finally SEE. But what I could see, remained a mystery.",
                "counts": {
                    "i": 2,
                    "could": 2,
                    "finally": 1,
                    "see": 2,
                    "but": 1,
                    "what": 1,
                    "remained": 1,
                    "a": 1,
                    "mystery": 1,
                },
            },
        ]

        for item in testitems:
            with self.subTest(**item):
                bot = BodyOfText(item["text"])
                self.assertEqual(item["counts"], bot.wordcounts())


class TestParagraph(unittest.TestCase):
    def test_empty_paragraph(self):
        para = Paragraph("")
        self.assertEqual(0, para.num_sentences())

    def test_invalid_paragraph_with_only_whitespaces(self):
        with self.assertRaises(ValueError):
            para = Paragraph("                 ")

    def test_invalid_paragraph_with_no_words_multiline_string(self):
        with self.assertRaises(ValueError):
            para = Paragraph(
                """\
                
                
            """
            )

    def test_single_sentence(self):
        para = Paragraph("A single sentence paragraph")
        self.assertEqual(1, para.num_sentences())

    def test_several_sentences(self):
        para = Paragraph(
            "First Sentence is first. Second Sentence is second. Third Sentence is third."
        )
        self.assertEqual(3, para.num_sentences())


# Part of Powerful Python Academy. Copyright MigrateUp LLC. All rights reserved.
