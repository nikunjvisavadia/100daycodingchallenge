word=input("Enter a string : ")
new=""
for i in word:
    if i.islower()==True:
        new=new+i.upper()
    else:
        new=new+i.lower()
print(new)