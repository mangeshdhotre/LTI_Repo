class Employee:
    company="Google"
    salary = 100

harry=Employee()
rajni=Employee()

print(harry.company) 
print(rajni.company)
rajni.company = "Youtube"
rajni.salary=410
print(harry.company)
print(rajni.company)

print(harry.salary)
print(rajni.salary)