def percent(marks):
    p =((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
    return p


marks = [45,56,99,55]
percentage1=percent(marks)

marks2 = [75,88,99,45]
percentage2=percent(marks2)
print(percentage1,percentage2)