from student import Student
from teacher import Teacher
from course import Course
from student_manager import StudentManager
from teacher_manager import TeacherManager
from course_manager import CourseManager
from report_manager import ReportManager
from system_menu import SystemMenu
from validators import (
    validate_name, validate_age, validate_student_id, validate_grade,
    validate_teacher_id, validate_salary, validate_course_name, validate_max_students,
    DUPLICATE_STUDENT_ERROR, DUPLICATE_TEACHER_ERROR, DUPLICATE_COURSE_ERROR
)


def get_input_with_validation(prompt, validation_func):
    while True:
        value = input(prompt).strip()
        try:
            validation_func(value)
            return value
        except ValueError as e:
            print(f"Error: {e}")


def handle_students_menu(student_manager):
    while True:
        print()
        SystemMenu.students_menu()
        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                print("\n===== Add New Student =====")
                student_name = get_input_with_validation("Enter student name: ", validate_name)
                student_age = get_input_with_validation("Enter student age: ", validate_age)
                student_id = get_input_with_validation("Enter student ID: ", validate_student_id)
                try:
                    student_manager.get_student(student_id)
                    print(DUPLICATE_STUDENT_ERROR)
                    continue
                except ValueError:
                    pass
                student_grades = []
                while True:
                    grade = input("Enter grade (0-100), (or press Enter to finish): ").strip()
                    if not grade:
                        break
                    try:
                        validate_grade(grade)
                        student_grades.append(grade)
                    except ValueError as e:
                        print(f"Error: {e}")
                        continue
                student = Student(student_name, student_age, student_id, student_grades)
                student_manager.add_student(student)
                print("Student added successfully")

            elif choice == "2":
                print("\n===== Update Student Grades =====")
                student_id = get_input_with_validation("Enter student ID: ", validate_student_id)
                try:
                    student_manager.get_student(student_id)
                except ValueError as e:
                    print(f"Error: {e}")
                    continue
                student_grades = []
                while True:
                    grade = input("Enter grade (0-100), (or press Enter to finish): ").strip()
                    if not grade:
                        break
                    try:
                        validate_grade(grade)
                        student_grades.append(grade)
                    except ValueError as e:
                        print(f"Error: {e}")
                        continue
                student_manager.update_student_grades(student_id, student_grades)
                print("Grades updated successfully")

            elif choice == "3":
                print("\n===== Add Grade to Student =====")
                student_id = get_input_with_validation("Enter student ID: ", validate_student_id)
                try:
                    student_manager.get_student(student_id)
                except ValueError as e:
                    print(f"Error: {e}")
                    continue
                new_grade = get_input_with_validation("Enter grade (0-100): ", validate_grade)
                student_manager.add_grade_to_student(student_id, new_grade)
                print("Grade added successfully")

            elif choice == "4":
                print("\n===== Delete Student =====")
                student_id = get_input_with_validation("Enter student ID: ", validate_student_id)
                student_manager.delete_student(student_id)
                print("Student deleted successfully")
                
            elif choice == "5":
                print("\n===== Student Information =====")
                student_id = get_input_with_validation("Enter student ID: ", validate_student_id)
                print(student_manager.view_student_info(student_id))

            elif choice == "6":
                break

            else:
                print("Invalid choice: try again")

        except ValueError as e:
            print(f"Error: {e}")


def handle_teachers_menu(teacher_manager):
    while True:
        print()
        SystemMenu.teachers_menu()
        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                print("\n===== Add New Teacher =====")
                teacher_name = get_input_with_validation("Enter teacher name: ", validate_name)
                teacher_age = get_input_with_validation("Enter teacher age: ", validate_age)
                teacher_id = get_input_with_validation("Enter teacher ID: ", validate_teacher_id)
                try:
                    teacher_manager.get_teacher(teacher_id)
                    print(DUPLICATE_TEACHER_ERROR)
                    continue
                except ValueError:
                    pass
                teacher_salary = get_input_with_validation("Enter teacher salary: ", validate_salary)
                teacher = Teacher(teacher_name, teacher_age, teacher_id, teacher_salary)
                teacher_manager.add_teacher(teacher)
                print("Teacher added successfully")

            elif choice == "2":
                print("\n===== Update Teacher Salary =====")
                teacher_id = get_input_with_validation("Enter teacher ID: ", validate_teacher_id)
                try:
                    teacher_manager.get_teacher(teacher_id)
                except ValueError as e:
                    print(f"Error: {e}")
                    continue
                new_salary = get_input_with_validation("Enter new salary: ", validate_salary)
                teacher_manager.update_teacher_salary(teacher_id, new_salary)
                print("Salary updated successfully")

            elif choice == "3":
                print("\n===== Delete Teacher =====")
                teacher_id = get_input_with_validation("Enter teacher ID: ", validate_teacher_id)
                teacher_manager.delete_teacher(teacher_id)
                print("Teacher deleted successfully")

            elif choice == "4":
                print("\n===== Teacher Information =====")
                teacher_id = get_input_with_validation("Enter teacher ID: ", validate_teacher_id)
                print(teacher_manager.view_teacher_info(teacher_id))

            elif choice == "5":
                break

            else:
                print("Invalid choice: try again")

        except ValueError as e:
            print(f"Error: {e}")


