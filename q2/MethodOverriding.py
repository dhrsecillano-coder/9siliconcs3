class Animal:
    def __init__(self, name):
        self.name = name

    def feed(self):
        print(self.name, "is eating.")

    def make_sound(self):
        print(self.name, "makes a sound.")

class Lion(Animal):
    def make_sound(self):
        print(self.name, "roars loudly!")
        return ""

    def feed(self):
        print(self.name, "eats fresh meat.")
        return ""

class Elephant(Animal):
    def make_sound(self):
        print(self.name, "trumpets!")
        return ""

    def feed(self):
        print(self.name, "eats grass and fruits.")
        return ""

class Monkey(Animal):
    def make_sound(self):
        print(self.name, "chatters!")
        return ""

    def feed(self):
        print(self.name, "eats bananas.")
        return ""


lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")

print(lion.make_sound())
print(lion.feed())
print("-----")

print(elephant.make_sound())
print(elephant.feed())
print("-----")

print(monkey.make_sound())
print(monkey.feed())
print("-----")
