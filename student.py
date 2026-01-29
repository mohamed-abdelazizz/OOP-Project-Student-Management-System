from person import Person
from validators import validate_student_id, validate_grade, GRADES_ERROR


class Student(Person):
    __total_students = 0

    def __init__(self, name, age, student_id, grades=None):
        super().__init__(name, age)
        self.student_id = student_id
        self.grades = grades if grades is not None else []
        Student.__total_students += 1 

    @property
    def student_id(self):
        return self.__student_id

    @student_id.setter
    def student_id(self, student_id):
        self.__student_id = validate_student_id(student_id)

    @property
    def grades(self):
        return self.__grades.copy()

    @grades.setter
    def grades(self, grades):
        if isinstance(grades, list):
            self.__grades = [validate_grade(g) for g in grades]
        else:
            raise ValueError(GRADES_ERROR)

    def add_grade(self, grade):
        grade = validate_grade(grade)
        self.__grades.append(grade)

    def calculate_average(self):
        if len(self.__grades) == 0:
            return 0
        return sum(self.__grades) / len(self.__grades)

    @classmethod
    def get_total_students(cls):
        return cls.__total_students

    @classmethod
    def decrement_total_students(cls):
        if cls.get_total_students() > 0:
            cls.__total_students -= 1

    def get_info(self):
        return f"""Student name: {self.name}
Student age: {self.age}
Student id: {self.student_id}
Student grades: {self.grades}
Student average grade: {self.calculate_average():.2f}"""
