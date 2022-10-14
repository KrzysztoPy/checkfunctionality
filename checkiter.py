from random import randint


class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


class ClassAtSchool:
    def __init__(self, class_name):
        self.number_at_jurnal = 1
        self.class_name = class_name
        self.list_with_students = list()
        self.i = 0

    def adding_to_class_list(self, student):
        student.set_class_at_school(self.class_name)
        student.set_number_at_jurnal(self.number_at_jurnal)
        self.increment_number_at_jurnal()
        self.list_with_students.append(student)

    def increment_number_at_jurnal(self):
        self.number_at_jurnal += 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == self.list_with_students.__len__():
            self.i = 0
            raise StopIteration
        self.i += 1
        return self.list_with_students[self.i - 1]


class Student(Person, ClassAtSchool):

    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.class_at_school = None
        self.number_at_jurnal = None

    def set_number_at_jurnal(self, number_at_jurnal):
        self.number_at_jurnal = number_at_jurnal

    def set_class_at_school(self, class_at_school):
        self.class_at_school = class_at_school

    def view_inf(self):
        return f" \nStudent name: {self.name} \n" \
               f"Student surname: {self.surname}\n" \
               f"Student age: {self.age} \n" \
               f"Student class name: {self.class_at_school} \n" \
               f"Student number at jurnal: {self.number_at_jurnal}"

        # print(f"Student name: {self.name}")
        # print(f"Student surname: {self.surname}")
        # print(f"Student age: {self.age}")
        # print(f"Student class name: {self.class_at_school}")
        # print(f"Student number at jurnal: {self.number_at_jurnal}")


s1 = Student("Krzysztof", "M", randint(16, 28), )
s2 = Student("Władysław", "W", randint(16, 28), )
s3 = Student("Józef", "S", randint(16, 28), )
s4 = Student("Gerwazy", "F", randint(16, 28), )

class_1cT = ClassAtSchool("1cT")
class_1cT.adding_to_class_list(s1)
class_1cT.adding_to_class_list(s2)
class_1cT.adding_to_class_list(s3)
class_1cT.adding_to_class_list(s4)

for i in class_1cT:
    print(i.view_inf())
