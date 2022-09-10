mydict= {
    "Fast":"In a quick manner",
    "Harry":"A coder",
     "marks":[100,200],
    "anotherdict":{"mangu":"Coder"},
    1: 2
}
# print(mydict)
# print(mydict["Fast"])
# print(mydict["Harry"])
# mydict["marks"]=[10,50]
# print(mydict["marks"])
# print(mydict["anotherdict"]["mangu"])
print(list(mydict.keys()))
print(mydict.values())
print(mydict.items())
updatedict={
    "Nimesh":"Friend"
}
mydict.update(updatedict) #update key value in dictionary
print(mydict)

print(mydict.get("Harry"))
print(mydict.get("Mangesh"))