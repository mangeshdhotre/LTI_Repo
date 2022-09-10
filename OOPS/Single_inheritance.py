class University:
    def __init__(self):
        self.name = "Pune University"
        print("You are in University class constructor ")


class Colleage(University):
    def show(self):
        print("You are in College class instance method", self.name)


col = Colleage()
col.show()