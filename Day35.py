word=input("Enter a string : ")
sum=0
for i in word:
    if i.isdigit()==True:
        z=int(i)
        sum=sum+z
print(sum)