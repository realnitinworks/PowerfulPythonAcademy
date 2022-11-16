class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def full_name(self):
        return f"{self.first} {self.last}"

    @full_name.setter
    def full_name(self, value):
        first, last = value.split()
        self.first, self.last = first, last


p = Person("Nitin", "Cherian")
print(p.full_name)
p.full_name = "Dave George"
print(p.full_name)
