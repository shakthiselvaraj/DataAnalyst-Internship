# Creating Class and Object

class humans:
    def ab(self):
        print('Hii')

human1 = humans()
human2 = humans()
human1.ab()
human2.ab()


# Initializing  Variable in Class

class humans:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def ab(self):
        print('Name is :', self.name)
        print('Age is:', self.age)

human1 = humans('yox',23)
human2 = humans('vera',25)
human1.ab()
human2.ab()


# Types of Variables

class humans:

# Class variable
    gender = 'Female'
# Instance Variable
    def __init__(self, name, age):
        self.name = name
        self.age = age



human1 = humans('yox',23)
human2 = humans('ver',25)

print('Name:', human1.name,'Age:', human1.age,'Gender:', humans.gender)
print('Name:', human2.name,'Age:', human2.age,'Gender:', humans.gender)

# Types of Methods

class students:

    school = 'ABCD'

    def __init__(self,mark1,mark2,mark3):
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def avg(self):
        return (self.mark1 + self.mark2 + self.mark3)/3


    @classmethod

    def info(cls):
        return cls.school

    @staticmethod

    def message():
        print('Hi Students!!')

s1 = students(80,65,75)
s2 = students(95,85,88)

students.message()
print('From', s1.info(), 'School','Your marks:', s1.mark1, s1.mark2, s1.mark3,'and Average:', s1.avg())
print('From', s2.info(), 'School','Your marks:', s2.mark1, s2.mark2, s2.mark3,'and Average:', s2.avg())








