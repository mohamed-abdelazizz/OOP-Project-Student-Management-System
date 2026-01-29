from teacher import Teacher
from validators import TEACHER_ERROR, DUPLICATE_TEACHER_ERROR, TEACHER_NOT_FOUND_ERROR


class TeacherManager:
    def __init__(self):
        self.__teachers = {}

    def add_teacher(self, teacher):
        if not isinstance(teacher, Teacher):
            raise ValueError(TEACHER_ERROR)
        teacher_id = teacher.teacher_id
        if teacher_id in self.__teachers:
            raise ValueError(DUPLICATE_TEACHER_ERROR)
        self.__teachers[teacher_id] = teacher

    def update_teacher_salary(self, teacher_id, salary):
        if teacher_id not in self.__teachers:
            raise ValueError(TEACHER_NOT_FOUND_ERROR)
        self.__teachers[teacher_id].salary = salary

    def delete_teacher(self, teacher_id):
        if teacher_id not in self.__teachers:
            raise ValueError(TEACHER_NOT_FOUND_ERROR)
        del self.__teachers[teacher_id]
        Teacher.decrement_total_teachers()

    def view_teacher_info(self, teacher_id):
        if teacher_id not in self.__teachers:
            raise ValueError(TEACHER_NOT_FOUND_ERROR)
        return self.__teachers[teacher_id].get_info()

    def get_teacher(self, teacher_id):
        if teacher_id not in self.__teachers:
            raise ValueError(TEACHER_NOT_FOUND_ERROR)
        return self.__teachers[teacher_id]

    def get_teachers(self):
        return list(self.__teachers.values())
