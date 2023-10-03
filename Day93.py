t=int(input())
l=[]
l1=[]
for i in range(t):
    s=input()
    l.append(s)
    l1.append(int(s,2))
j=0
k=0
cout=0
while(j<t-1):
    k=j+1
    while(k<t):
        if(l[j][k]=="0" and (l1[j]&l1[k]>=1)):
            cout=cout+2
        k=k+1
    j=j+1
print(cout)