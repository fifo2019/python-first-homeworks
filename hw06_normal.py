# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class Parent(object):
    def __init__(self, name):
        self.first_name, self.middle_name, self.last_name = name.split()

    def __str__(self):
        return "Имя: {}, Отчество: {}, Фамилия: {}".format(self.first_name, self.middle_name, self.last_name)


class Student(object):
    def __init__(self, name, parents, classroom):
        self.first_name, self.middle_name, self.last_name = name.split()
        self.mother, self.father = parents
        self.classroom = classroom

    def __str__(self):
        return "{} {} {} из {}".format(self.first_name, self.middle_name, self.last_name, self.classroom)


class Classroom(object):
    def __init__(self, number):
        self.number = number
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def get_students(self):
        return self.students

    def get_teachers(self):
        return self.teachers

    def __str__(self):
        return self.number


class Teacher(object):
    def __init__(self, name, science):
        self.first_name, self.middle_name, self.last_name = name.split()
        self.classrooms = []
        self.science = science

    def add_classroom(self, classroom):
        self.classrooms.append(classroom)

    def get_classrooms(self):
        return self.classrooms

    def __str__(self):
        return "{} {} {} преподает {} в {}".format(self.first_name, self.middle_name, self.last_name, self.science, " ".join(self.classrooms))


class School(object):
    def __init__(self, classrooms):
        self.classrooms = {i:Classroom(i) for i in classrooms}
        self.teachers = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)
        for i in teacher.get_classrooms():
            self.classrooms[i].add_teacher(teacher)

    def add_student(self, student):
        self.classrooms[student.classroom].add_student(student)

    def get_students(self, classroom):
        return self.classrooms[classroom].get_students()

    def get_sciences(self, student):
        return [i.science for i in self.classrooms[student.classroom].get_teachers()]

    def __str__(self):
        return " ".join(self.classrooms)


mother = Parent("Мария Федоровна Романова")
father = Parent("Николай Александрович Романов")

vasya = Student("Василий Иванович Чапаев", [mother, father], "3А")
kolya = Student("Николай Васильевич Гоголь", [mother, father], "4Б")

school = School(["3А", "4Б", "5В", "6Г"])
print(school)

school.add_student(vasya)
school.add_student(kolya)

for i in school.get_students("3А"):
    print(i)

print("Мама Коли: {}\nПапа Коли: {}".format(kolya.mother, kolya.father))

teacher = Teacher("Иванов Иван Иванович", "физика")
teacher.add_classroom("5В")
teacher.add_classroom("6Г")
print(teacher)

print("Все предметы Васи:")
teacher.add_classroom("3А")
school.add_teacher(teacher)
print(" ".join(school.get_sciences(vasya)))