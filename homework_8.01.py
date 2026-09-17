#Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
#Створіть об('єкт цього класу, представляючи студента. '
#Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента.'
#Виведіть інформацію про студента та змініть його середній бал.)
class Student:
    def __init__(self, name, surname, age, average_mark):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_mark = average_mark

    def change_average_mark(self, new_average_mark):
        self.average_mark = new_average_mark


student = Student(
    name="Pavlo",
    surname="Ivanov",
    age=28,
    average_mark=70
)

print(f"name: {student.name}, surname: {student.surname}, age: {student.age}, old average mark: {student.average_mark}")
student.change_average_mark(85)

print(f"name: {student.name}, surname: {student.surname}, age: {student.age}, updated average mark: {student.average_mark}")