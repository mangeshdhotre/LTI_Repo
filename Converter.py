with open("CurrencyConverter.txt") as f:
    lines = f.readlines()

ConverterDict ={}
for line in lines:
    parsed = line.split("\t")
    ConverterDict[parsed[0]] = parsed[1]

amount = int(input("Enter amount :\n"))
print("Which currency you want to convert\n")
[print(item) for item in ConverterDict.keys()]
currName = input("Enter currency name :\n")
print(f"{amount} INR is equal to {amount *float(ConverterDict[currName])} {currName}  ")
