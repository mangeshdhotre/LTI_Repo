class Employee:
    company="Google"
    def getsalary(self,Signature):
        print(f"Salary is {self.salary} in company {self.company} \n{Signature}")
    

    def __init__(self):
        print("Employee is created")
        
    @staticmethod
    def greet():
        print("Good Morning , sir")

harry = Employee()
# harry.salary=100000
# harry.getsalary("Thanks!")# Employee.getsalary(harry)
# harry.greet()