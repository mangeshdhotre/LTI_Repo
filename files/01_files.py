
f =open("sample.txt","r")  #by default mode is read
data = f.read()
# data = f.read(10) #only read 10 characters
print(data)
f.close()