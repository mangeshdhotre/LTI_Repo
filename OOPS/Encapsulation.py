class student:
    def __init__(self):
        self.name = "Mangesh"  #Public Variable
        self._name = "Nimesh"  #Protected variable
        self.__name = "Vishvajit" #Private variable


st = student()
print(st.name)
print(st._name)
print(st._student__name)