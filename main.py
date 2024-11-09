import inspect
from lesson_4 import Student
from classes_homework4 import Person

print('Lesson 5: Class Inspect')

print('(Student) is function: ', inspect.isfunction(Student))
print('(Student) is class: ', inspect.isclass(Student))
print('(Person) is function: ', inspect.isfunction(Person))
print('(Person) is class: ', inspect.isclass(Person))

sigStudent = inspect.signature(Student)
sigPerson = inspect.signature(Person)

print(f'(Class Person)', sigPerson.parameters)
print(f'(Class Student)', sigStudent.parameters)
for item in sigPerson.parameters.items():
    print('Class "Person"')
    print(f'item - {item[1]}')

for item in sigStudent.parameters.items():
    print('Class "Student"')
    print(f'item - {item[1]}')
