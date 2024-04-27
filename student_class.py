
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
    
    def aver_grade(self):
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
    
    def aver_grade(self):
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

def best_student(students):
    return max(students, key=students.get)
    
def best_lecturer(lecturers):
    return max(lecturers, key=lecturers.get)

student1 = Student('Ruoy', 'Eman', 'your_gender')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['Git']
student1.finished_courses += ['Введение в программирование']
student2 = Student('Mike', 'Jugger', 'your_gender')
student2.courses_in_progress += ['C++']
student2.courses_in_progress += ['Git']
student2.finished_courses += ['Введение в программирование']


reviewer1 = Reviewer('Some', 'Buddy')
reviewer1.courses_attached += ['Python']
reviewer2 = Reviewer('Teddy', 'Bear')
reviewer2.courses_attached += ['Git']

lecturer1 = Lecturer("Ricky", "Martin")
lecturer1.courses_attached += ["Python"]
lecturer2 = Lecturer("Too", "Tired")
lecturer2.courses_attached += ["C++"]

reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 8)

student1.rate_lecturer(lecturer1, "Python", 7)
student1.rate_lecturer(lecturer1, "Python", 9)
student2.rate_lecturer(lecturer2, "C++", 10)
student2.rate_lecturer(lecturer2, "C++", 9)


students = {student1.name : student1.aver_grade(), student2.name : student2.aver_grade()}
lecturers = {lecturer1.name : lecturer1.aver_grade(), lecturer2.name : lecturer2.aver_grade()}

print(reviewer1)
print(lecturer1)
print(student1)
print(f"Лучший студент: {best_student(students)}")
print(f"Лучший лектор: {best_lecturer(lecturers)}")