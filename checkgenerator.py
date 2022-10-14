from random import randint
from checkiter import Student


def example_generator(student_list):
    i = 0
    while True:
        if i < len(student_list):
            yield print(student_list[i].view_inf())
            i += 1


def example_generator_1(student_list):
    yield print(student_list.view_inf())


if __name__ == "__main__":
    student_list = [Student("Krzysztof", "M", randint(16, 28), ), Student("Władysław", "W", randint(16, 28), ),
                    Student("Józef", "S", randint(16, 28), ), Student("Gerwazy", "F", randint(16, 28), )]

    for i in example_generator(student_list):
        print(i)

    # gener = (gen for gen in example_generator(student_list))
    # for i in gener:
    #     print(i)

