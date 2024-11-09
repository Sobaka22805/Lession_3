import inspect
from lesson_4 import Student
from classes_homework4 import Person

# print('Lesson 6: Try-Expect')

# print('(Student) is function: ', inspect.isfunction(Student))
# print('(Student) is class: ', inspect.isclass(Student))
# print('(Person) is function: ', inspect.isfunction(Person))
# print('(Person) is class: ', inspect.isclass(Person))

# try:
#   print('(Person) is method: ', inspect.ismethod(Person))
# except Exception as exception:
#    print(f'Error: {exception.__str__()}')
# finally:
#    print('Checking is done!')

# try:
#    print('(Student) is method: ', inspect.ismethod(Student))
# except Exception as exception:
#    print(f'Error: {exception.__str__()}')
# finally:
#    print('Checking is done!')

# sigStudent = inspect.signature(Student)
# sigPerson = inspect.signature(Person)

# print(f'(Class Person)', sigPerson.parameters)
# print(f'(Class Student)', sigStudent.parameters)
# for item in sigPerson.parameters.items():
#    print('Class "Person"')
#    print(f'item - {item[1]}')

# for item in sigStudent.parameters.items():
#    print('Class "Student"')
#    print(f'item - {item[1]}')


# class ItemSoft:
#    price: int
#    mark: str
#    company: str

#    def __init__(self, price: int, mark: str, company: str):
#        if type(price) is not int:
#            raise TypeError('argument price is not int')
#        self.price = price
#        self.mark = mark
#        self.company = company


# try:
#    keyboard = ItemSoft(1500, 'Logitech', 'Logitech International S.A')
#    print(f'Mark: {keyboard.mark}, Price: {keyboard.price}, Company: {keyboard.company}')
# except Exception as error:
#    print(f'error msg: {error.__str__()}')
# finally:
#    print('init of instance is done')

