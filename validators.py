NAME_ERROR = "Invalid name: must be a string of words, each with at least 2 alphabetic characters"
AGE_ERROR = "Invalid age: must be an integer between 1 and 120"
STUDENT_ID_ERROR = "Invalid student ID: must be a string of digits, length 1–10, and greater than 0"
GRADE_ERROR = "Invalid grade: must be an integer between 0 and 100"
TEACHER_ID_ERROR = "Invalid teacher ID: must be a string of digits, length 1–10, and greater than 0"
SALARY_ERROR = "Invalid salary: must be a number greater than or equal to 3000"
COURSE_NAME_ERROR = "Invalid course name: must be a string of words, each with at least 2 alphabetic characters"
MAX_STUDENTS_INPUT_ERROR = "Invalid max students: must be an integer greater than 0"
GRADES_ERROR = "Invalid grades: must be a list of integers between 0 and 100"
DUPLICATE_STUDENT_ERROR = "Duplicate student: same student cannot be added twice"
MAX_STUDENTS_ERROR = "Cannot add student: maximum number of students exceeded"
STUDENT_NOT_FOUND_ERROR = "Student not found"
COURSE_ERROR = "Invalid course: must be a Course object"
DUPLICATE_COURSE_ERROR = "Duplicate course: same course cannot be added twice"
COURSE_NOT_FOUND_ERROR = "Course not found"
STUDENT_ERROR = "Invalid student: must be a Student object"
TEACHER_ERROR = "Invalid teacher: must be a Teacher object"
DUPLICATE_TEACHER_ERROR = "Duplicate teacher: same teacher cannot be added twice"
TEACHER_NOT_FOUND_ERROR = "Teacher not found"


def validate_name(name):
    name = " ".join(name.split())
    if isinstance(name, str):
       if all(element.isalpha() and len(element) >= 2 for element in name.split()):
           return name
    raise ValueError(NAME_ERROR)

def validate_age(age):
    try:
        age = int(age)
    except (ValueError, TypeError):
        raise ValueError(AGE_ERROR)
    if age < 1 or age > 120:
        raise ValueError(AGE_ERROR)
    return age

def validate_student_id(student_id):
    if isinstance(student_id, str) and student_id.isdigit() and 1 <= len(student_id) <= 10 and int(student_id) > 0:
        return student_id
    raise ValueError(STUDENT_ID_ERROR)

def validate_grade(grade):
    try:
        g = int(grade)
    except (ValueError, TypeError):     
        raise ValueError(GRADE_ERROR)
    if g < 0 or g > 100:
        raise ValueError(GRADE_ERROR)
    return g

def validate_teacher_id(teacher_id):
    if isinstance(teacher_id, str) and teacher_id.isdigit() and 1 <= len(teacher_id) <= 10 and int(teacher_id) > 0:
        return teacher_id
    raise ValueError(TEACHER_ID_ERROR)

def validate_salary(salary):
    try:
        salary = float(salary.replace(",", ""))
    except (ValueError, TypeError):     
        raise ValueError(SALARY_ERROR)
    if salary < 3000:
        raise ValueError(SALARY_ERROR)
    return salary

def validate_course_name(course_name):
    course_name = " ".join(course_name.split())
    if isinstance(course_name, str):
       if all(element.isalpha() and len(element) >= 2 for element in course_name.split()):
           return course_name
    raise ValueError(COURSE_NAME_ERROR)

def validate_max_students(max_students):
    try:
        max_students = int(max_students)
    except (ValueError, TypeError):     
        raise ValueError(MAX_STUDENTS_INPUT_ERROR)
    if max_students <= 0:
        raise ValueError(MAX_STUDENTS_INPUT_ERROR)
    return max_students 
