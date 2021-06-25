class Student:
    items = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.items.append(self)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached\
                and course in self.courses_in_progress:
            if course in lecturer.lect_rate:
                lecturer.lect_rate[course] += [grade]
            else:
                lecturer.lect_rate[course] = [grade]
        else:
            print('Ошибка')

    def average_grade(self):
        summ_grade = 0
        grades_quantity = 0
        for marks in list(self.grades.values()):
            for mark in marks:
                summ_grade += int(mark)
                grades_quantity += 1
        if summ_grade == 0:
            ave_grade = 'оценок пока нет'
        else:
            ave_grade = round(summ_grade / grades_quantity, 2)
        return ave_grade

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Это не студент!')
            return
        return self.average_grade() < other.average_grade()

    def __str__(self):
        sep = '\n'
        courses_now = str(', '.join(self.courses_in_progress))
        courses_past = str(', '.join(self.finished_courses))
        description = f'Имя: {self.name}{sep}Фамилия: {self.surname}{sep}Средняя оценка за домашние задания: \
{self.average_grade()}{sep}Курсы в процессе изучения: {courses_now}{sep}Завершенные курсы: {courses_past}'
        return description


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    items = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lect_rate = {}
        Lecturer.items.append(self)

    def average_grade(self):
        summ_grade = 0
        grades_quantity = 0
        for marks in list(self.lect_rate.values()):
            for mark in marks:
                summ_grade += int(mark)
                grades_quantity += 1
        if summ_grade == 0:
            ave_grade = 'оценок пока нет'
        else:
            ave_grade = round(summ_grade / grades_quantity, 2)
        return ave_grade

    def __str__(self):
        sep = '\n'
        description = f'Имя: {self.name}{sep}Фамилия: {self.surname}{sep}Средняя оценка за лекции: \
{self.average_grade()}'
        return description

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Это не лектор!')
            return
        return self.average_grade() < other.average_grade()


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

cool_boy = Student('John', 'Johnson', 'M')
cool_boy.finished_courses += ['HTML', 'SMM']
cool_boy.courses_in_progress += ['C++', 'Target']

clever_man = Reviewer('Bob', 'Bobson')
clever_man.courses_attached += ['WEB', 'Target']
clever_man.rate_hw(cool_girl, 'WEB', 10)
clever_man.rate_hw(cool_girl, 'WEB', 10)
clever_man.rate_hw(cool_girl, 'Target', 9)
clever_man.rate_hw(cool_boy, 'Target', 10)
clever_man.rate_hw(cool_boy, 'Target', 9)

beardman = Reviewer('Bob', 'Bobson')
beardman.courses_attached += ['WEB', 'Target', 'C++']
beardman.rate_hw(cool_girl, 'WEB', 9)
beardman.rate_hw(cool_girl, 'WEB', 10)
beardman.rate_hw(cool_girl, 'Target', 9)
beardman.rate_hw(cool_boy, 'C++', 8)
beardman.rate_hw(cool_boy, 'Target', 9)
beardman.rate_hw(cool_boy, 'Target', 9)

nice_guy = Lecturer('Peter', 'Peterson')
nice_guy.courses_attached += ['Target', 'WEB']
cool_girl.rate_lecturer(nice_guy, 'Target', 10)
cool_girl.rate_lecturer(nice_guy, 'WEB', 8)
cool_boy.rate_lecturer(nice_guy, 'Target', 10)

nice_lady = Lecturer('Jane', 'Jameson')
nice_lady.courses_attached += ['Target', 'C++']
cool_girl.rate_lecturer(nice_lady, 'Target', 10)
cool_boy.rate_lecturer(nice_lady, 'C++', 9)
cool_boy.rate_lecturer(nice_lady, 'Target', 9)


print(clever_man)
print(cool_girl)
print(nice_guy)
print(nice_guy > nice_lady)


def hw_grade_counter(student_lists, course_name):
    summ_mark = 0
    marks_quantity = 0
    for student in student_lists.items:
        if course_name in student.grades:
            for mark in student.grades[course_name]:
                marks_quantity += 1
                summ_mark += mark
    average_mark = round((summ_mark / marks_quantity), 2)
    return average_mark


def lecturers_grade_counter(lecturers_list, course_name):
    summ_mark = 0
    marks_quantity = 0
    for lecturer in lecturers_list.items:
        if course_name in lecturer.lect_rate:
            for mark in lecturer.lect_rate[course_name]:
                marks_quantity += 1
                summ_mark += mark
    average_mark = round((summ_mark / marks_quantity), 2)
    return average_mark


print(hw_grade_counter(Student, 'Target'))
print(lecturers_grade_counter(Lecturer, 'C++'))
