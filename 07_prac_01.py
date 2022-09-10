myfict={
    "pankha":"fan",
    "dabba":"box",
    "vastu":"item"
}
print("Options are",myfict.keys())
a = input("Enter the hindi word \n")
# print("the meaning of your word is",myfict[a])

print(myfict.get(a)) #canot raise erroe if value is nnot present