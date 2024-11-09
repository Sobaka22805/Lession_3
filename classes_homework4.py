class Person:
    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age

    def info_person(self):
        print(f'Person: {self.name} | {self.surname} | {self.age}')

