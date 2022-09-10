class Employee:
    company="Google"
    def getsalary(self):
        print(f"Salary is {self.salary} in company {self.company}")


harry = Employee()
harry.salary=100000
harry.getsalary()# Employee.getsalary(harry)