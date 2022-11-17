class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def full_name(self):
        return self.first + " " + self.last

    def formal_name(self, title):
        return title + " " + self.full_name()

# Part of Powerful Python Academy. Copyright MigrateUp LLC. All rights reserved.
