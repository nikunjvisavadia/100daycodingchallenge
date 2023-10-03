num=int(input())
for i in range(0,num):
    a1,a2,a3,a4,a5,a6,a7=list(map(int, input().split(' ')))
    ar1=[a1,a2,a3,a4,a5,a6,a7]
    sum=0
    for i in ar1:
        if i==1:
            sum +=1
    if sum>3:
        print("YES")
    else:
        print("NO")