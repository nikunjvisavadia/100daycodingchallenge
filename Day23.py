num=int(input("Enter a number: "))
s=str(num)
new=[]
for i in s:
    if(i=='0'):
        new.append('1')
    else:
        new.append(i)
newn=""
for i in new:
    newn+=i
print(int(newn))