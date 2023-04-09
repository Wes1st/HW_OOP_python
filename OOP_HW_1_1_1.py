import random


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.position = []
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.avg_grades = {}

    def __str__(self):
        to_string = f'Имя: {self.name}\n' \
                    f'Фамилия: {self.surname}\n' \
                    f'Должность: студент\n' \
                    f'Оценка за домашние задания: {self.grades}\n' \
                    f'Средняя оценка за домашние задания: {self.avg_grades}\n' \
                    f'Курсы в процессе изучения: {self.courses_in_progress}\n' \
                    f'Завершенные курсы: {self.finished_courses}\n'
        return to_string

    def avg_rate_lecturers(self, lecturers, course, grade):
        if isinstance(lecturers, Lecturer) \
                and course in self.courses_in_progress \
                and course in lecturers.courses_attached:

            if course in lecturers.grades:
                lecturers.grades[course] += [grade]
            else:
                lecturers.grades[course] = [grade]

            lecturers.avg_grades[course] = round(*list(
                map(lambda res: sum(res) / len(lecturers.grades.get(course)),
                    [[val for val in lecturers.grades[course]]])), 1)
        else:
            return 'Ошибка'

    def course_avg_rates_students(self, student2, courses):
        for course in courses:
            if isinstance(student2, Student) \
                    and course in self.courses_in_progress \
                    and course in student2.courses_in_progress:
                if Comparing.__lt__(self.avg_grades[course], student2.avg_grades[course]):
                    print(f'Средняя оценка студента на курсе {course} у '
                          f'{self.name} {self.surname} = {self.avg_grades[course]} меньше чем у '
                          f'{student2.name} {student2.surname} = {student2.avg_grades[course]}')
                elif Comparing.__gt__(self.avg_grades[course], student2.avg_grades[course]):
                    print(f'Средняя оценка студента на курсе {course} у '
                          f'{self.name} {self.surname} = {self.avg_grades[course]} больше чем у '
                          f'{student2.name} {student2.surname} = {student2.avg_grades[course]}')
                elif Comparing.__eq__(self.avg_grades[course], student2.avg_grades[course]):
                    print(f'Средняя оценка студента на курсе {course} у '
                          f'{self.name} {self.surname} = {self.avg_grades[course]} равна оценке '
                          f'{student2.name} {student2.surname} = {student2.avg_grades[course]}')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def avg_rate_students(self, student, course, grade):
        if isinstance(student, Student) \
                and course in self.courses_attached \
                and course in student.courses_in_progress:

            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]

            student.avg_grades[course] = round(*list(
                map(lambda res: sum(res) / len(student.grades.get(course)),
                    [[val for val in student.grades[course]]])), 1)
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.position = 'лектор'
        self.grades = {}
        self.avg_grades = {}

    def __str__(self):
        to_string = f'Имя: {self.name}\n' \
                    f'Фамилия: {self.surname}\n' \
                    f'Должность: {self.position}\n' \
                    f'Средняя оценка за лекции: {self.avg_grades}\n' \
                    f'Прикрепленные курсы: {self.courses_attached}\n'
        return to_string

    def course_avg_rates_lecturers(self, lecturer2, courses):
        for course in courses:
            if isinstance(lecturer2, Lecturer) \
                    and course in self.courses_attached \
                    and course in lecturer2.courses_attached:
                if Comparing.__lt__(self.avg_grades[course], lecturer2.avg_grades[course]):
                    print(f'Средняя оценка лектора на курсе {course} у '
                          f'{self.name} {self.surname} = {self.avg_grades[course]} меньше чем у '
                          f'{lecturer2.name} {lecturer2.surname} = {lecturer2.avg_grades[course]}')
                elif Comparing.__gt__(self.avg_grades[course], lecturer2.avg_grades[course]):
                    print(f'Средняя оценка лектора на курсе {course} у '
                          f'{self.name} {self.surname} = {self.avg_grades[course]} больше чем у '
                          f'{lecturer2.name} {lecturer2.surname} = {lecturer2.avg_grades[course]}')
                elif Comparing.__eq__(self.avg_grades[course], lecturer2.avg_grades[course]):
                    print(f'Средняя оценка лектора на курсе {course} у '
                          f'{self.name} {self.surname} = {self.avg_grades[course]} равна оценке '
                          f'{lecturer2.name} {lecturer2.surname} = {lecturer2.avg_grades[course]}')


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.position = 'ревьювер'

    def __str__(self):
        to_string = f'Имя: {self.name}\n' \
                    f'Фамилия: {self.surname}\n' \
                    f'Должность: {self.position}\n'
        return to_string


