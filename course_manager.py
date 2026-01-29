from course import Course
from validators import COURSE_ERROR, DUPLICATE_COURSE_ERROR, COURSE_NOT_FOUND_ERROR


class CourseManager:
    def __init__(self):
        self.__courses = {}

    def add_course(self, course):
        if not isinstance(course, Course):
            raise ValueError(COURSE_ERROR)
        course_name = course.course_name
        if course_name in self.__courses:
            raise ValueError(DUPLICATE_COURSE_ERROR)
        self.__courses[course_name] = course

    def delete_course(self, course_name):
        if course_name not in self.__courses:
            raise ValueError(COURSE_NOT_FOUND_ERROR)
        del self.__courses[course_name]

    def add_student_to_course(self, course_name, student):
        if course_name not in self.__courses:
            raise ValueError(COURSE_NOT_FOUND_ERROR)
        self.__courses[course_name].add_student(student)

    def remove_student_from_course(self, course_name, student_id):
        if course_name not in self.__courses:
            raise ValueError(COURSE_NOT_FOUND_ERROR)
        self.__courses[course_name].remove_student(student_id)

    def change_course_teacher(self, course_name, teacher):
        if course_name not in self.__courses:
            raise ValueError(COURSE_NOT_FOUND_ERROR)
        self.__courses[course_name].teacher = teacher

    def view_course_info(self, course_name):
        if course_name not in self.__courses:
            raise ValueError(COURSE_NOT_FOUND_ERROR)
        return self.__courses[course_name].get_info()

    def get_course(self, course_name):
        if course_name not in self.__courses:
            raise ValueError(COURSE_NOT_FOUND_ERROR)
        return self.__courses[course_name]

    def get_courses(self):
        return list(self.__courses.values())
