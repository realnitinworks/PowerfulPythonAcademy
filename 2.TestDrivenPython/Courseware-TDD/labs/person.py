from dataclasses import dataclass


@dataclass
class Person:
    first: str
    last: str

    def full_name(self):
        return f"{self.first} {self.last}"

    def formal_name(self, title):
        return f"{title} {self.full_name()}"
