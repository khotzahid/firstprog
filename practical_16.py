#my first class program
'''class st:
    def show(self):
        print("Good Morning")
s=st()
s.show()

#practical_16.2
#program with public and private data

class st:
    y=2
    __v=4
    def show(self):
        print("Good Morning")
        print("y=",self.y)
        print("x=",self.__v)
s=st()
s.show()
print(s.y)
print(s.__v)

#practical_16.3
#program to find marks obtained by student using class
class Student:
    def inputStudentData(self):
        self.rollno=int(input("Enter roll number:"))
        self.name=input("Enter student name:")
        print("Enter marks of three subject:")
        self.sub1=int(input("subject 1:"))
        self.sub2=int(input("subject 2:"))
        self.sub3=int(input("subject 3:"))
        self.MOBT=self.sub1+self.sub2+self.sub3
    def showStudentData(self):
        print("Roll number:",self.rollno)
        print("student's name:",self.name)
        print("Marks obtained:",self.MOBT)

  #  def Student(self):
   #     pass


s1=Student()
s1.Student()
s1.inputStudentData()
s1.showStudentData()

#practical_16.4
#write a program to declare a named as a student having two function to
class Student:
    def inputstudentData(self):
        self.rollno=int(input("Enter roll number:"))
        self.name=int(input("Enter student's name:"))
        print("Enter marks of three subject:")
        self.sub1=int(input("\t subject 1:"))
        self.sub2=int(input("\t subject 2:"))
        self.sub3=int(input("\t subject 3:"))
        self.MOTB=self.sub1+self.sub2+self.sub3
    def showstudentData(self):
        print("Roll number:",self.rollno)
        print("student's name:",self.name)
        print("Marks obtained",self.MOTB)
StudentList=[]
n=int(input("How many students:"))
for i in range(n):
    s=Student()
    s.inputstudentData()
    StudentList.append(s)
for i in StudentList:
    i.showstudentData()
print(StudentList)

#practical_16.5
#program to demonstrate use of constructor
class Student:
    def __init__(self,rollno,name,age):
        self.rollno=rollno
        self.name=name
        self.age=age
    def display(self):
        print(self.rollno,end='\t\t')
        print(self.name,end='\t\t')
        print(self.age)
rollno=int(input("Enter your rollno:"))
name=input("Enter Your Name:")
age=input("Enter Age:")
stu=Student(rollno,name,age)
stu.display()

#practical_16.6
#program to demonstrate deletion of an object
class Student:
    def __init__(self,rollno,name,age):
        self.rollno=rollno
        self.name=name
        self.age=age
    def display(self):
        print(self.rollno,end='\t\t')
        print(self.name,end='\t\t')
        print(self.age,end='\t\t')
    def __del__(self):
        print("object deleted")
rollno=int(input("Enter your rollno:"))
name=input("Enter your name:")
age=int(input("Enter your age:"))
stu=Student(rollno,name,age)
stu.display()
stu=Student(125,"Lalit",34)
stu.display()

#practical_16.7
#program to use a classs and pass parameter
class C1:
    def __init__(self,name,age):
        self.name=name
        self.age=age
st1=C1("Jasbir",45)
print(st1.name,st1.age)'''

#practical_16.8
#pragram to use distructor
class St:
    def __init__(self,n):
        print("Hel",n)
    def __del__(self):
        print("Deleted")
v=St("sonali")
v=St("Jasbir")