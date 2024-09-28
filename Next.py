class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(self.name, "is walking")

    def eat(self):
        print(self.name, "is eating")


class Dog(Animal):
    def eat(self):
        print(self.name, "the dog is eating")

    def walk(self):
        super().walk()
        print("It yuguryapti")

    def make_sound(self):
        print(f"{self.name}: Woof!")


dog1 = Dog("Hasan")

dog1.walk()
dog1.eat()
dog1.make_sound()
