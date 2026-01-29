from student import Student
from teacher import Teacher


class ReportManager:   
    def __init__(self, student_manager, teacher_manager, course_manager):
        self.__student_manager = student_manager
        self.__teacher_manager = teacher_manager
        self.__course_manager = course_manager

    def list_of_students(self):
        students = self.__student_manager.get_students()
        return [student.get_info() for student in students]

    def list_of_teachers(self):
        teachers = self.__teacher_manager.get_teachers()
        return [teacher.get_info() for teacher in teachers]

    def list_of_courses(self):
        courses = self.__course_manager.get_courses()
        return [course.get_info() for course in courses]

    def list_students_in_course(self, course_name):
        course = self.__course_manager.get_course(course_name)
        students = course.get_students()
        return [student.get_info() for student in students]
    
    def show_statistics(self):
        return {
            "total_students": Student.get_total_students(),
            "total_teachers": Teacher.get_total_teachers(),
            "total_courses": len(self.__course_manager.get_courses()),
        }
