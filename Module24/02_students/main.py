class Student:

    def __init__(self, name, surname, age, group_number, raiting):
        self.name = name
        self.surname = surname
        self.age = age
        self.group_number = group_number
        self.raiting = raiting

    def info(self):
        print('Name: {}\nSurname: {}\nAge: {}\nGroup number: {}\nRaiting: {}'.format(
            self.name,
            self.surname,
            self.age,
            self.group_number,
            self.raiting
        ))

    def sort_raiting(self):
        return self.raiting


student_1 = Student('Dez', 'Schavr', 30, 106129, 6.5)
student_2 = Student('Nova', 'Novik', 29, 106129, 7.1)
student_3 = Student('Pashik', 'Gjdan', 30, 106129, 6.2)

students = [student_1, student_2, student_3]
sort_students = sorted(students, key=lambda x: x.sort_raiting())

for student in sort_students:
    print(student.name)
