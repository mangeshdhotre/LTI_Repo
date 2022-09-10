class Father:
    def __init__(self):
        print("You are in father class constructor")

    def disp(self):
        print("Father class instance method")


class Mother:
    def __init__(self):
        print("You are in mother class constructor")

    def show(self):
        print("Mother class instance method")


class Son(Mother,Father):
    def __init__(self):
        print("You are in Son class constructor")


s = Son()
s.disp()
s.show()

