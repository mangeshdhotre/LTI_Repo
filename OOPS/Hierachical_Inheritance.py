class University:     #Parent class
     def __init__(self):
         self.name = "Pune University"
         print("You are in University class constructor")

     def disp(self):
         print("You are in university class disp method")


class Medical_college(University):  #Child class one
    def __init__(self):
        self.name = "Pune Medical College"
        print("You are Medical college class constructor")

    def show(self):
        print("Medical_college class instance method:",self.name)


class Law_colleage(University):   #Child class two
    def __init__(self):
        self.name = "Pune Law College"
        print("You are Law college class constructor")

    def view(self):
        print("Law_college class instance method:",self.name)

med = Medical_college()
med.show()
med.disp()

law = Law_colleage()
law.view()
law.disp()