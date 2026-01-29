# 🎓 Student Management System

A comprehensive **Command-Line Interface (CLI)** application built with Python using **Object-Oriented Programming (OOP)** principles. This system allows educational institutions to manage students, teachers, and courses efficiently with robust validation and error handling.

---

## 📋 Table of Contents

- [Features](#-features)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [Menu Structure](#-menu-structure)
- [OOP Concepts Implemented](#-oop-concepts-implemented)
- [Data Validation](#-data-validation)
- [Testing Scenarios](#-testing-scenarios)

---

## ✨ Features

### 👨‍🎓 Student Management
- **Add Student**: Register new students with name, age, ID, and optional initial grades
- **Update Grades**: Replace a student's entire grade list
- **Add Grade**: Append a single new grade to a student's record
- **Delete Student**: Remove a student from the system (automatically updates total student count)
- **View Info**: Display detailed student information including calculated average grade

### 👨‍🏫 Teacher Management
- **Add Teacher**: Register new teachers with name, age, ID, and salary
- **Update Salary**: Modify a teacher's salary with validation
- **Delete Teacher**: Remove a teacher from the system (automatically updates total teacher count)
- **View Info**: Display detailed teacher information

### 📚 Course Management
- **Add Course**: Create new courses with name, maximum student capacity, and assigned teacher
- **Delete Course**: Remove courses from the system
- **Enroll Student**: Add a student to a specific course (validates capacity and prevents duplicates)
- **Remove Student**: Unenroll a student from a course
- **Change Teacher**: Assign a different teacher to an existing course
- **View Info**: Show course details including current enrollment and capacity

### 📊 Reports & Statistics
- **List All Students**: Detailed list of every registered student with grades and averages
- **List All Teachers**: Detailed list of every registered teacher with salary information
- **List All Courses**: Detailed list of every available course with enrollment status
- **List Students in a Course**: View all students enrolled in a specific course
- **System Statistics**: Real-time counts of total students, teachers, and courses

---

## 📁 Project Structure

```
Student-Management-System/
│
├── main.py                 # Main entry point and UI logic
├── person.py               # Base class for Student and Teacher
├── student.py              # Student class 
├── teacher.py              # Teacher class 
├── course.py               # Course class 
├── student_manager.py      # CRUD operations for students
├── teacher_manager.py      # CRUD operations for teachers
├── course_manager.py       # CRUD operations for courses
├── report_manager.py       # Generates reports and statistics
├── system_menu.py          # Static methods for CLI menu display
├── validators.py           # Centralized validation functions
└── README.md               # Project documentation
```

---

## 🚀 Installation

### Prerequisites
- Python 

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/mohamed-abdelazizz/OOP-Project-Student-Management-System.git
   ```

2. **Navigate to the project directory**
   ```bash
   cd OOP-Project-Student-Management-System
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

---

## 🎮 Usage

When you run the application, you will be greeted with the main menu:

```
==================================================
   Welcome to the Student Management System
==================================================

===== Student Management System =====
1. Manage Students
2. Manage Teachers
3. Manage Courses
4. Reports
5. Exit
Enter your choice:
```

### Recommended Workflow

1. **Add Students**: Register students into the system
2. **Add Teachers**: Teachers are required to create courses
3. **Create Courses**: Create courses and assign teachers
4. **Enroll Students**: Add students to courses
5. **Manage Data**: Update grades, salaries, or other information
6. **Generate Reports**: View lists and statistics

### Example Usage Flow

```
1. Add students → "Mohamed" (ID: 20210325)
2. Add a teacher → "Dr Ahmed" (ID: 20001000, Salary: 10000)
3. Create course → "Mathematics" (Max: 30, Teacher: 20001000)
4. Enroll students → Add student 20210325 to Mathematics
5. Update grades → Add grades for students
6. View reports → See all students in Mathematics course
```

---

## 🗂️ Menu Structure

```
Main Menu
├── 1. Manage Students
│   ├── 1. Add Student
│   ├── 2. Update Student Grades
│   ├── 3. Add Grade to Student
│   ├── 4. Delete Student
│   ├── 5. View Student Info
│   └── 6. Back to main menu
│
├── 2. Manage Teachers
│   ├── 1. Add Teacher
│   ├── 2. Update Teacher Salary
│   ├── 3. Delete Teacher
│   ├── 4. View Teacher Info
│   └── 5. Back to main menu
│
├── 3. Manage Courses
│   ├── 1. Add Course
│   ├── 2. Delete Course
│   ├── 3. Add Student to Course
│   ├── 4. Remove Student from Course
│   ├── 5. Change Course Teacher
│   ├── 6. View Course Info
│   └── 7. Back to main menu
│
├── 4. Reports
│   ├── 1. List of Students
│   ├── 2. List of Teachers
│   ├── 3. List of Courses
│   ├── 4. List Students in a Course
│   ├── 5. Show Statistics
│   └── 6. Back to main menu
│
└── 5. Exit
```

---

## 🧠 OOP Concepts Implemented

This project applies core OOP principles and additional design principles:

| Concept | Key idea | Where used |
|--------|----------|------------|
| Inheritance | Share common attributes/behaviors through a base class | `Student`, `Teacher` inherit from `Person` |
| Encapsulation | Use private attributes with validated accessors | Private fields with `@property` in `Person`, `Student.grades`; `Course.__students` |
| Polymorphism | Same interface, different implementations | `get_info()` in `Person`, `Student`, `Teacher` |
| Abstraction | Hide complexity behind simpler interfaces | `StudentManager`, `TeacherManager`, `CourseManager`, `validators.py` |
| Composition | HAS-A relationships between objects | `Course` has a `Teacher` and a collection of `Students` |
| Class/Static Methods | Class-level counters and utility functions | `Student.get_total_students`, `Teacher.get_total_teachers`; `SystemMenu` static menus |

---



## 🛡️ Data Validation

The system implements comprehensive input validation with clear error messages:

### Validation Rules

| Field | Rules | Examples |
|-------|-------|----------|
| **Name** | String of words, each ≥2 alphabetic chars | ✅ `Mohamed Ahmed`<br>❌ `M`, `Mohamed123` |
| **Age** | Integer between 1-120 | ✅ `25`, `18`<br>❌ `0`, `150`, `abc` |
| **Student ID** | String of digits, length 1-10, >0 | ✅ `20210325`, `123456`<br>❌ `0`, `-1`, `abc` |
| **Teacher ID** | String of digits, length 1-10, >0 | ✅ `20001000`, `789101`<br>❌ `0`, `12345678901` |
| **Grade** | Integer between 0-100 | ✅ `85`, `100`<br>❌ `150`, `-10`, `abc` |
| **Salary** | Number ≥3000 (commas allowed) | ✅ `5000`, `50,000`<br>❌ `2000`, `abc` |
| **Course Name** | String of words, each ≥2 alphabetic chars | ✅ `Mathematics`, `NLP`<br>❌ `Math1`, `CS_101` |
| **Max Students** | Integer >0 | ✅ `30`, `50`<br>❌ `0`, `-5`, `abc` |



### Error Handling

- All validation functions raise `ValueError` with descriptive messages
- Input loops continue until valid data is provided
- User-friendly error messages guide correct input format

---

## ✅ Testing Scenarios

The system has been thoroughly tested with various input scenarios:

### Valid Input Tests

| Test Case | Input | Expected Result |
|-----------|-------|-----------------|
| Add Student | Name: `Mohamed Ahmed`<br>Age: `22`<br>ID: `20210325`<br>Grades: `85, 90, 95`| ✅ Student added successfully |
| Add Teacher | Name: `Dr Asmaa`<br>Age: `35`<br>ID: `20001001`<br>Salary: `50,000` | ✅ Teacher added successfully |
| Add Course | Name: `NLP`<br>Max: `30`<br>Teacher ID: `20001001` | ✅ Course added successfully |
| Enroll Student | Course: `NLP`<br>Student ID: `20210325` | ✅ Student enrolled successfully |

### Invalid Input Tests

| Scenario | Input | Error Message |
|----------|-------|---------------|
| Invalid Name | `J`, `Mohamed5`, `123` | Invalid name: must be a string of words, each with at least 2 alphabetic characters |
| Invalid Age | `-5`, `0`, `150`, `abc` | Invalid age: must be an integer between 1 and 120 |
| Invalid ID | `0`, `-1`, `abc`, `12345678901` | Invalid student/teacher ID: must be a string of digits, length 1-10, and greater than 0 |
| Invalid Grade | `150`, `-10`, `abc` | Invalid grade: must be an integer between 0 and 100 |
| Invalid Salary | `2000`, `abc`, `-5000` | Invalid salary: must be a number greater than or equal to 3000 |
| Duplicate Student | Existing student ID | Duplicate student: same student cannot be added twice |
| Duplicate Teacher | Existing teacher ID | Duplicate teacher: same teacher cannot be added twice |
| Duplicate Course | Existing course name | Duplicate course: same course cannot be added twice |
| Course Full | Add to full course | Cannot add student: maximum number of students exceeded |
| Student Not Found | Invalid student ID | Student not found |
| Teacher Not Found | Invalid teacher ID | Teacher not found |
| Course Not Found | Invalid course name | Course not found |

### Edge Cases Tested

- Empty grade lists (returns 0 average)
- Salary with commas (e.g., "50,000" → 50000.0)
- Names with multiple spaces (normalized to single space)
- Maximum capacity enforcement in courses
- Counter decrement on deletion

