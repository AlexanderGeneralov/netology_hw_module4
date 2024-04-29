
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)   
        
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
    
    def aver_grade(self): # calculae average grade on all courses
        total_grade = 0
        if self.grades:
            grade_amount = 0
            for v in self.grades.values():
                total_grade += sum(v)
                grade_amount += len(v)
            return round(total_grade / grade_amount, 1)
        return 0
    
    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.aver_grade()}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}")
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def aver_grade(self): # calculae average grade on all courses
        total_grade = 0
        if self.grades:
            grade_amount = 0
            for v in self.grades.values():
                total_grade += sum(v)
                grade_amount += len(v)
        return round(total_grade / grade_amount, 1)
    
    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self.aver_grade()}")    
    
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
            
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

def best_student(students): # returns name of a student with highest average grade on all courses
    grade = 0
    name = ""
    for student in students:
        if student.aver_grade() >= grade:
            grade = student.aver_grade()
            name = student.name
    return name
    
def best_lecturer(lecturers): # returns name of a lecturer with highest average grade on all courses
    grade = 0
    name = ""
    for lecturer in lecturers:
        if lecturer.aver_grade() >= grade:
            grade = lecturer.aver_grade()
            name = lecturer.name
    return name

def aver_grade_of_all_students(students, course): # returns avarage grade of all students on dedicated course
    res = 0
    for student in students:
        if course in student.courses_in_progress:
            res += sum(student.grades[course]) / len(student.grades[course])
    return round(res / len(students), 1)
    
def aver_grade_of_all_lecturers(students, course): # returns avarage grade of all lecturers on dedicated course
    res = 0
    for lecturer in lecturers:
        if course in lecturer.courses_attached:
            res += sum(lecturer.grades[course]) / len(lecturer.grades[course])
    return round(res / len(lecturers), 1)    

student1 = Student('Ruoy', 'Eman', 'your_gender')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['Git']
student1.finished_courses += ['Введение в программирование']
student2 = Student('Mike', 'Jugger', 'your_gender')
student2.courses_in_progress += ['C++']
student2.courses_in_progress += ['Python']
student2.finished_courses += ['Введение в программирование']

mentor1 = Mentor("Lary", "Hofman")
mentor2 = Mentor("Kily", "Monogue")

reviewer1 = Reviewer('Some', 'Buddy')
reviewer1.courses_attached += ['Python']
reviewer2 = Reviewer('Teddy', 'Bear')
reviewer2.courses_attached += ['Git']
reviewer2.courses_attached += ['Python']

lecturer1 = Lecturer("Ricky", "Martin")
lecturer1.courses_attached += ["Python"]
lecturer2 = Lecturer("Too", "Tired")
lecturer2.courses_attached += ["C++"]
lecturer2.courses_attached += ["Python"]

reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 8)
reviewer2.rate_hw(student2, 'Python', 7)
reviewer2.rate_hw(student2, 'Python', 10)
reviewer2.rate_hw(student2, 'Python', 7)


student1.rate_lecturer(lecturer1, "Python", 7)
student1.rate_lecturer(lecturer1, "Python", 9)
student2.rate_lecturer(lecturer2, "Python", 10)
student2.rate_lecturer(lecturer2, "Python", 8)


students = [student1, student2]
lecturers = [lecturer1, lecturer2]

print(reviewer1)
print(lecturer1)
print(student1)
print(f"Лучший студент: {best_student(students)}")
print(f"Лучший лектор: {best_lecturer(lecturers)}")
print(f"Средний бал всех студентов на курсе Python: {aver_grade_of_all_students(students, 'Python')}")
print(f"Средний бал всех лекторов на курсе Python: {aver_grade_of_all_lecturers(lecturers, 'Python')}")

