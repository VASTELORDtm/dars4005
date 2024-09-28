class Person:
    def __init__(self, ism, familya, yosh):
        self.first_name = ism
        self.last_name = familya
        self.age = yosh

    def introduce(self):
        print(f"My name is {self.first_name}")


p1 = Person("SolihCoder", "Lastname", 99)

p1.introduce()
