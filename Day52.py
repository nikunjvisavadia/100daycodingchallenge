num=int(input("Enter the number of elements in an array : "))
ar1=list(map(int,input().split(' ')))
ar2=[]
j=num-1
while j>=0:
    tmp2=ar1[j]
    ar2.append(tmp2)
    j=j-1
print(ar2)