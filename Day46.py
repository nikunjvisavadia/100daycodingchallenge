def sm(ar):
    sum=0
    for i in ar:
        sum+=i
    return sum

nu=int(input("Enter number of array elements : "))
ar1=[]
for i in range(0,nu):
    tmp=int(input())
    ar1.append(tmp)
    
print(sum(ar1))