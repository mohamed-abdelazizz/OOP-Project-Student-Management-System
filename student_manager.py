from student import Student
from validators import GRADES_ERROR, STUDENT_ERROR, DUPLICATE_STUDENT_ERROR, STUDENT_NOT_FOUND_ERROR


class StudentManager:
    def __init__(self):
        self.__students = {}

    def add_student(self, student):
        if not isinstance(student, Student):
            raise ValueError(STUDENT_ERROR)
        student_id = student.student_id
        if student_id in self.__students:
            raise ValueError(DUPLICATE_STUDENT_ERROR)
        self.__students[student_id] = student

    def update_student_grades(self, student_id, grades):
        if student_id not in self.__students:
            raise ValueError(STUDENT_NOT_FOUND_ERROR)
        self.__students[student_id].grades = grades

    def add_grade_to_student(self, student_id, grade):
        if student_id not in self.__students:
            raise ValueError(STUDENT_NOT_FOUND_ERROR)
        self.__students[student_id].add_grade(grade)

    def delete_student(self, student_id):
        if student_id not in self.__students:
            raise ValueError(STUDENT_NOT_FOUND_ERROR)
        del self.__students[student_id]
        Student.decrement_total_students()

    def view_student_info(self, student_id):
        if student_id not in self.__students:
            raise ValueError(STUDENT_NOT_FOUND_ERROR)
        return self.__students[student_id].get_info()

    def get_student(self, student_id):
        if student_id not in self.__students:
            raise ValueError(STUDENT_NOT_FOUND_ERROR)
        return self.__students[student_id]

    def get_students(self):
        return list(self.__students.values())
