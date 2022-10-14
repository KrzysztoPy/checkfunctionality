from random import randint
from checkiter import Student


def example_generator(student_list):
    i = 0
    while True:
        if i < len(student_list):
            yield student_list[i].view_inf()
            i += 1
        else:
            break


def tmp_gen():
    for i in range(4):
        yield i


def example_generator_in_another_generator(student_list):
    yield "List with studenst:"
    yield from example_generator(student_list)
    yield "\nEnds list with students."


if __name__ == "__main__":
    student_list = [Student("Krzysztof", "M", randint(16, 28), ), Student("Władysław", "W", randint(16, 28), ),
                    Student("Józef", "S", randint(16, 28), ), Student("Gerwazy", "F", randint(16, 28), )]

    for i in example_generator(student_list):
        print(i)

    # gen = example_generator(student_list)K
    # print(next(gen))
    # print(next(gen))
    # print(next(gen))
    # print(next(gen))
    # print(next(gen)) # That "next" method only raise StopIteration.

    # for i in example_generator_in_another_generator(student_list):
    #     print(i)

    # exa_gen = example_generator_in_another_generator(student_list)
    # print(next(exa_gen))
    # print(next(exa_gen))
    # print(next(exa_gen))
    # print(next(exa_gen))
    # print(next(exa_gen))
    # print(next(exa_gen))
    # print(next(exa_gen))
    # print(next(exa_gen)) # That "next" method only raise StopIteration.



