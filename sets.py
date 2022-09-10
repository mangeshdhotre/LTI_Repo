a={1,2,3,4,5}
print(a)
print(type(a))

q={} #this create empty dictionary not empty set
print(type(q))

b=set()
print(type(b))
b.add(4)
b.add(9)
b.add(1)
print(b)

print(len(b))
b.remove(4)
# b.remove(10) print error because 15 is not in set
print(b)
print(b.pop())
# print(b.claer()) clear the set
