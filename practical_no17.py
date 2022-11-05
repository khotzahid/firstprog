#program for single inheritence
'''class C1:
    def a1(self):
        print("now in base class")
class C2(C1):
    def a2(self):
        print("now in derived class")

obj=C2()
obj.a2()
obj.a1()'''

#practical 17.2

'''class Student1:
    def __init__(self):
        self.name="islam"
        self.rollno=1
        print("father class constructor")
        print("\nreading marks of students")
        self.sub1=int(input("enter marks of subject1:"))
        self.sub2=int(input("enter marks of subject2:"))
        self.sub3=int(input("enter marks of subject3:"))

    def showdata(self):
        print(self.name,"is a student of gmk clg")
        print("rollno is",self.rollno)
        print("father class instance method")
class Student2(Student1):
    def display(self):
        self.total=self.sub1+self.sub2+self.sub3
        print("total marks obtained by "+self.name+'is',self.total)
        print("son class instance method")

s1=Student2()
print("student details")
s1.showdata()
s1.display()'''

#practical 17.3
#program for multiple inheritence
'''class C1:
    def a1(self):
        self.n1=7
        print("number 1=",self.n1)

class C2(C1):
    def a2(self):
        self.n2=8
        print("number 2=",self.n2)

class C3(C2):
    def add(self):
        #self.a1()
        #self.a2()
        self.n3=self.n1+self.n2
        return self.n3

c=C3()
c.a1()
c.a2()
sum=c.add()
print("sum=",sum)'''

#practical 17.4
#program to demonstrate use of super()
'''class C1:
    def a1(self):
        print("now in base class")

class C2(C1):
    def a1(self):
        print("now in derived class")
        super().a1()

obj1=C2()
obj1.a1()'''


#practical 17.5
#program to demonstrate use of method over
'''class C1:
    def f1(self):
        print("now in base class")

class C2(C1):
    def f1(self):
        print("now in derived class")

obj1=C2()
obj1.f1()
obj2=C1()
obj2.f1()'''

#practical 17.6
#program to demonstrate encapsulation
class C1:
    def __init__(self):
        self.__show()

    def show(self):
        print("hello")
        print("good")
        print("morning")
    def __show(self):
        print("hello good morning")
        a=20
        __b=25

obj = C1()
obj.show()
#obj.__show()
print(obj.a)