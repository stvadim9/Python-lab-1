class Student:
    def __init__(self,name,age,sex,phone):
        self.name = name
        self.age = age
        self.sex = sex
        self.phone = phone

    def printData(student,name,age,sex,phone):
        print("Name: ",student.name)
        print("Age: ",student.age)
        print("Sex: ",student.sex)
        print("Phone: ",student.phone)

print ("Enter name: ")
name = input()
print ("Enter Age: ")
age = int(input())
print ("Enter sex: ")
sex = input()
print ("Enter phone: ")
phone = int(input())

student = Student(name,age,sex,phone)

Student.printData(student,name,age,sex,phone)

online = True

while online == True:

    print("Change some data?")
    print("1.Change name")
    print("2.Change age")
    print("3.Change sex")
    print("4.Change phone")
    print("5.End programm")

    choice = int(input("Enter 1-4: "))

    if (choice == 1):
        print ("Enter name: ")
        name = input()
        student = Student(name,age,sex,phone)
        Student.printData(student,name,age,sex,phone)

    elif (choice == 2):
        print ("Enter age: ")
        age = input()
        student = Student(name,age,sex,phone)
        Student.printData(student,name,age,sex,phone)

    elif (choice == 3):
        print ("Enter sex: ")
        sex = input()
        student = Student(name,age,sex,phone)
        Student.printData(student,name,age,sex,phone)

    elif (choice == 4):
        print ("Enter phone: ")
        phone = input()
        student = Student(name,age,sex,phone)
        Student.printData(student,name,age,sex,phone)

    elif (choice == 5):
        online = False
