def pal(nu):
    nu=str(nu)
    tmp=nu[::-1]
    if tmp==nu:
        return "Yes"
    else:
        return "Not"
    
def mx(ar):
    x=len(ar)
    tmp1=ar[0]
    for i in range(0,x):
        if ar[i]>tmp1:
            tmp1=ar[i]
    return tmp1

nom=int(input("Enter the size of array : "))
print("Enter the elements of array")
ar1=[]
for i in range(0,nom):
    tmp2=int(input())
    ar1.append(tmp2)
ar2=[]
for i in ar1:
    if pal(i)=="Yes":
        ar2.append(i)
        
print(mx(ar2))