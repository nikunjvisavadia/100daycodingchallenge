word=input("Enter a string : ")
fin=""
for i in word:
    if i.lower() in ('a','e','i','o','u'):
        pass
    else:
        fin=fin+i
print(fin)