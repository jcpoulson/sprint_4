class Admin():
    id = ''
    first_name = ''
    last_name = ''
    is_admin = True

    def __init__(self, first_name, last_name, is_admin):
        self.first_name = first_name
        self.first_name = last_name
        self.is_admin = is_admin

class Teacher():
    id = ''
    first_name = ''
    last_name = ''
    courses_to_teach = []
    students = []
    is_admin = False

    def __init__(self, first_name, last_name, courses_to_teach, students):
        self.first_name = first_name
        self.first_name = last_name
        self.courses_to_teach = courses_to_teach
        self.students = students

class Student():
    id = ''
    first_name = ''
    last_name = ''
    courses_enrolled = []
    teachers = []
    is_admin = False

    def __init__(self, first_name, last_name, courses_enrolled, teachers):
        self.first_name = first_name
        self.first_name = last_name
        self.courses_enrolled = courses_enrolled
        self.teachers = []

class Course():
    id = ''
    course_name = ''
    couse_level = ''
    teacher = ''
    students = []

    def __init__(self, course_name, course_level, teacher, students):
        self.course_name = course_name
        self.course_level = course_level
        self.teacher = teacher
        self.students = students