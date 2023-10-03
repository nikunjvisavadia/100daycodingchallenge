no=int(input("Enter number of element in array : "))
ar1=[]

for i in range(0,no):
    tmp=int(input())
    ar1.append(tmp)
    
o=0
e=0
for j in ar1:
    if j%2==0:
        e+=1
    else:
        o+=1

print("Number of odd element in the array are : ", o)
print("Number of even element in the array are : ", e)