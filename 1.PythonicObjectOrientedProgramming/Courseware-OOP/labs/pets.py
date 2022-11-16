class Pet:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"the {self.__class__.__name__.lower()} says: {self.sound}!"


class Dog(Pet):
    sound = "Woof"


class Cat(Pet):
    sound = "Meow"


fred = Dog("Fred")
misha = Cat("Misha")
print(f"{fred.name} {fred.describe()}")
print(f"{misha.name} {misha.describe()}")
