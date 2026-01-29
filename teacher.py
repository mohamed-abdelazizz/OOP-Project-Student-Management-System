from person import Person
from validators import validate_teacher_id, validate_salary


class Teacher(Person):
    __total_teachers = 0

    def __init__(self, name, age, teacher_id, salary):
        super().__init__(name, age)
        self.teacher_id = teacher_id
        self.salary = salary
        Teacher.__total_teachers += 1

    @property
    def teacher_id(self):
        return self.__teacher_id

    @teacher_id.setter
    def teacher_id(self, teacher_id):
        self.__teacher_id = validate_teacher_id(teacher_id)

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        self.__salary = validate_salary(salary)

    @classmethod
    def get_total_teachers(cls):
        return cls.__total_teachers

    @classmethod
    def decrement_total_teachers(cls):
        if cls.__total_teachers > 0:
            cls.__total_teachers -= 1

    def get_info(self):
        return f"""Teacher name: {self.name}
Teacher age: {self.age}
Teacher id: {self.teacher_id}
Teacher salary: {self.salary:.2f}"""
