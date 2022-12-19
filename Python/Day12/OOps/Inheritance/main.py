# Inheritance

# Single Inheritaance

class A:

    def f1(self):
        print('f1 is working')

    def f2(self):
        print('f2 is working')

class B(A):
    def f3(self):
        print('f3 is working')

a1 = A()
b1 = B()

a1.f2()

# b1 can access classA, classB
b1.f1()
b1.f3()


# Multilevel Inheritance

class school:

    def sclname(self):
        print('ABC School')

class mark(school):

    def marinfo(self):
        print('Your marks are Good!')

class student(mark):

    def info(self):
        print('student form class XI')


# class student can access class school, mark, student
s = student()

s.sclname()
s.info()
s.marinfo()





