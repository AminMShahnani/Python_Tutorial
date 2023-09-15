"""
Object Oriented Programming
"""

class Student: 
    pass

student_1 = Student()
student_2 = Student()

student_1.first_name = 'Eric'
student_1.last_name = 'Roby'
student_1.major = 'Computer Science'

student_2.first_name = 'John'
student_2.last_name = 'Miller'
student_2.major = 'Math'


print(student_1.first_name)
print(student_2.first_name)

######################################################

class Teacher :

    number_of_teacher = 0
    school = 'Online School'


    def __init__(self, first_name, last_name, major):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major

        Teacher.number_of_teacher += 1

    def fullname_with_major(self) :
        return f'{self.first_name} {self.last_name} is a ' \
                f'{self.major} major!'

    def fullname_major_school(self) :
        return f'{self.first_name} {self.last_name} is a  ' \
                f'{self.major} going to {self.school}'
    
    @classmethod
    def set_online_school(cls, new_school) :
        cls.school = new_school

    @classmethod
    def split_teacher(cls, teacher_str) :
        first_name, last_name, major = teacher_str.split('.')
        return cls(first_name, last_name, major)

print(f'Number of teacher = {Teacher.number_of_teacher}')

teacher_1 = Teacher('Eric', 'Roby', 'Computer Science')
teacher_2 = Teacher('John', 'Miller', 'Math')

print(f'Number of students = {Teacher.number_of_teacher}')


print(teacher_1)
print(teacher_2)

print(teacher_1.first_name)
print(teacher_2.first_name)

print(teacher_1.fullname_with_major())
print(teacher_2.fullname_with_major())

print(Teacher.fullname_with_major(teacher_1))
print(Teacher.fullname_with_major(teacher_2))

print(teacher_1.school)
print(teacher_2.school)

print(teacher_2.fullname_major_school())
print(teacher_1.fullname_major_school())

print(teacher_1.school)
print(teacher_2.school)
Teacher.set_online_school('I use Google Hangouts for class!')
print(teacher_1.school)
print(teacher_2.school)

new_teacher = 'Adilew.Bokolr.English'
teacher_3 = Teacher.split_teacher(new_teacher)
print(teacher_3.first_name)
print(teacher_3.fullname_with_major())
print(teacher_3.fullname_major_school())

######################################################