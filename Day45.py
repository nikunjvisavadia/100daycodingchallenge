def sml(ar):
    x=len(ar)
    tmp=ar[0]
    for i in range(0,x):
        if ar[i]<tmp:
            tmp=ar[i]
    return tmp

def lrg(ar):
    x=len(ar)
    tmp=ar[0]
    for i in range(0,x):
        if ar[i]>tmp:
            tmp=ar[i]
    return tmp

        
no=int(input("Enter number of element in array : "))
ar1=[]

for i in range(0,no):
    tmp=int(input())
    ar1.append(tmp)

print("Smallest number in array is : ", sml(ar1))

print("Largest number in array is : ", lrg(ar1))