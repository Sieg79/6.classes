class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.lect_rate:
                lecturer.lect_rate[course] += [grade]
            else:
                lecturer.lect_rate[course] = [grade]
        else:
            print('Ошибка')

    def __str__(self):
        sep = '\n'
        summ_grade = 0
        for marks in list(self.grades.values()):
            for mark in marks:
                summ_grade += int(mark)
        if summ_grade == 0:
            ave_grade = 'оценок пока нет'
        else:
            ave_grade = summ_grade / len(self.grades)
        courses_now = str(', '.join(self.courses_in_progress))
        courses_past = str(', '.join(self.finished_courses))
        description = f'Имя: {self.name}{sep}Фамилия: {self.surname}{sep}Средняя оценка за домашние задания: \
{ave_grade}{sep}Курсы в процессе изучения: {courses_now}{sep}Завершенные курсы: {courses_past}'
        return description

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lect_rate = {}

    def __str__(self):
        sep = '\n'
        summ_grade = 0
        for marks in list(self.lect_rate.values()):
            for mark in marks:
                summ_grade += int(mark)
        if summ_grade == 0:
            ave_grade = 'оценок пока нет'
        else:
            ave_grade = summ_grade / len(self.lect_rate)
        description = f'Имя: {self.name}{sep}Фамилия: {self.surname}{sep}Средняя оценка за лекции: \
{ave_grade}'
        return description


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('Ошибка')

    def __str__(self):
        sep = '\n'
        description = f'Имя: {self.name}{sep}Фамилия: {self.surname}'
        return description

cool_girl = Student('Ana', 'Nana', 'F')
cool_girl.finished_courses += ['HTML']
cool_girl.courses_in_progress += ['WEB', 'Target']
clever_man = Reviewer('Bob', 'Bobson')
clever_man.courses_attached += ['WEB', 'Target']
clever_man.rate_hw(cool_girl, 'WEB', 10)
clever_man.rate_hw(cool_girl, 'Target', 9)
nice_guy = Lecturer('Peter', 'Peterson')
nice_guy.courses_attached += ['Target', 'WEB']
cool_girl.rate_lecturer(nice_guy, 'Target', 10)
cool_girl.rate_lecturer(nice_guy, 'WEB', 8)
print(clever_man)
print(cool_girl)
print(nice_guy)