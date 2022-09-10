# class university():
#     def __init__(self):
#         self.name = "Pune University"
#         print("You are in University class constructor")
#
#     def disp(self):
#         print("University class instance method")
#
#
# def college(university):
#     def __init__(self):
#         self.name = "VPkBIET"
#         print("You are in college class constructor")
#
#     def show(self):
#         print("College class instance metnod",self.name)
#
#
# def student(college):
#     def __init__(self):
#         self.name = "Mangesh"
#         print("You are in Student class constructor")
#
#     def view(self):
#         print("Student class Instance method",self.name)
#
# s = student
# s.view

'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''


class University():
    def __init__(self):
        self.name = "Pune University"
        print("You are in University class constructor")

    def disp(self):
        print("You are in University class disp method")


class college(University):
    def __init__(self):
        self.name = "VPKBIET"
        print("You are in college class constructor")

    def show(self):
        print("college class instance method:", self.name)


class student(college):
    def __init__(self):
        self.name = "Mangesh"
        print("You are in student class constructor")

    def view(self):
        print("student class instancen method:", self.name)


s1 = student()
s1.view()
s1.show()
s1.disp()