class Comparing:
    def __lt__(self, other):
        return self < other

    def __gt__(self, other):
        return self > other

    def __eq__(self, other):
        return self == other


def create_student(course_list):
    unique_students = []
    [unique_students.append(item)
     for val in course_student.values()
     for item in val if item not in unique_students]

    student_dict = {student_id: Student(name, surname, gender)
                    for student_id, (name, surname, gender) in enumerate(unique_students)}

    for i in range(len(student_dict)):
        for item in course_list:
            for val in course_student[item]:
                if student_dict[i].name in val:
                    student_dict.get(i).courses_in_progress.append(item)
        student_dict.get(i).finished_courses.append('Введение в программирование')

    return student_dict


def create_employee(course_list, employee, course_employee):
    unique_employee = []
    [unique_employee.append(item)
     for val in course_employee.values()
     for item in val if item not in unique_employee]

    employee_dict = {employee_id: employee(name, surname)
                     for employee_id, (name, surname) in enumerate(unique_employee)}

    for i in range(len(employee_dict)):
        for item in course_list:
            for val in course_employee[item]:
                if employee_dict[i].name in val:
                    employee_dict.get(i).courses_attached.append(item)

    return employee_dict


def get_rates(who_rated, who_is_rated, courses):
    for course in courses:
        for val in range(len(who_rated)):
            if isinstance(who_rated[val], Student):
                if course in who_rated[val].courses_in_progress:
                    for item in range(len(who_is_rated)):
                        who_rated[val].avg_rate_lecturers(who_is_rated[item], course, random.randint(1, 10))
            elif isinstance(who_rated[val], Lecturer):
                if course in who_rated[val].courses_attached:
                    for item in range(len(who_is_rated)):
                        who_rated[val].avg_rate_students(who_is_rated[item], course, random.randint(1, 10))


def avg_courses_rates(val_list, courses):
    avg_rates = {}

    for course in courses:
        for val in val_list:
            if val_list[val].grades.get(course) is not None:
                for rate in val_list[val].grades.get(course):
                    if course in avg_rates:
                        avg_rates[course] += [rate]
                    else:
                        avg_rates[course] = [rate]
        avg_rates[course] = round(sum(avg_rates[course]) / len(avg_rates[course]), 1)

    return avg_rates


def get_to_string(val_list):
    for val in range(len(val_list)):
        print(val_list[val])


extension_course = ['Python', 'GIT']

course_student = {extension_course[0]: [
    ['Riannon', 'Maber', 'Female'],
    ['Kellby', 'MacArthur', 'Male'],
    ['Emiline', 'Barnshaw', 'Female'],
    ['Odo', 'Bluck', 'Male']
],
    extension_course[1]: [
        ['Riannon', 'Maber', 'Female'],
        ['June', 'Ealles', 'Female'],
        ['Emiline', 'Barnshaw', 'Female'],
        ['Roth', 'Strowlger', 'Male']
    ]}

course_lecturer = {extension_course[0]: [
    ['Libbey', 'Tirrey'],
    ['Hailey', 'Donoher']
],
    extension_course[1]: [
        ['Libbey', 'Tirrey'],
        ['Hailey', 'Donoher'],
        ['Teddy', 'Edmondson']
    ]}

course_reviewer = {extension_course[0]: [
    ['Philipa', 'Larwell'],
    ['Alix', 'Ben']
],
    extension_course[1]: [
        ['Philipa', 'Larwell'],
        ['Rice', 'Bowlands'],
        ['Cara', 'Bukac']
    ]}

students = create_student(extension_course)
lecturer = create_employee(extension_course, Lecturer, course_lecturer)
reviewer = create_employee(extension_course, Reviewer, course_reviewer)

get_rates(students, lecturer, extension_course)
get_rates(lecturer, students, extension_course)
get_to_string(students)
get_to_string(lecturer)

print(f'Средняя оценка за домашние задания по всем студентам в рамках курса '
      f'{avg_courses_rates(students, extension_course)}')

print(f'Средняя оценка за лекции всех лекторов в рамках курса '
      f'{avg_courses_rates(lecturer, extension_course)}')

Student.course_avg_rates_students(students[0], students[2], extension_course)
Lecturer.course_avg_rates_lecturers(lecturer[0], lecturer[1], extension_course)