def handle_courses_menu(course_manager, student_manager, teacher_manager):
    while True:
        print()
        SystemMenu.courses_menu()
        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                print("\n===== Add New Course =====")
                course_name = get_input_with_validation("Enter course name: ", validate_course_name)
                try:
                    course_manager.get_course(course_name)
                    print(DUPLICATE_COURSE_ERROR)
                    continue
                except ValueError:
                    pass
                max_students = get_input_with_validation("Enter max number of students: ", validate_max_students)
                teacher_id = get_input_with_validation("Enter teacher ID for this course: ", validate_teacher_id)
                teacher = teacher_manager.get_teacher(teacher_id)
                course = Course(course_name, max_students, teacher)
                course_manager.add_course(course)
                print("Course added successfully")

            elif choice == "2":
                print("\n===== Delete Course =====")
                course_name = get_input_with_validation("Enter course name: ", validate_course_name)
                course_manager.delete_course(course_name)
                print("Course deleted successfully")

            elif choice == "3":
                print("\n===== Add Student to Course =====")
                course_name = get_input_with_validation("Enter course name: ", validate_course_name)
                try:
                    course_manager.get_course(course_name)
                except ValueError as e:
                    print(f"Error: {e}")
                    continue
                student_id = get_input_with_validation("Enter student ID: ", validate_student_id)
                student = student_manager.get_student(student_id)
                course_manager.add_student_to_course(course_name, student)
                print("Student added to course successfully")

            elif choice == "4":
                print("\n===== Remove Student from Course =====")
                course_name = get_input_with_validation("Enter course name: ", validate_course_name)
                try:
                    course_manager.get_course(course_name)
                except ValueError as e:
                    print(f"Error: {e}")
                    continue
                student_id = get_input_with_validation("Enter student ID: ", validate_student_id)
                course_manager.remove_student_from_course(course_name, student_id)
                print("Student removed from course successfully")

            elif choice == "5":
                print("\n===== Change Course Teacher =====")
                course_name = get_input_with_validation("Enter course name: ", validate_course_name)
                try:
                    course_manager.get_course(course_name)
                except ValueError as e:
                    print(f"Error: {e}")
                    continue
                teacher_id = get_input_with_validation("Enter new teacher ID: ", validate_teacher_id)
                teacher = teacher_manager.get_teacher(teacher_id)
                course_manager.change_course_teacher(course_name, teacher)
                print("Course teacher updated successfully")

            elif choice == "6":
                print("\n===== Course Information =====")
                course_name = get_input_with_validation("Enter course name: ", validate_course_name)
                print(course_manager.view_course_info(course_name))

            elif choice == "7":
                break

            else:
                print("Invalid choice: try again")

        except ValueError as e:
            print(f"Error: {e}")


def handle_reports_menu(report_manager):
    while True:
        print()
        SystemMenu.reports_menu()
        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                print("\n===== All Students =====")
                students = report_manager.list_of_students()
                if not students:
                    print("No students found")
                else:
                    for line in students:
                        print(line)
                        print()

            elif choice == "2":
                print("\n===== All Teachers =====")
                teachers = report_manager.list_of_teachers()
                if not teachers:
                    print("No teachers found")
                else:
                    for line in teachers:
                        print(line)
                        print()

            elif choice == "3":
                print("\n===== All Courses =====")
                courses = report_manager.list_of_courses()
                if not courses:
                    print("No courses found")
                else:
                    for line in courses:
                        print(line)
                        print()

            elif choice == "4":
                print("\n===== List Students in a Course =====")
                course_name = get_input_with_validation("Enter course name: ", validate_course_name)
                students = report_manager.list_students_in_course(course_name)
                if not students:
                    print(f"No students enrolled in '{course_name}'")
                else:
                    for line in students:
                        print(line)
                        print()

            elif choice == "5":
                print("\n===== Statistics =====")
                stats = report_manager.show_statistics()
                print(f"Total Students: {stats['total_students']}")
                print(f"Total Teachers: {stats['total_teachers']}")
                print(f"Total Courses: {stats['total_courses']}")

            elif choice == "6":
                break

            else:
                print("Invalid choice: try again")
        except ValueError as e:
            print(f"Error: {e}")


def main():
    student_manager = StudentManager()
    teacher_manager = TeacherManager()
    course_manager = CourseManager()
    report_manager = ReportManager(student_manager, teacher_manager, course_manager)

    print("\n" + "=" * 50)
    print("   Welcome to the Student Management System")
    print("=" * 50)

    while True:
        print()
        SystemMenu.main_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            handle_students_menu(student_manager)

        elif choice == "2":
            handle_teachers_menu(teacher_manager)

        elif choice == "3":
            handle_courses_menu(course_manager, student_manager, teacher_manager)

        elif choice == "4":
            handle_reports_menu(report_manager)

        elif choice == "5":
            print("\n" + "=" * 50)
            print("   Thank you for using Student Management System")
            print("             Exiting the program...")
            print("=" * 50 + "\n")
            break

        else:
            print("Invalid choice: try again")


if __name__ == "__main__":
    main()
