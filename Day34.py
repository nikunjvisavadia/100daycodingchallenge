word= input("Enter a word : ")
new=""
for i in word:
    if ord(i) == 41 or ord(i) == 40 or ord(i) == 91 or ord(i) == 93 or ord(i) == 123 or ord(i) == 125:
        pass
    else:
        new=new+i
print(new)