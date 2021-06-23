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
        for grade in self.grades:
            summ_grade += grade
        if summ_grade == 0:
            ave_grade = 'оценок пока нет'
        else:
            ave_grade = summ_grage / len(self.grades)
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

cool_girl = Student('Ana', 'Nana', 'F')
cool_girl.finished_courses += ['HTML']
cool_girl.courses_in_progress += ['WEB', 'Target']
print(cool_girl)
