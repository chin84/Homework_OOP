class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def marks_lector(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Что-то пошло не так!'

    def __str__(self):
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашнее задание: {self.get_average_rate()}\n' \
               f'Курсы в процессе обучения: {courses_in_progress_string}\n' \
               f'Завершенные курсы: {finished_courses_string}\n'

    def get_average_rate(self):
        if not self.grades:
            return 0
        grades_list = []
        for marks in self.grades.values():
            grades_list.extend(marks)
        return round(sum(grades_list) / len(grades_list), 2)

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'УПС...Так нельзя!!'
        return self.get_average_rate() < other.get_average_rate()

    def __le__(self, other):
        if not isinstance(other, Student):
            return 'УПС...Так нельзя!!'
        return self.get_average_rate() <= other.get_average_rate()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return 'УПС...Так нельзя!!'
        return self.get_average_rate() == other.get_average_rate()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_average_grade(self):
        if not self.grades:
            return 0
        grades_list = []
        for marks in self.grades.values():
            grades_list.extend(marks)
        return round(sum(grades_list) / len(grades_list), 2)

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.get_average_grade()}\n"

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'УПС...Так нельзя!!'
        return self.get_average_rate() < other.get_average_rate()

    def __le__(self, other):
        if not isinstance(other, Student):
            return 'УПС...Так нельзя!!'
        return self.get_average_rate() <= other.get_average_rate()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return 'УПС...Так нельзя!!'
        return self.get_average_rate() == other.get_average_rate()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Что-то пошло не так!'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\n"


best_student = Student('Иван', 'Варенуха', 'your_gender')
bad_student = Student('Клим', 'Чугункин', 'your_gender')

best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['C++']
best_student.finished_courses += ['HTML CSS']
bad_student.courses_in_progress += ['Python']
bad_student.courses_in_progress += ['C++']
bad_student.finished_courses += ['HTML CSS']

cool_reviewer = Reviewer('Кот', 'Бегемот')
bad_reviewer = Reviewer('Михаил', 'Берлиоз')

cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['C++']
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'C++', 10)
cool_reviewer.rate_hw(best_student, 'C++', 9)
cool_reviewer.rate_hw(best_student, 'C++', 8)

bad_reviewer.courses_attached += ['Python']
bad_reviewer.courses_attached += ['C++']
bad_reviewer.rate_hw(bad_student, 'Python', 1)
bad_reviewer.rate_hw(bad_student, 'Python', 2)
bad_reviewer.rate_hw(bad_student, 'Python', 3)
bad_reviewer.rate_hw(bad_student, 'C++', 4)
bad_reviewer.rate_hw(bad_student, 'C++', 5)
bad_reviewer.rate_hw(bad_student, 'C++', 6)

cool_lecturer = Lecturer('Степан', 'Лиходеев')
bad_lecturer = Lecturer('Никанор', 'Босой')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['C++']

best_student.marks_lector(cool_lecturer, 'Python', 9)
best_student.marks_lector(cool_lecturer, 'Python', 4)
best_student.marks_lector(cool_lecturer, 'Python', 10)

best_student.marks_lector(cool_lecturer, 'C++', 10)
best_student.marks_lector(cool_lecturer, 'C++', 9)
best_student.marks_lector(cool_lecturer, 'C++', 8)

bad_lecturer.courses_attached += ['Python']
bad_lecturer.courses_attached += ['C++']

bad_student.marks_lector(bad_lecturer, 'Python', 5)
bad_student.marks_lector(bad_lecturer, 'Python', 2)
bad_student.marks_lector(bad_lecturer, 'Python', 4)

bad_student.marks_lector(bad_lecturer, 'C++', 2)
bad_student.marks_lector(bad_lecturer, 'C++', 3)
bad_student.marks_lector(bad_lecturer, 'C++', 5)

print(cool_reviewer)
print(bad_reviewer)
print(cool_lecturer)
print(bad_lecturer)
print(best_student)
print(bad_student)

course = 'Python'
persons = [best_student, bad_student, cool_lecturer, bad_lecturer]


def total_rating(persons, course):
    grades_list = []
    for person in persons:
        grades_list.extend(person.grades.get(course, []))
    if not grades_list:
        return "Такого курса нет!"
    return round(sum(grades_list) / len(grades_list), 1)


print(f"Средняя оценка для всех студентов по курсу {course}: {total_rating(persons[:2], course)}")

print(f"Средняя оценка для всех лекторов по курсу {course}: {total_rating(persons[2:], course)}")
