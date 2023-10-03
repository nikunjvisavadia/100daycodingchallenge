num = int(input("Enter number of element in the array :"))

ar=[]

for i in range(0,num):
    tmp=int(input())
    ar.append(tmp)

print(sorted(ar))