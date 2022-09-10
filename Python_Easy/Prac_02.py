
def findGreaterNumber(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] >= 100:
            count += 1
    return count

print("Enter Numbers ") #dont write this line in code
list = []
while(True):
    ele = int(input())
    list.append(ele)
    if ele == -1:
        break
result = findGreaterNumber(list)
print("OutPut" )  #dont write this line in code
print(result)
