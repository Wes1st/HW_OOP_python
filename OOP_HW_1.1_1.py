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
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Должность: студент\n' \
              f'Оценка за домашние задания: {self.grades}\n' \
              f'Средняя оценка за домашние задания: {self.avg_grades}\n' \
              f'Курсы в процессе изучения: {self.courses_in_progress}\n' \
              f'Завершенные курсы: {self.finished_courses}\n'

        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.avg_grades = {}

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
                # student.avg_grades[course] = \
                #     round(*list(map(lambda a: sum(a) / len(*student.grades.values()), student.grades.values())), 1)
            else:
                student.grades[course] = [grade]
                # student.avg_grades[course] = \
                #     round(*list(map(lambda a: sum(a) / len(*student.grades.values()), student.grades.values())), 1)
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.position = 'лектор'

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Должность: {self.position}\n' \
              f'Средняя оценка за лекции: {self.avg_grades}\n' \
              f'Прикрепленные курсы: {self.courses_attached}\n'
        return res


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.position = 'ревьювер'

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Должность: {self.position}\n'
        return res


def create_student(course_list):
    unique_students = []
    [unique_students.append(item) for val in course_student.values() for item in val if item not in unique_students]

    student_dict = {student_id: Student(name, surname, gender)
                    for student_id, (name, surname, gender) in enumerate(unique_students)}

    for i in range(len(student_dict)):
        for item in course_list:
            for val in course_student[item]:
                if student_dict[i].name in val:
                    student_dict.get(i).courses_in_progress.append(item)
        student_dict.get(i).finished_courses.append('Введение в программирование')
        # print(Student.__str__(student_dict.get(i)))

    return student_dict


def create_employee(course_list, employee, course_employee):
    unique_employee = []
    [unique_employee.append(item) for val in course_employee.values() for item in val if item not in unique_employee]

    employee_dict = {employee_id: employee(name, surname)
                     for employee_id, (name, surname) in enumerate(unique_employee)}

    for i in range(len(employee_dict)):
        for item in course_list:
            for val in course_employee[item]:
                if employee_dict[i].name in val:
                    employee_dict.get(i).courses_attached.append(item)

        # print(employee.__str__(employee_dict.get(i)))

    return employee_dict


course = ['Python', 'GIT']

course_student = {course[0]: [
    ['Riannon', 'Maber', 'Female'],
    ['Kellby', 'MacArthur', 'Male'],
    ['Emiline', 'Barnshaw', 'Female'],
    ['Odo', 'Bluck', 'Male']
],
    course[1]: [
        ['Riannon', 'Maber', 'Female'],
        ['June', 'Ealles', 'Female'],
        ['Emiline', 'Barnshaw', 'Female'],
        ['Roth', 'Strowlger', 'Male']
    ]}

course_lecturer = {course[0]: [
    ['Libbey', 'Tirrey'],
    ['Hailey', 'Donoher']
],
    course[1]: [
        ['Libbey', 'Tirrey'],
        ['Teddy', 'Edmondson']
    ]}

course_reviewer = {course[0]: [
    ['Philipa', 'Larwell'],
    ['Alix', 'Ben']
],
    course[1]: [
        ['Philipa', 'Larwell'],
        ['Rice', 'Bowlands'],
        ['Cara', 'Bukac']
    ]}

student = create_student(course)

lecturer = create_employee(course, Lecturer, course_lecturer)
reviewer = create_employee(course, Reviewer, course_reviewer)

reviewer[0].rate_hw(student[0], course[0], 10)
reviewer[0].rate_hw(student[0], course[1], 8)

reviewer[1].rate_hw(student[0], course[0], 7)
reviewer[1].rate_hw(student[0], course[1], 3)

reviewer[2].rate_hw(student[0], course[0], 9)
reviewer[2].rate_hw(student[0], course[1], 5)

print(student[0])
# best_student.courses_in_progress += ['Python']
#
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
#
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)

# print(best_student.grades)
# print(course_student['Python'][1])
# print(student_py_1.name, student_py_1.surname, student_py_1.gender)


# def avg_sum(x):
#         for val in x.values():
#
#             for item in val:
#                 print(item)

# x = {'python': [4, 10, 8]}
#
# res = round(*list(map(lambda a: sum(a) / len(*x.values()), x.values())), 1)
# print(len(x.values()))
# print(res)
# avg_sum({'python': [5, 10]})