def artpe(ar):
    for i in ar:
        if (ar[i]%2)==0:
            return "Even"
        elif (ar[i]%2)==1:
            return "Odd"
        else:
            return "Mixed"

no=int(input("Enter number of element in array : "))
ar1=[]

for i in range(0,no):
    tmp=int(input())
    ar1.append(tmp)
    
print(artpe(ar1))