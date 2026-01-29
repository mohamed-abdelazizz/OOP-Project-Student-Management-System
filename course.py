from student import Student
from teacher import Teacher
from validators import (
    validate_course_name, validate_max_students,
    TEACHER_ERROR, DUPLICATE_STUDENT_ERROR, MAX_STUDENTS_ERROR, STUDENT_NOT_FOUND_ERROR, STUDENT_ERROR
)

class Course:
    def __init__(self, course_name, max_students, teacher):
        self.course_name = course_name
        self.max_students = max_students
        self.teacher = teacher
        self.__students = {}

    @property
    def course_name(self):
        return self.__course_name

    @course_name.setter
    def course_name(self, course_name):
        self.__course_name = validate_course_name(course_name)

    @property
    def max_students(self):
        return self.__max_students

    @max_students.setter
    def max_students(self, max_students):
        self.__max_students = validate_max_students(max_students)

    @property
    def teacher(self):
        return self.__teacher

    @teacher.setter
    def teacher(self, teacher):
        if isinstance(teacher, Teacher):
            self.__teacher = teacher
        else:
            raise ValueError(TEACHER_ERROR)

    def add_student(self, student):
        if not isinstance(student, Student):
            raise ValueError(STUDENT_ERROR)
        student_id = student.student_id
        if student_id in self.__students:
            raise ValueError(DUPLICATE_STUDENT_ERROR)
        if len(self.__students) >= self.__max_students:
            raise ValueError(MAX_STUDENTS_ERROR)
        self.__students[student_id] = student

    def remove_student(self, student_id):
        if student_id not in self.__students:
            raise ValueError(STUDENT_NOT_FOUND_ERROR)
        del self.__students[student_id]

    def get_students(self):
        return list(self.__students.values())

    def get_info(self):
        return f"""Course name: {self.course_name}
Teacher: {self.teacher.name}
Students count: {len(self.__students)}/{self.max_students}"""
