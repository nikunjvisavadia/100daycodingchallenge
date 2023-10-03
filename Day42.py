al1=int(input("Enter the size of first array : "))
al2=int(input("Enter the size of second array : "))
ar1=[]
ar2=[]

for i in range(0,al1):
    tmp=int(input())
    ar1.append(tmp)

for j in range(0,al2):
    tmp2=int(input())
    ar2.append(tmp2)
    
if al1!=al2:
    print("Not Same")
elif ar1==ar2:
        print("Same")
else:
    print("Not Same")