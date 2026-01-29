from validators import validate_name, validate_age


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = validate_name(name)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = validate_age(age)
   
    def get_info(self):
        return f"""Person name: {self.name}
Person age: {self.age}"""
