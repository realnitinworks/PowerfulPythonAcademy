class Person:
    def __init__(self, first, middle, last) -> None:
        self.first = first
        self.middle = middle
        self.last = last

    def full_name(self):
        return f"{self.first} {self.middle} {self.last}"

    def formal_name(self, title):
        return f"{title} {self.full_name()}"


person = Person("Nitin", "George", "Cherian")
print(person.formal_name("Mr."))
