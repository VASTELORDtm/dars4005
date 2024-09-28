class Student:
    def __init__(self, first_name, last_name, birth_year):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.num_of_books_read = 0
        self.num_of_subjects_learned = 0

    def introduce(self):
        print(
            f"First name: {self.first_name}", f"Last name: {self.last_name}", f"Birth year: {self.birth_year}", sep="\n"
        )

    def read_books(self, number):
        print(f"{self.first_name} has read {number} books")
        self.num_of_books_read += number

    def learn_subjects(self, subject):
        print(f"{self.first_name} has learned {subject}")
        self.num_of_subjects_learned += 1

    def report(self):
        self.introduce()
        print(f"Books read: {self.num_of_books_read}")
        print(f"Subjects learned: {self.num_of_subjects_learned}")

student=Student("Vasto","Lorde","2008")
student.introduce()
