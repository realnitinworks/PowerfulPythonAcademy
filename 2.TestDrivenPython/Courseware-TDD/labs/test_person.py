from person import Person
from unittest import TestCase


class TestPerson(TestCase):
    def test_main(self):
        guy = Person("John", "Doe")
        self.assertEqual("John", guy.first)
        self.assertEqual("Doe", guy.last)
        self.assertEqual("John Doe", guy.full_name())
        self.assertEqual("Mr. John Doe", guy.formal_name("Mr."))
