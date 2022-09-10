f =open("sample.txt") 
data = f.readline() #print one line only from start

print(data)

data=f.readline()
print(data)
f.close()