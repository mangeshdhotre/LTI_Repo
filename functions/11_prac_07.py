

def replace_word(string,word):
    newstr=string.replace(word," ")
    return newstr.strip()


this="           harry is good person     "
s=replace_word(this,"harry")
print(s)