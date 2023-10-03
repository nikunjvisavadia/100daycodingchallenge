num=int(input("Enter a no: "))
s=0
while num!=0:
    s=s+num%10
    num=num//10
print(s)