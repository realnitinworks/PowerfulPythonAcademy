from dataclasses import dataclass
from collections import Counter
import re


@dataclass
class Paragraph:
    text: str

    def __post_init__(self):
        if self.text == "":
            return
        if not self.text.strip():
            raise ValueError("text cannot be empty")

    def num_sentences(self):
        return len([s for s in self.text.split(". ") if s])


@dataclass
class BodyOfText:
    text: str

    def __post_init__(self):
        if not self.text:
            raise ValueError("text cannot be empty!")

    def _paragraphs(self):
        return (p for p in self.text.splitlines() if p)

    def num_paragraphs(self):
        return len(list(self._paragraphs()))

    def paragraphs(self):
        return list(self._paragraphs())

    def wordcounts(self):
        return Counter(word.lower() for word in re.split(r"[^\w]", self.text) if word)


# Part of Powerful Python Academy. Copyright MigrateUp LLC. All rights reserved.
