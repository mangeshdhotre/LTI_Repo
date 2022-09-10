class University:
    def name(self):
        self.name = "Yele University"
        print("Name:",self.name)

class College(University):
    def name(self):
        # super().name()  #if u want access base class method
        self.name = "Yele medical college"
        print("Name:",self.name)

c = College()
c.name()

# u = University()
# u.name()