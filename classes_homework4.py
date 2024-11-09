# class Person:
#    def __init__(self, name: str, surname: str, age: int):
#        self.name = name
#        self.surname = surname
#        self.age = age
#
#    def info_person(self):
#        print(f'Person: {self.name} | {self.surname} | {self.age}')


class Person:
    name: str
    surname: str
    age: int
    pensione: bool

    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age
        self.set_pensione(self.age)

    def set_pensione(self, value: int):
        if value >= 60:
            self.pensione = True
        else:
            self.pensione = False

    def info_person(self):
        print(f'Person: {self.name} | {self.surname} | {self.age}')


Chelovek1 = Person('Абобус', 'Автобус', 68)
Chelovek2 = Person('Амогус', 'Автобус', 45)
print(f'Name: {Chelovek1.name}, Surname: {Chelovek1.surname}, Age: {Chelovek1.age}, Pensione: {Chelovek1.pensione}')
print(f'Name: {Chelovek2.name}, Surname: {Chelovek2.surname}, Age: {Chelovek2.age}, Pensione: {Chelovek2.pensione}')
