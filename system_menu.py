class SystemMenu:
    @staticmethod
    def main_menu():
        print("""===== Student Management System =====
1. Manage Students
2. Manage Teachers
3. Manage Courses
4. Reports
5. Exit""")
        
    @staticmethod
    def students_menu():
        print("""===== Students Menu =====
1. Add Student
2. Update Student Grades
3. Add Grade to Student
4. Delete Student
5. View Student Info
6. Back to main menu""")
    
    @staticmethod
    def teachers_menu():
        print("""===== Teachers Menu =====
1. Add Teacher
2. Update Teacher Salary
3. Delete Teacher
4. View Teacher Info
5. Back to main menu""")

    @staticmethod   
    def courses_menu():
        print("""===== Courses Menu =====
1. Add Course
2. Delete Course
3. Add Student to Course
4. Remove Student from Course
5. Change Course Teacher
6. View Course Info
7. Back to main menu""")
    
    @staticmethod
    def reports_menu():
        print("""===== Reports Menu =====
1. List of Students
2. List of Teachers
3. List of Courses
4. List Students in a Course
5. Show Statistics
6. Back to main menu""")
