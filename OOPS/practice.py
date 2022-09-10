# Assigning lambda functions to a variable
mul = lambda a,b:a*b
print(mul(5,2))

# Wrapping lambda functions inside another function:
def myWrapper(n):
    return lambda a:a*n

mymul = myWrapper(5)
print(mymul(2))